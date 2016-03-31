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

## Make path to database global
#! Do best to remove hardcode
SQL_FILE = "/home/ben/Desktop/ProductWebApp/model/database.db"

## Import product class
import product


def productExist(ID):
    return True

def getProductByID(ID): ## Read only
    ## Create database connection and cursor
    conn = sqlite3.connect(SQL_FILE)
    sql = conn.cursor()

    ## Setup query
    query = "SELECT * FROM products WHERE ID='%s';" % (ID)
    ## Send query to database
    sql.execute(query)

    ## Extract all entrys
    rows = sql.fetchall()

    ## Get data from rows
    for row in rows:
        data = row

    ## Create product from data
    retnProduct = product.product(data[0], data[1], data[2], data[3])

    ## Return dummy product
    return retnProduct
