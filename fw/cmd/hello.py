#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fw.cmd.abstractCmd import AbstractCmd
import subprocess

class Hello(AbstractCmd):
    def execute(self):
        print("Hello")

    def result():
        pass
