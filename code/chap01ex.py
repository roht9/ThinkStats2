"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def main(script):
    print "exercise 1-2 pregnumの頻度分布"
    df = nsfg.ReadFemPreg()
    temp = df.pregnum.value_counts().sort_index()
    for i in range(0,len(temp.values)):
        print( "%d:%s" % (i + 1, (temp.values[i] / temp.axes[0][i])))

    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)


