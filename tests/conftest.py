import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/"))


__maya_test = bool(os.environ.get("MAYA_TEST"))
maya_flag = False


@pytest.fixture(scope="session", autouse=__maya_test)
def check_maya_test():
    import maya.cmds as cmds
    import maya.standalone
    maya.standalone.initialize("python")
    info = cmds.about(installedVersion=True)
    # info = cmds.about(version=True)
    version = info.split(" ")
    print(version)
    yield
    maya.standalone.uninitialize()
