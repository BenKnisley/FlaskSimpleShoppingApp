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
    """
    Defines a products entry in the the database. Holds the direct data, and
        functions to process data.
    """
    def __init__(self, ID, name, desc, price, tagJson):
        ## set product attrubutes from arguments
        self.ID = ID
        self.name = name
        self.description = desc
        self.price = price
        self._importTags(tagJson)

    def getPriceStr(self):
        """
        Converts self.price from int to a string in the 0.00 format of currency.
        """
        cents = self.price
        if cents > 100:
            return str('{:20,.2f}'.format(cents/100)).strip()
        else:
            if cents > 10:
                return '0.' + str(cents)
            else:
                return '0.0' + str(cents)

    def _importTags(self, tagJson):
        """
        Parses the tags into a set from json format stored in the database.
            Creates self.tags.
        """
        ## Create return set
        self.tags = set()

        ## Gets tags from json in list format
        tags = json.loads(tagJson)["tags"]

        ## Convert list to set
        for tag in tags:
            self.tags.add(tag)
