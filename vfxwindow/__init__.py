"""Set the window class to be specific to whichever program is loaded.

TODO:
    Substance callbacks
    Add dialog code for each application
    Revise setDefault* methods

    # Potential breaking changes
    Change setDocked to setFloating
    Remove docked in favour of floating
    Remove *_VERSION constants
    Changed dialog to isDialog
    Remove processEvents
    Remove signalExists
"""

from __future__ import absolute_import

__all__ = ['VFXWindow']
__version__ = '1.9.0'

import sys
from . import application


def _setup_qapp():
    """Attempt to start a QApplication automatically in batch mode.
    The purpose of this is to override whatever the program uses.
    This must happen before any libraries are imported, as it's usually
    at that point when the QApplication is initialised.
    """
    from Qt import QtWidgets
    try:
        app = QtWidgets.QApplication(sys.argv)
    except RuntimeError:
        pass


if application.Maya:
    if application.Maya.batch:
        _setup_qapp()
        from .maya import MayaBatchWindow as VFXWindow
    else:
        from .maya import MayaWindow as VFXWindow

elif application.Nuke:
    if application.Nuke.batch:
        from .nuke import NukeBatchWindow as VFXWindow
    else:
        from .nuke import NukeWindow as VFXWindow

elif application.Houdini:
    from .houdini import HoudiniWindow as VFXWindow

elif application.Blender:
    from .blender import BlenderWindow as VFXWindow

elif application.Unreal:
    from .unreal import UnrealWindow as VFXWindow

elif application.Max:
    from .max import MaxWindow as VFXWindow

elif application.SubstanceDesigner:
    from .substance_designer import SubstanceDesignerWindow as VFXWindow

elif application.SubstancePainter:
    from .substance_painter import SubstancePainterWindow as VFXWindow

elif application.Fusion:
    from .fusion import FusionWindow as VFXWindow

elif application.CryEngine:
    from .cryengine import CryWindow as VFXWindow

else:
    from .standalone import StandaloneWindow as VFXWindow
