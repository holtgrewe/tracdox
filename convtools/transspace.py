#!/usr/bin/env python

from __future__ import print_function

import re
import sys

for line in sys.stdin:
  print(line.replace('\xc2\xa0', ' ').rstrip())
