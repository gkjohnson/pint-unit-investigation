#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect, os
from pint import UnitRegistry

directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
ureg = UnitRegistry()
ureg.load_definitions(directory + '\\..\\units\\custom.txt')

# This throws an error because the underlying
# string conversion doesn't seem to be able to
# convert utf-8
val = ureg.Quantity(1, 'degF')
print val.to('°F')

# This throws an error because the unit expression
# tokenizer assumes percent is an operator
# Tokens defined here may be problematic:
# https://github.com/hgrecco/pint/blob/master/pint/compat/tokenize.py#L65
val = ureg.Quantity(1, 'ratio')
print val.to('%')