# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.rest.fmfwio import fmfwio


class bitcoincom(fmfwio):

    def describe(self):
        return self.deep_extend(super(bitcoincom, self).describe(), {
            'id': 'bitcoincom',
        })
