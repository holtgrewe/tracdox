#!/usr/bin/env python

from __future__ import print_function

import re
import sys

def sub1(m):
  hit = m.group(1).replace(r'\_', '_')
  path = hit[len('source:trunk/'):]
  path = path[:path.find(',')]
  frag = hit[hit.find('fragment='):-1]
  frag = frag[len('fragment='):]
  result = ['.. includefrags:: %s' % path,
            '   :fragment: %s' % frag,
            '']
  return '\n'.join(result)

def sub2(m):
  indent = m.group(1)
  tokens = m.group(2).split(', fragment=')
  result = [indent + '.. includefrags:: %s' % tokens[0],
            indent + '   :fragment: %s' % tokens[1],
            '']
  return '\n'.join(result)

text = sys.stdin.read()
text = re.sub(r'`Include\((.*?\)).*?__\n', sub1, text, flags=re.DOTALL).rstrip()
text = re.sub(r'( *)\[\[Include\(source:(.*?)\)\]\]', sub2, text, flags=re.DOTALL).rstrip()
print(text)
