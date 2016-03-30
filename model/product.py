#!/usr/bin/env python
"""
Project: Nimbus Web Simple Shopping Web App
File: Product Class File
Author: Ben Knisley [benknisley@gmail.com]
Date: Mar/27/2016
This file holds a class representing the product in the database.
"""

## Define product class
class product:
    ## product constructor
    def __init__(self, ID, name, desc, price ):
        ## set product attrubutes from args
        self.ID = ID
        self.name = name
        self.description = desc
        self.price = price
