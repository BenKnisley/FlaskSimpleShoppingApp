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
SQL_FILE = "./model/database.db"

## Import product class
import product

### PRODUCT FUNCTIONS ###

def productExist(ID): ## Read Only
    ## Create database connection and cursor
    conn = sqlite3.connect(SQL_FILE)
    sql = conn.cursor()

    ## Setup query
    query = "SELECT EXISTS(SELECT 1 FROM products WHERE ID='%s');" % (ID)
    ## Send query to database
    sql.execute(query)

    ## Extract and return data
    if sql.fetchone()[0] == 1:
        return True
    else:
        return False

def getAllProducts():
    ## Create database connection and cursor
    conn = sqlite3.connect(SQL_FILE)
    sql = conn.cursor()

    ## Setup query
    query = "SELECT * FROM products;"
    ## Send query to database
    sql.execute(query)

    ## Get data from query
    entrys = sql.fetchall()

    ## Create return list
    retn = list()

    ## For each entry create product from data
    for data in entrys:
        retn.append( product.product(data[0], data[1], data[2], data[3], data[4]) )

    ## Return ste of products
    return retn

def getProductsWTag(tag):
    ## Call getAllProducts to get all products
    allProducts = getAllProducts()

    ## Create new list for tagged products
    taggedProducts = list()

    ## For each product if tag is in product.tags, add to taggedProducts
    for product in allProducts:
        if tag in product.tags:
            taggedProducts.append(product)

    ## Return taggedProducts
    return taggedProducts

def getProductsBySearch(query):
        ## Break down query into words
        queryList = query.split()

        ## Call getAllProducts to get all products
        allProducts = getAllProducts()

        ## Create list of results
        results = list()

        ## For each product
        for product in allProducts:
            ## For each word in queryList
            for word in queryList:
                ## If word is contained in name, add to results
                if (word in product.name):
                    results.append(product)
                ## If word is contained in description, add to results
                if (word in product.description):
                    results.append(product)
                ## If word is contained in tags, add to results
                if (word in product.tags):
                    results.append(product)

        ## Remove duplicates from results
        results = list(set(results))

        ## return results
        return results

def getProductByID(ID): ## Read only
    ## Create database connection and cursor
    conn = sqlite3.connect(SQL_FILE)
    sql = conn.cursor()

    ## Setup query
    query = "SELECT * FROM products WHERE ID='%s';" % (ID)
    ## Send query to database
    sql.execute(query)

    ## Get data from query
    data = sql.fetchone()

    ## Create product from data
    retnProduct = product.product(data[0], data[1], data[2], data[3], data[4])

    ## Return product
    return retnProduct


### VISITOR FUNCTIONS ###
