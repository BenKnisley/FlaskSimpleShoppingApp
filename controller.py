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
from flask import Flask, render_template, abort, request, make_response, Response

## Import app modules
import model, view

## Create Flask application object
app = Flask(__name__)

## Set app varibles
app.config['template_folder'] = '/templates'


## Cookie function
def processCookie(response):
    """
    Processes the request, if request doesnt have a visit cookie, creates a new
        one. Function returns the request with a cookie, and the visit id.
    """
    visitCookie = request.cookies.get('visit')
    if visitCookie == None:
        newVisitID = model.newVisitor()
        print  "***" + request.remote_addr
        response.set_cookie('visit', newVisitID)
    return response, visitCookie

############
#$ Routes $#
############

## The home route
@app.route('/')
def index():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Generate Html from template and append to response
    html = view.display("Welcome", "./model/textFiles/home.html")
    response.set_data(html)

    ## Return
    return response

## The Product route
@app.route('/product/<productID>')
def product(productID):
    ## If product exists, display product page
    if model.productExist(productID):

        ## Create new Response
        response = Response()

        ## Process cookie, and get cookied response and visitID
        response, visitID = processCookie(response)

        ## Get product object from model
        product = model.getProductByID(productID)

        ## Get html from view and product object
        html = view.product(product)

        ## Set response with html
        response.set_data(html)

        ## Return response
        return response

    ## If product does not exist, 404
    else:
        abort(404)

@app.route('/test_allproducts')
def allProducts():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get a list of products
    allProducts = model.getAllProducts()

    ## Send products to productIndex template and get resultent html
    html = view.productIndex("All Products", allProducts)

    ## Set response with html
    response.set_data(html)

    ## Return response
    return response

@app.route('/test_taggedproducts')
def taggedProducts():

    ## Get tag
    tag = request.args.get('tag')

    ## If empty, call 404
    if tag == None:
        abort(404)

    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get a list of products
    allProducts = model.getProductsWTag(tag )

    ## Generate html with product list
    html = view.productIndex( ("Products with tag '" + tag + "'"), allProducts)

    ## Set response with html
    response.set_data(html)

    return response

@app.route('/search')
def searchProducts():
    ## Get query
    query = request.args.get('q')

    ## If empty, call 404
    if query == None:
        abort(404)

    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get a list of products
    products = model.getProductsBySearch(query)

    ## Send products to productIndex template and get result
    html = view.productIndex( ("Search results for: '" + query + "'"), products)

    ## Set response with html
    response.set_data(html)

    ## Return response
    return response


## Run Application
if __name__ == '__main__':
    app.run(debug=True)
