#!/usr/bin/env python
"""
Project: Nimbus Web Simple Shopping Web App
File: Product Class File
Author: Ben Knisley [benknisley@gmail.com]
Date: Mar/27/2016
This file holds a class representing the product in the database.
"""

## Import Json for tag reading
import json

## Define product class
class product:
    def __init__(self, ID, name, desc, price, tagJson):
        ## set product attrubutes from args
        self.ID = ID
        self.name = name
        self.description = desc
        self.price = price
        self.importTags(tagJson)
        print self.tags

    def getPriceStr(self):
        cents = self.price
        if cents > 100:
            return str('{:20,.2f}'.format(cents/100)).strip()
        else:
            if cents > 10:
                return '0.' + str(cents)
            else:
                return '0.0' + str(cents)

    def importTags(self, tagJson):
            self.tags = set()
            tags = json.loads(tagJson)["tags"]
            for tag in tags:
                self.tags.add(tag)
