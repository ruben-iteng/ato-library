# usb

USB connectors and circuitry

## Package Information

- Version: 0.3.1
- Total Modules: 4
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library/blob/main/packages/usb/README.md

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|![usb_2_0_type_c_data_power_vertical_connector](https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_2_0_type_c_data_power_vertical_connector.png)| usb_2_0_type_c_data_power_vertical_connector | USB 2.0 Type-C connector<br>    - 5V PD compatible<br>    - ESD protection<br>    - Fuse [500mA(hold), 1A(trip)]<br>    - Vertical USB Type-C connector |
|![usb_2_0_type_c_data_power_horizontal_connector](https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_2_0_type_c_data_power_horizontal_connector.png)| usb_2_0_type_c_data_power_horizontal_connector | USB 2.0 Type-C connector<br>    - 5V PD compatible<br>    - ESD protection<br>    - Fuse [500mA(hold), 1A(trip)]<br>    - Horizontal USB Type-C connector |
|![usb_pd_power_sink_horizontal_connector](https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_pd_power_sink_horizontal_connector.png)| usb_pd_power_sink_horizontal_connector | USB PD power sink with Horizontal Type-C connector<br><br>    Set the requested PD voltages as follows:<br>    9V  -> resistance = 6.8kohm<br>    12V -> resistance = 24kohm<br>    15V -> resistance = 56kohm<br>    20V -> resistance = DNP<br>    pd_sink = new USBPDPowerSink<br>    pd_sink.pd_trigger.voltage_set_resistor.resistance = 56kohm +/- 1% |
|![usb_pd_power_sink_vertical_connector](https://github.com/ruben-iteng/ato-library/raw/main/packages/usb/assets/usb_pd_power_sink_vertical_connector.png)| usb_pd_power_sink_vertical_connector | USB PD power sink with Vertical Type-C connector<br><br>    Set the requested PD voltages as follows:<br>    9V  -> resistance = 6.8kohm<br>    12V -> resistance = 24kohm<br>    15V -> resistance = 56kohm<br>    20V -> resistance = DNP<br>    pd_sink = new USBPDPowerSink<br>    pd_sink.pd_trigger.voltage_set_resistor.resistance = 56kohm +/- 1% |
