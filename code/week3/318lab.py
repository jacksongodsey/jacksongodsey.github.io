#!/usr/bin/env python
# -*- coding: utf-8 -*-

lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
serving_size = float(input("How many servings does this make?\n"))
print()

print(f"Lemonade ingredients - yields {serving_size:.2f} servings")
print(f"{lemon_juice:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar")
print()


desired_servings = float(input("How many servings would you like to make?\n"))
print()
print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{(lemon_juice * (desired_servings / serving_size)):.2f} cup(s) lemon \
juice")
print(f"{(water * (desired_servings / serving_size)):.2f} cup(s) water")
print(f"{(agave_nectar * (desired_servings / serving_size)):.2f} cup(s) agave \
nectar")
print()

print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{((lemon_juice * (desired_servings / serving_size)) / 16):.2f} gallon(s) \
lemon juice")
print(f"{((water * (desired_servings / serving_size))/ 16):.2f} gallon(s) \
water")
print(f"{((agave_nectar * (desired_servings / serving_size)) / 16):.2f} \
gallon(s) agave nectar")
