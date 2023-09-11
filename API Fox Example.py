# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:34:56 2023

@author: Rudy.Nartker
"""


'''
use :
https://randomfox.ca/?=9

'''

import requests

response = requests.get("https://randomfox.ca/floof", verify=False)
fox = response.json()
print(fox['image'])
