import logging

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.library import L
from faebryk.libs.units import P

logger = logging.getLogger(__name__)


class CurrentSensor(Module):
    """
    Current sensor module for easy connecting in your design.
    """

    # external interfaces
    power_source: F.ElectricPower
    power_sink: F.ElectricPower

    # traits
    @L.rt_field
    def can_bridge(self):
        return F.can_bridge_defined(self.power_source, self.power_sink)
