# usb

USB connectors and circuitry

## Package Information

- Version: 0.1.1
- Total Modules: 2
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|<img src="https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_2_0_type_c_data_power.png" alt="usb_2_0_type_c_data_power" width="250"/>| usb_2_0_type_c_data_power | USB 2.0 Type-C connector<br>    - 5V PD compatible<br>    - ESD protection<br>    - Fuse [500mA(hold), 1A(trip)] |
|<img src="https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_pd_power_sink.png" alt="usb_pd_power_sink" width="250"/>| usb_pd_power_sink | USB PD power sink with Type-C connector<br>    <br>    Set the requested PD voltages as follows:<br>    9V  -> resistance = 6.8kohm<br>    12V -> resistance = 24kohm<br>    15V -> resistance = 56kohm<br>    20V -> resistance = DNP<br>    pd_sink = new USBPDPowerSink<br>    pd_sink.pd_trigger.voltage_set_resistor.resistance = 56kohm +/- 1% |
