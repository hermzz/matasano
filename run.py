#!/bin/env python

import sys

if len(sys.argv) != 3:
    print("Incorrect number of arguments")
    sys.exit(1)

set = sys.argv[1]
step = sys.argv[2]

excercise = getattr(__import__("set%s.e%s" % (set, step)), "e%s" % step)
excercise.run()