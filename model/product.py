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
    Defines a class for the products entry in the the database. Holds the direct
    data, and functions to process data.
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
        Returns the price (self.price stored as an int) as string in the 0.00
            format
        """
        ## Put the price value into new var
        cents = self.price

        ## If the value above dollar
        if cents > 100:
            ## Return string with format <dollar>.<cents w/ 2 dec points>
            return str('{:20,.2f}'.format(cents/100)).strip()

        ## If price below a dollar
        else:
            ## If larger than 10 cents
            if cents > 10:
                ## Add 0. in front on cents
                return '0.' + str(cents)

            ## If less than a dollar
            else:
                ## Add a 0.0 in front of cents
                return '0.0' + str(cents)

    def _importTags(self, tagJson):
        """
        Parses the tags into a set from json format stored in the database.
            - Creates self.tags (no need to capture return)
        """
        ## Create return set
        self.tags = set()

        ## Gets tags from json in list format
        tags = json.loads(tagJson)["tags"]

        ## Convert list to set
        for tag in tags:
            self.tags.add(tag)
