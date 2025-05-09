# leds

Various (addressable) LED components and modules

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
|<img src="https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_connector.png" alt="addressable_led_connector" width="250"/>| addressable_led_connector | - |
|<img src="https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led.png" alt="addressable_led" width="250"/>| addressable_led | Addressable LED with decoupling capacitors.<br><br>    Usage:<br>    from "ruben-iteng/ato-library/leds/addressable_leds.ato" import AddressableLED<br><br>    module MyProject:<br>        ...<br>        indicator = new AddressableLED<br>        indicator.led -> WS2812B_5050_Black |
