#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

base = float(input("Enter initial savings: "))
print()

rate = float(input("Enter annual interest % rate: "))
print()

years = int(input("Enter years that pass: "))
print()

total = base * math.pow(1 + (rate / 100), years)

# Years becomes the exponent after 1 + (rate / 100) is executed

print("Savings after", years, "years is", total)
