# -*- coding: utf-8 -*-
"""For test code.
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division


class Totalizer(object):
    def sam(self, one, two):
        return one + two


class DoubleTotalizer(Totalizer):
    def sam(self, one, two):
        result = super(DoubleTotalizer, self).sam(one, two)
        return result * 2
