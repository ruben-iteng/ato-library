# leds

Various (addressable) LED components and modules

## Package Information

- Version: 0.1.2
- Total Modules: 2
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|![addressable_led_connector](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_connector.png)| addressable_led_connector | - |
|![addressable_led](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led.png)| addressable_led | Addressable LED with decoupling capacitors.<br><br>    Usage:<br>    from "ruben-iteng/ato-library/leds/addressable_leds.ato" import AddressableLED<br><br>    module MyProject:<br>        ...<br>        indicator = new AddressableLED<br>        indicator.led -> WS2812B_5050_Black |
