## Usage

### PCA9554/PCA9554A

```ato
import ElectricPower
import I2C

from "pca9554.ato" import NXP_Semiconductors_PCA9554_driver
from "pca9554.ato" import NXP_Semiconductors_PCA9554PW_TSSOP16_package
from "pca9554.ato" import NXP_Semiconductors_PCA9554BS_HVQFN16_4x4mm_package

from "pca9554.ato" import NXP_Semiconductors_PCA9554A_driver
from "pca9554.ato" import NXP_Semiconductors_PCA9554APW_TSSOP16_package
from "pca9554.ato" import NXP_Semiconductors_PCA9554ABS_HVQFN16_4x4mm_package

module Test:
    # Choose one the supported packages
    pca9554 = new NXP_Semiconductors_PCA9554_driver
    pca9554.package -> NXP_Semiconductors_PCA9554PW_TSSOP16_package
    #pca9554.package -> NXP_Semiconductors_PCA9554BS_HVQFN16_4x4mm_package
    pca9554a = new NXP_Semiconductors_PCA9554A_driver
    pca9554a.package -> NXP_Semiconductors_PCA9554APW_TSSOP16_package
    #pca9554a.package -> NXP_Semiconductors_PCA9554ABS_HVQFN16_4x4mm_package

    # Create power and I2C interfaces
    power = new ElectricPower
    i2c = new I2C

    # Connect IO expanders to power and I2C
    pca9554.power ~ power
    pca9554a.power ~ power
    pca9554.i2c ~ i2c
    pca9554a.i2c ~ i2c

    # Set IO expander addresses
    pca9554.i2c.address = 0x20
    pca9554a.i2c.address = 0x38

    # set parameters
    power.voltage = 3.3V +/- 10%
    i2c.frequency = 100kHz
```

### PCA9536

```ato
import ElectricPower
import I2C

from "pca9536.ato" import NXP_Semiconductors_PCA9536_driver
from "pca9536.ato" import NXP_Semiconductors_PCA9536D_S08_package
#from "pca9536.ato" import NXP_Semiconductors_PCA9536TK_HVSON8_package
#from "pca9536.ato" import NXP_Semiconductors_PCA9536DP_TSSOP8_package

module Test:
    # Choose one the supported packages
    pca9536 = new NXP_Semiconductors_PCA9536_driver
    pca9536.package -> NXP_Semiconductors_PCA9536D_S08_package
    #pca9536.package -> NXP_Semiconductors_PCA9536TK_HVSON8_package
    #pca9536.package -> NXP_Semiconductors_PCA9536DP_TSSOP8_package

    # Create power and I2C interfaces
    power = new ElectricPower
    i2c = new I2C

    # Connect IO expanders to power and I2C
    pca9536.power ~ power
    pca9536.i2c ~ i2c

    # set parameters
    power.voltage = 3.3V +/- 10%
    i2c.frequency = 100kHz
```
