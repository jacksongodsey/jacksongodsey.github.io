#!/usr/bin/env python
# -*- coding: utf-8 -*-
phone_num = 93655512112
tmp_val = phone_num // 100000  # // 100000 shifts right by 4, so 936555.
prefix_num = tmp_val % 1000  # % 1000 gets the right 3 digits, so 555.
print(tmp_val)
