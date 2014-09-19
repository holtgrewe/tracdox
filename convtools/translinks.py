#!/usr/bin/env python

from __future__ import print_function

import re
import sys

def sub(m):
  link = m.group(0)[5:-1]
  tokens = link.split()
  # Remove duplication in [dox:Foo Foo].
  if len(tokens) == 2 and tokens[0] == tokens[1]:
    href = tokens[0]
  else:
    href = ' '.join(tokens)
  result = ':dox:`%s`' % href
  #print(link, result, file=sys.stderr)
  return result

for line in sys.stdin:
  print(re.sub(r'\[dox:[^\]]+\]', sub, line, flags=re.DOTALL).rstrip())
