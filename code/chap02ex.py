"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """

    max_key = None
    max_value = -1
    for k, v in thinkstats2.Hist.Items(hist) :
        if v > max_value :
            max_key = k
            max_value = v
        
    return max_key


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    list = []

    for k in  sorted(hist.Values(),key=lambda v: thinkstats2.Hist.Freq(hist, v), reverse=True) :
        # print("key")
        # print(k)
        # print("val")
        # print(thinkstats2.Hist.Freq(hist,k))
        list.append([k, thinkstats2.Hist.Freq(hist, k)])
    return list


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
