#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

user_num = int(input())
x = int(input())

print(
    f"{user_num//x} {math.floor(user_num // math.pow(x, 2))} {math.floor(user_num // math.pow(x, 3))}"
)
