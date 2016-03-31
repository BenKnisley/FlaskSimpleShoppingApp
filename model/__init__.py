#!/usr/bin/env python
"""
Project: Nimbus Web Simple Shopping Web App
File: Model Module Index
Author: Ben Knisley [benknisley@gmail.com]
Date: Mar/26/2016
This file holds and controls all functions and objects related to the model.
    Meaning it holds functions that deal with the database and any output actions.
    For example it holds the functions getProductByID(), sessionExist(), etc.
    This file should be writen so that the database backend can be switch quickly.
"""
## Import sqlite
import sqlite3

## Import product class
import product


def productExist(ID):
    return True

def getProductByID(ID):
    ## Return dummy product
    return product.product("PRODUCT_4411", "Apple", "A big red fruit.", 75)
