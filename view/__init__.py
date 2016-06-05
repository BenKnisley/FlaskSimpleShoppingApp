#!/usr/bin/env python
"""
Project: Nimbus Web Simple Shopping Web App
File: View Module Index
Author: Ben Knisley [benknisley@gmail.com]
Date: Mar/26/2016
This file holds and controls all functions and objects related to the view. For
    example it holds the functions display(), index(), and product(). Each
    function holds the business logic for rendering each class of pages.
    Display for
"""
from flask import render_template

def display(title, file, cartcount):
    """
    This is the render function for the display set of pages (home, legal, contact, etc).
        It is the simplest, it is handed a page title and a html file path and it passes
        them to the display template, and returns the result.
    """
    ## Extract html out of given file
    html = open(file, 'r').read()

    ## Pass html to display template and update it to the rendered content.
    html = render_template("display.html", title=title, content=html, cartcount=cartcount)

    ## Return
    return html


def product(product, cartcount):
    """
    This is the render function for the product page.
        This function takes a product object, feeds it to the product template,
        and returns the result.
    """
    ## Route given product object to product template
    html = render_template("product.html", product=product, cartcount=cartcount)

    ## Returns result
    return html


def productIndex(title, products, cartcount):
    """
    """
    ## Route given title and products list to productIndex template
    html = render_template("productIndex.html", title=title, products=products, cartcount=cartcount)

    ## Returns result
    return html
