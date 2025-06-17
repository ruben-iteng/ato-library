#!/bin/bash

# This script is taken from https://github.com/atopile/packages

# Store the original directory and script directory
ORIGINAL_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"

# Create logs directory if it doesn't exist
mkdir -p "$ROOT_DIR/.logs"

# Arrays to store results
declare -a successful_builds=()
declare -a failed_builds=()
declare -A pids=()  # Store process IDs

# Function to handle errors
handle_error() {
    echo "❌ Error occurred in directory: $1"
    failed_builds+=("$1")
    return 1
}

# Change to packages directory
cd "$ROOT_DIR/packages" || handle_error "Could not change to packages directory"

# Loop through all directories and start builds in parallel
for dir in */; do
    if [ -d "$dir" ]; then
        dir_name=${dir%/}
        log_file="$ROOT_DIR/.logs/${dir_name}.log"
        echo "🔨 Starting build for package in $dir with arguments: $@"
        echo "📝 Logging output to: $log_file"
        (
            cd "$dir" && ato build "$@" > "$log_file" 2>&1
            if [ $? -eq 0 ]; then
                echo "✅ Successfully built $dir"
                echo "SUCCESS:$dir" > "/tmp/ato_build_${dir_name}.result"
            else
                echo "❌ Failed to build $dir"
                echo "FAIL:$dir" > "/tmp/ato_build_${dir_name}.result"
            fi
        ) &
        pids[$dir]=$!
    fi
done

# Wait for all background processes to complete
for dir in "${!pids[@]}"; do
    wait ${pids[$dir]}
    if [ -f "/tmp/ato_build_${dir%/}.result" ]; then
        result=$(cat "/tmp/ato_build_${dir%/}.result")
        rm "/tmp/ato_build_${dir%/}.result"
        if [[ $result == SUCCESS:* ]]; then
            successful_builds+=("$dir")
        else
            failed_builds+=("$dir")
        fi
    fi
done

# Return to original directory
cd "$ORIGINAL_DIR"

# Print summary report
echo -e "\n📊 Build Summary Report"
echo "====================="
echo -e "\n✅ Successful builds (${#successful_builds[@]}):"
for build in "${successful_builds[@]}"; do
    echo "  - $build"
done

echo -e "\n❌ Failed builds (${#failed_builds[@]}):"
for build in "${failed_builds[@]}"; do
    echo "  - $build"
done

echo -e "\n📈 Total packages: $((${#successful_builds[@]} + ${#failed_builds[@]}))"
echo "✅ Successful: ${#successful_builds[@]}"
echo "❌ Failed: ${#failed_builds[@]}"

# Exit with error if any builds failed
if [ ${#failed_builds[@]} -gt 0 ]; then
    exit 1
fi
