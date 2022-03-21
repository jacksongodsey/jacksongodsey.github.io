#!/usr/bin/env python
# -*- coding: utf-8 -*-
minutes = int(input("Enter minutes:\n"))
hours = float(input("Enter hours:\n"))
hours_remainder = hours % 1
hours = hours // hours
minutes_total = (hours * 60) + (hours_remainder * 60) + minutes
print(hours, hours_remainder, minutes, minutes_total)
print(f"{hours:.2f} and {minutes} means there is {minutes_total} minutes")
