# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

import logging
from pathlib import Path

import faebryk.library._F as F
from faebryk.core.module import Module
from faebryk.libs.library import L

logger = logging.getLogger(__name__)

HERE = Path(__file__).parent


class faebrykLogo(Module):
    designator_prefix = L.f_field(F.has_designator_prefix)("LOGO")

    footprint: F.can_attach_to_footprint_symmetrically

    def __preinit__(self):
        self.footprint.attach(
            F.KicadFootprint.from_path(
                HERE
                / "footprints"
                / "footprints.pretty"
                / "faebrykLogo_8x9mm.kicad_mod"
            )
        )
