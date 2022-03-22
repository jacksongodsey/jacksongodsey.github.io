#!/usr/bin/env python
# -*- coding: utf-8 -*-

integer_input = int(input("Enter integer (32 - 126):\n"))
float_input = float(input("Enter float:\n"))
character_input = input("Enter character:\n")
string_input = input("Enter string:\n")

print(f"{integer_input} {float_input} {character_input} {string_input}")
print(f"{string_input} {character_input} {float_input} {integer_input}")
print(f"{integer_input} converted to a character is {chr(integer_input)}")
