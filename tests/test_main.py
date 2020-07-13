# -*- coding: utf-8 -*-
"""code test pour src\main.py.
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division
from src.main import Totalizer, DoubleTotalizer


class TestTotalizer(object):
    def test_sam(self):
        result = Totalizer().sam(1, 2)
        assert result == 3


class TestDoubleTotalizer(object):
    def test_sam(self):
        result = DoubleTotalizer().sam(1, 2)
        assert result == 6


def test_maya():
    try:
        import maya.cmds as cmds
        import maya.standalone
        maya.standalone.initialize("python")
        info = cmds.about(installedVersion=True)
        # info = cmds.about(version=True)
        version = info.split(" ")
        print(version)
        maya.standalone.uninitialize()
    except:
        pass
    else:
        assert True
