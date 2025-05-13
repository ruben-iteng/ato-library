# rs485

RS485 related modules

## Package Information

- Version: 0.1.4
- Total Modules: 4
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|![bus_protection](https://github.com/ruben-iteng/ato-library/raw/main/packages/rs485/assets/bus_protection.png)| bus_protection | RS485 bus protection.<br>    - Overvoltage protection<br>    - Overcurrent protection<br>    - Common mode filter<br>    - Termination resistor<br>    - ESD protection<br>    - Lightning protection<br><br>    based on: https://www.mornsun-power.com/public/uploads/pdf/TD(H)541S485H.pdf |
|![transceiver](https://github.com/ruben-iteng/ato-library/raw/main/packages/rs485/assets/transceiver.png)| transceiver | Simple UART to RS485 converter.<br>    UART and TNOW interface in, RS485 interface out. |
|![isolated_transceiver](https://github.com/ruben-iteng/ato-library/raw/main/packages/rs485/assets/isolated_transceiver.png)| isolated_transceiver | Isolated UART to half duplex RS485 interface |
|![isolated_powered_transceiver](https://github.com/ruben-iteng/ato-library/raw/main/packages/rs485/assets/isolated_powered_transceiver.png)| isolated_powered_transceiver | Isolated powered UART to RS485 transceiver design block.<br>    - 3.3V or 5V logic power<br>    - 3.3V or 5V module power<br>    - 0.5 Mbps UART<br>    - Read enable/write enable input<br>    - RS485 half duplex<br>    - ANSI/ESDA/JEDEC JS-001 ESD protection<br>    - JESD22-C101 CDM protection |
