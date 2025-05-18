import logging

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.library import L
from faebryk.libs.units import P

logger = logging.getLogger(__name__)


class ShuntedElectricPower(Module):
    """
    Helper module to easily connect a shunt between two electric powers.
    Can be placed on either high or low side of power.
    """

    power_in: F.ElectricPower
    power_out: F.ElectricPower
    shunt_sense: F.DifferentialPair

    shunt: F.Resistor

    @L.rt_field
    def can_bridge(self):
        return F.can_bridge_defined(self.power_in, self.power_out)

    def __init__(self, lowside: bool = False, filtered: bool = False):
        super().__init__()
        self._lowside = lowside
        self._filtered = filtered

    def __preinit__(self):
        self.shunt_sense.p.line.connect_via(self.shunt, self.shunt_sense.n.line)
        # TODO: minus voltagedrop over shunt
        self.power_in.voltage.alias_is(self.power_out.voltage)
        if self._lowside:
            self.power_in.lv.connect_via(self.shunt, self.power_out.lv)
            self.power_in.hv.connect(self.power_out.hv)
        else:
            self.power_in.hv.connect_via(self.shunt, self.power_out.hv)
            self.power_in.lv.connect(self.power_out.lv)

        if self._filtered:
            assert NotImplementedError
            # filter_cap = self.add(F.Capacitor())
            # filter_resistors = L.list_field(2, F.Resistor)

            # filter_cap.capacitance.constrain_subset(
            #     L.Range.from_center_rel(0.1 * P.uF, 0.20)
            # )
            # filter_cap.max_voltage.constrain_ge(170 * P.V)
            # for res in filter_resistors:
            #     res.resistance.constrain_le(10 * P.ohm)
        # TODO: auto calculate, see: https://www.ti.com/lit/ug/tidu473/tidu473.pdf
