#!/usr/bin/env python                                                                                                                                                                                                                                                                                                                       

import sys

for c in zip(*(l.split() for l in sys.stdin.readlines() if l.strip())):
    sys.stdout.write("%s\n" % ('\t'.join(c)))
