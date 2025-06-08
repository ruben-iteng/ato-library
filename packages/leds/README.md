# leds

Various (addressable) LED components and modules

## Package Information

- Version: 0.2.2
- Total Modules: 2
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library/blob/main/packages/leds/README.md

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|![addressable_led_connector_driver](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_connector_driver.png)| addressable_led_connector_driver | - |
|![addressable_led_driver](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_driver.png)| addressable_led_driver | Addressable LED with decoupling capacitors.<br><br>    Usage:<br>    from "ruben-iteng/ato-library/leds/addressable_leds.ato" import AddressableLED<br><br>    module MyProject:<br>        ...<br>        leds = new AddressableLED[3]<br><br>        power = new ElectricPower<br>        data_in = new ElectricLogic<br><br>        for led in leds:<br>            led -> WS2812B_5050_Black<br>            led.power ~ power<br><br>        data_in ~> leds[0] ~> leds[1] ~> leds[2] |
