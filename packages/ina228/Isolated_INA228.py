# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

import logging

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.library import L
from faebryk.libs.util import not_none

logger = logging.getLogger(__name__)


class Isolated_INA228(Module):
    """INA228 with I2C and power isolation."""

    power_isolator: F.B0505S_1WR3_ReferenceDesign
    i2c_isolator: F.ISO1540
    ina228 = L.f_field(F.INA228_ReferenceDesign)(filtered=False, lowside=False)
    alarm_led = L.f_field(F.LEDIndicator)(use_mosfet=False)
    power_indicator: F.PoweredLED

    i2c: F.I2C
    power_5v: F.ElectricPower
    power_source: F.ElectricPower
    power_sink: F.ElectricPower

    @L.rt_field
    def bridge(self):
        return F.can_bridge_defined(self.power_source, self.power_sink)

    def __preinit__(self):
        # ----------------------------------------
        #                 Alias
        # ----------------------------------------
        power_isolated = self.power_isolator.power_out

        # ----------------------------------------
        #               Connections
        # ----------------------------------------
        # data
        self.i2c.connect_via(self.i2c_isolator, self.ina228.ina288.i2c)
        self.i2c_isolator.iso.i2c.terminate(owner=self)

        # power
        self.power_5v.connect(
            self.power_isolator.power_in,
        )
        self.i2c_isolator.non_iso.power.connect(self.i2c.sda.reference)
        power_isolated.connect(
            self.power_indicator.power,
            self.ina228.ina288.power,
            self.i2c_isolator.iso.power,
        )

        self.power_source.connect(self.ina228.power_source)
        self.power_sink.connect(self.ina228.power_load)

        # other
        self.ina228.ina288.alert.connect(self.alarm_led.logic_in)

        # ----------------------------------------
        #            parametrization
        # ----------------------------------------
        self.power_indicator.led.color.constrain_subset(F.LED.Color.RED)
        self.power_indicator.led.add(F.has_explicit_part.by_supplier("C2286"))
        self.alarm_led.led.led.color.constrain_subset(F.LED.Color.GREEN)
        self.alarm_led.led.led.add(F.has_explicit_part.by_supplier("C12624"))

        for res in self.get_children_modules(types=F.Resistor, include_root=True):
            parent = not_none(res.get_parent())[0]
            if not isinstance(parent, F.INA228_ReferenceDesign.ShuntedElectricPower):
                res.add(F.has_package(F.has_package.Package.R0402))

        for cap in self.get_children_modules(types=F.Capacitor, include_root=True):
            parent = not_none(cap.get_parent())[0]
            if not isinstance(
                parent, (F.B0505S_1WR3_ReferenceDesign, F.INA228_ReferenceDesign)
            ):
                cap.add(F.has_package(F.has_package.Package.C0603))
