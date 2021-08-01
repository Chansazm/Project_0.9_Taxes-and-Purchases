#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:24:31 2019

@author: chansa
"""


def taxes(purchase_Amount):
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    for state in states:

        if state == input("Please enter State"):
            tax = 0.075
            total_Cost = purchase_Amount * (1 + tax)
            result = "Since you are from {}, your Total cost is: {} ".format(
                state, total_Cost)
        elif state == 'MN':
            tax = 0.095
            total_Cost = purchase_Amount * (1 + tax)
        elif state == 'NY':
            tax = 0.089
            total_Cost = purchase_Amount * (1 + tax)
        else:
            tax = 'invalid'


print(taxes(10))
