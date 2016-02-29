#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fw.cmd import abstractCmd as abst
from fw.cmd import hello
from fw.cmd import hoge

plugin_options = {
   'Hello'   : hello.Hello,
   'Hoge' : hoge.Hoge,
}

class CmdFW():
    def __init__(self):
       pass

    def doCmd(self, cmd):
       var = plugin_options[cmd]
       c = var()
       print(c.__class__.__name__, end=": ")
       if not isinstance(c, abst.AbstractCmd):
           print(cmd + " is not an instance.")
           return
       c.execute()
