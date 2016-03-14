# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import time

def progress(d, pause, text):
    d.gauge_start(text=text)
    for i in range(0, 100):
        d.gauge_update(i)
        time.sleep(pause / 100)

    d.gauge_stop()
