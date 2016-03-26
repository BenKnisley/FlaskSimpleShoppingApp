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


def display(file):
    """
    This is the render function for the display set of pages (home, legal,
        contact, etc). It is the simplest, it is handed an html file path and it
        passes the contents to the display template, and returns the result.
    """
    ## Extract html out of given file
    html = open(file, 'r').read()

    ## Pass html to display template and update it to the rendered content.
    html = render_template("display.html", content=html)

    ## Return
    return html
