#!/usr/bin/env python                                                                                                                                                                                                                                                                                                                       

import sys

for e in (l.split() for l in sys.stdin.readlines() if l.strip()):
    sys.stdout.write(">%s\n%s\n" % (e[0], ''.join(e[1:])))
