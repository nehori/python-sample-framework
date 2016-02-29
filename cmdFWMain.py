# -*- coding: utf-8 -*-
#optparse_example.py
from fw import cmdFW

class CmdFWMain():
    def __init__(self, o, a):
         if o.input:
           cmdfw = cmdFW.CmdFW()
           cmdfw.doCmd(o.input)

if __name__ == '__main__':
    import sys
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-i","--input", type="string", dest="input",
                      help="mobule name")
    options, args = parser.parse_args(sys.argv[1:])
    CmdFWMain(options, args)
