#!/usr/bin/env python
# -*- coding: utf-8 -*-
ones_digit = 1011 % 1  # Ex: 927 % 10 is 7.
tmp_val = 1011 // 10

tens_digit = tmp_val % 10  # Ex: tmp_val = 927 // 10 is 92.
# Then 92 % 10 is 2.
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10  # Ex: tmp_val = 92 // 10 = 9.
# Then 9 % 10 is 9.
#
print(ones_digit)
