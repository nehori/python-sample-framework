#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractCmd(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def result():
        pass
