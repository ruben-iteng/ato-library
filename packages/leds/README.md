# leds

Various (addressable) LED components and modules

## Package Information

- Version: 0.2.2
- Total Modules: 8
- Author(s): Ruben Baldewsing
- License: MIT
- Homepage: https://github.com/ruben-iteng/ato-library/blob/main/packages/leds/README.md

## Available Modules

### Module List

| Image | Module | Description |
|-------|--------|-------------|
|![addressable_led_connector_driver](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_connector_driver.png)| addressable_led_connector_driver | - |
|![addressable_led_driver](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/addressable_led_driver.png)| addressable_led_driver | Addressable LED with decoupling capacitors.<br><br>    Usage:<br>    from "ruben-iteng/ato-library/leds/addressable_leds.ato" import AddressableLED<br><br>    module MyProject:<br>        ...<br>        leds = new AddressableLED[3]<br><br>        power = new ElectricPower<br>        data_in = new ElectricLogic<br><br>        for led in leds:<br>            led -> WS2812B_5050_Black<br>            led.power ~ power<br><br>        data_in ~> leds[0] ~> leds[1] ~> leds[2] |
|![red](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/red.png)| red | Hubei KENTO Elec KT-0603B Blue LED |
|![green](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/green.png)| green | Hubei KENTO Elec KT-0603B Blue LED |
|![blue](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/blue.png)| blue | Hubei KENTO Elec KT-0603B Blue LED |
|![yellow](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/yellow.png)| yellow | Hubei KENTO Elec KT-0603B Blue LED |
|![yellow_green](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/yellow_green.png)| yellow_green | Hubei KENTO Elec KT-0603B Blue LED |
|![white](https://github.com/ruben-iteng/ato-library/raw/main/packages/leds/assets/white.png)| white | Hubei KENTO Elec KT-0603B Blue LED |
