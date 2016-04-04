#!/usr/bin/env python
"""
Project: Nimbus Web Simple Shopping Web App
File: Application Controller
Author: Ben Knisley [benknisley@gmail.com]
Date: Mar/26/2016
This file holds the controller for the entire application. It takes requests,
querys the model, and sends data to the view.
"""

## Import Flask modules
from flask import Flask, render_template, abort

## Import app modules
import model, view

## Create Flask application object
app = Flask(__name__)

## Set app varibles
app.config['template_folder'] = '/templates'

## The home route
@app.route('/')
def index():
    return view.display("Yolo", "/home/ben/Desktop/yolo")

## The Product route
@app.route('/product/<productID>')
def product(productID):
    if model.productExist(productID):
        product = model.getProductByID(productID)
        return view.product(product)
    else:
        abort(404)

@app.route('/test')
def test():
    x = model.getAllProducts()
    string = ""
    for y in x:
        string += y.name
        string += "<br>"
    return string

## Run Application
if __name__ == '__main__':
    app.run(debug=True)
