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
import datetime

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
    visitID = request.cookies.get('visit')
    if visitID == None:
        ## Get IP Address of user
        ipAddr = request.remote_addr

        ## If new user, add entry in database and get visitID
        visitID = model.newVisitor(ipAddr)

        ## Set response with new visit cookie
        response.set_cookie('visit', visitID, expires = (datetime.datetime.now() + datetime.timedelta(days=14)))

    ## Return response and visitID
    return response, visitID

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

    ## Register Page Visit
    model.pageVisit(visitID, "Home")

    ## Return
    return response

## The Product route
@app.route('/product/<productID>')
def product(productID):
    ## If product doesnt exists, display error page
    if not model.productExist(productID):
        abort(404)

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

    ## Register Page Visit
    model.pageVisit(visitID, "product: " + product.name)

    ## Return response
    return response

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

    ## Register Page Visit
    model.pageVisit(visitID, "All Products")

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

    ## Register Page Visit
    model.pageVisit(visitID, "Tagged: " + tag)

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


    if len(products) == 0:
        html = view.productIndex( ("No Results Found for: '" + query + "'"), products)
    else:
        html = view.productIndex( ("Search results for: '" + query + "'"), products)

    ## Send products to productIndex template and get result

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "Search: " + query)

    ## Return response
    return response

@app.route('/x')
def test():
    return "<form action='/cartadd' method='post'><input name='p'></input></form>"


## JavaScript Routes
@app.route('/cartadd', methods=['POST'])
def addToCart():
    ## Get productId from args
    productId = request.form['p']

    ## Confirm that product exists
    if model.productExist(productId):
        ## If so, add to cart, and return 1
        model.addToCart(productId)
        return "1"
    ## Else return 0
    return "0"


## Run Application
if __name__ == '__main__':
    app.run(debug=True)
