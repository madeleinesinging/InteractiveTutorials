"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
# -------------------------------------------------------------------------
"""InteractiveTutorials\\editor\\scripts\\boostrap.py
Generated from O3DE PythonToolGem Template"""

import az_qt_helpers
import azlmbr.editor as editor
from interactivetutorials_dialog import InteractiveTutorialsDialog

if __name__ == "__main__":
    print("InteractiveTutorials.boostrap, Generated from O3DE PythonToolGem Template")

    # Register our custom widget as a dockable tool with the Editor under an Examples sub-menu
    options = editor.ViewPaneOptions()
    options.showOnToolsToolbar = True
    options.toolbarIcon = ":/InteractiveTutorials/toolbar_icon.svg"
    az_qt_helpers.register_view_pane('InteractiveTutorials', InteractiveTutorialsDialog, category="Examples", options=options)
