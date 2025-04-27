import logging
from pathlib import Path
from functools import partial
from typing import List, Tuple

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.library import L

logger = logging.getLogger(__name__)

HERE = Path(__file__).parent


def _create_port_property(port: str, index: int):
    """Create a port property for the given port and index."""

    @property
    def port_property(self) -> F.ElectricLogic:
        """Access {port}[{index}]."""
        return getattr(self, port)[index]

    return port_property


def add_port_properties(port_configs: List[Tuple[str, List[int]]]):
    """
    Class decorator to add port properties.
    Args:
        port_configs: List of tuples containing (port_name, [indices])
        Example: [('PA', [0,1,2,3,4,5,6,7]), ('PB', [0,1,2,3,4,5,6,7])]
    """

    def decorator(cls):
        for port, indices in port_configs:
            for i in indices:
                setattr(cls, f"{port}{i}", _create_port_property(port, i))
        return cls

    return decorator


@add_port_properties(
    [
        ("PA", list(range(8))),  # PA0 through PA7
        ("PB", list(range(8))),  # PB0 through PB7
        ("PC", list(range(8))),  # PC0 through PC7
        ("rdy", list(range(2))),  # rdy0 through rdy1
        ("ctl", list(range(3))),  # ctl0 through ctl2
    ]
)
class BM9002A_56ILG_ReferenceDesign(F.CBM9002A_56ILG_ReferenceDesign):
    """
    Reference design for the BM9002A_56ILG microcontroller.
    """

    def __preinit__(self):
        self.reset_circuit.diode.add(
            F.has_explicit_part.by_supplier(
                supplier_partno="C2128",
                pinmap={
                    "1": self.reset_circuit.diode.cathode,
                    "2": self.reset_circuit.diode.anode,
                },
            )
        )

        # crystal
        self.oscillator.crystal.add(
            F.has_explicit_part.by_supplier(
                supplier_partno="C388793",
                pinmap={
                    "1": self.oscillator.crystal.unnamed[0],
                    "2": self.oscillator.crystal.gnd,
                    "3": self.oscillator.crystal.unnamed[1],
                    "4": self.oscillator.crystal.gnd,
                },
            )
        )
