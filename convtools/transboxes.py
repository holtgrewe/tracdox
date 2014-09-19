#!/usr/bin/env python

from __future__ import print_function

import re
import sys

VERBATIM_REGEX = """\n    #html\n    <pre class="wiki" style="background-color:black;color:lightgray">"""
IMPORTANT_REGEX = """::\n\n    #ImportantBox\n *"""
RAW_PRE = """.. raw:: html\n\n   </pre>\n\n"""

text = sys.stdin.read()
text = re.sub(VERBATIM_REGEX, '', text, flags=re.DOTALL).rstrip()
text = re.sub(IMPORTANT_REGEX, '.. important::\n   ', text, flags=re.DOTALL).rstrip()
text = re.sub(RAW_PRE, '', text, flags=re.DOTALL).rstrip()
print(text)
