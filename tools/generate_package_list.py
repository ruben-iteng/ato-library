#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml", "typer", "jinja2"]
# ///

"""
Generate the README.md with updated list of packages
"""

import yaml
from pathlib import Path
import logging
import typer
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)


def sanitize_markdown_cell(text):
    """Sanitize text for markdown table cells."""
    return text.replace("\n", "<br>")


# Set up Jinja environment
template_dir = Path(__file__).parent.parent / "templates"
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
)
env.filters["md_cell"] = sanitize_markdown_cell


def get_module_docstring(file_path, module_name):
    """Extract the docstring for a specific module from a file.
    Looks for the docstring after the module definition.
    """
    try:
        logger.debug(
            f"Attempting to read docstring for module {module_name} from: {file_path}"
        )
        with open(file_path, "r") as f:
            content = f.read()

            # Find the module definition
            module_def = f"module {module_name}"
            module_pos = content.find(module_def)

            if module_pos == -1:
                logger.debug(f"Module {module_name} not found")
                return "-"

            # Look for triple-quote docstrings after the module definition
            content_after_module = content[module_pos:]
            for quote in ['"""', "'''"]:
                start = content_after_module.find(quote)
                if start != -1:
                    # Find the closing quotes
                    end = content_after_module.find(quote, start + 3)
                    if end != -1:
                        docstring = content_after_module[start + 3 : end].strip()
                        logger.debug(f"Found docstring using {quote}")
                        return docstring

            logger.debug("No docstring found")
            return "-"
    except Exception as e:
        logger.error(f"Failed to read docstring from {file_path}: {e}")
        return "-"


def find_module_file(package_dir, module_entry):
    """Find the module file from the entry point."""
    if not module_entry or ":" not in module_entry:
        return None

    module_path, class_name = module_entry.split(":")
    # The module file is named after the package (e.g. debug-headers.ato, relays.ato)
    file_path = package_dir / f"{package_dir.name}.ato"
    logger.debug(f"Looking for module file: {file_path}")
    return file_path, class_name


def main(
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug logging"),
):
    """Generate the README.md with updated list of packages."""
    # Set up logging based on debug flag
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

    packages_dir = Path("packages")
    packages_data = []

    # Find all directories with ato.yaml
    for package_dir in packages_dir.iterdir():
        if not package_dir.is_dir():
            continue

        ato_file = package_dir.joinpath("ato.yaml")
        if not ato_file.exists():
            continue

        logger.info(f"Processing package: {package_dir.name}")

        # Read and parse the ato.yaml file
        with open(ato_file, "r") as f:
            try:
                ato_config = yaml.safe_load(f)
                package_info = ato_config.get("package", {})
                builds = ato_config.get("builds", {})

                package_data = {
                    "name": package_dir.name,
                    "description": package_info.get("summary", "-"),
                    "version": package_info.get("version", "-"),
                    "num_modules": len(builds),
                    "modules": [],
                    "author": ", ".join(
                        author.get("name") for author in package_info.get("authors", [])
                    )
                    or "-",
                    "license": package_info.get("license", "-"),
                    "homepage": package_info.get("homepage", "-"),
                }

                # Process each module
                for build_name, build_info in builds.items():
                    module_info = find_module_file(package_dir, build_info.get("entry"))
                    if module_info is None:
                        build_description = "-"
                    else:
                        module_file, class_name = module_info
                        if module_file.exists():
                            build_description = get_module_docstring(
                                module_file, class_name
                            )
                        else:
                            build_description = "-"

                    package_data["modules"].append(
                        {
                            "name": build_name,
                            "description": sanitize_markdown_cell(build_description),
                        }
                    )

                packages_data.append(
                    {
                        "name": package_dir.name,
                        "description": sanitize_markdown_cell(
                            package_info.get("summary", "-")
                        ),
                        "version": package_info.get("version", "-"),
                        "num_modules": len(builds),
                        "modules": package_data["modules"],
                    }
                )

                # Generate package-specific README
                try:
                    package_template = env.get_template("package_readme.md.jinja")
                    package_readme = package_template.render(
                        package=package_data, ato_config=ato_config
                    )

                    readme_path = package_dir / "README.md"
                    with open(readme_path, "w") as f:
                        f.write(package_readme)
                        logger.info(f"Generated README at {readme_path}")
                except Exception as e:
                    logger.error(
                        f"Failed to generate package README for {package_dir.name}: {e}"
                    )

            except yaml.YAMLError as e:
                logger.error(f"Error parsing {ato_file}: {e}")
                continue

    # Generate main README
    try:
        main_template = env.get_template("main_readme.md.jinja")
        main_readme = main_template.render(packages=packages_data)

        with open("README.md", "w") as f:
            f.write(main_readme)
            logger.info(f"Wrote main README.md successfully to {Path('README.md')}")
    except Exception as e:
        logger.error(f"Failed to generate main README: {e}")


if __name__ == "__main__":
    typer.run(main)
