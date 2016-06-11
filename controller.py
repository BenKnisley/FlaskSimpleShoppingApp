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

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Generate Html from template and append to response
    html = view.display("Welcome", "./model/textFiles/home.html", cartcount)
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

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Get product object from model
    product = model.getProductByID(productID)

    ## Get html from view and product object
    html = view.product(product, cartcount)

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "product: " + product.name)

    ## Return response
    return response

@app.route('/allproducts')
def allProducts():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Get a list of products
    allProducts = model.getAllProducts()

    ## Send products to productIndex template and get resultent html
    html = view.productIndex("All Products", allProducts, cartcount)

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "All Products")

    ## Return response
    return response

@app.route('/tagged')
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

    ## Get cartCount
    cartcount = model.cartCount(visitID)


    ## Get a list of products
    allProducts = model.getProductsWTag(tag )

    ## Generate html with product list
    html = view.productIndex( ("Products with tag '" + tag + "'"), allProducts, cartcount)

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

    ## Get cartCount
    cartcount = model.cartCount(visitID)


    ## Get a list of products
    products = model.getProductsBySearch(query)


    if len(products) == 0:
        html = view.productIndex( ("No Results Found for: '" + query + "'"), products, cartcount)
    else:
        html = view.productIndex( ("Search results for: '" + query + "'"), products, cartcount)

    ## Send products to productIndex template and get result

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "Search: " + query)

    ## Return response
    return response

@app.route('/cart')
def cart():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Get Items in cart
    products = model.getProductsInCart(visitID)

    ## Compute subtotal, tax, and total
    subtotal = 0
    for product in products:
        subtotal += product.price
    tax = int(0.07 * subtotal)
    total = subtotal + tax

    ## Convert to useful string
    subtotal = ('{:.2f}'.format(subtotal/100.))
    tax = ('{:.2f}'.format(tax/100.))
    total = ('{:.2f}'.format(total/100.))



    ## Send product list to render template
    html = view.cart(products, subtotal, tax, total, cartcount)

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "cart")

    ## Return
    return response

@app.route('/checkout')
def checkout():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Get Items in cart
    products = model.getProductsInCart(visitID)

    ## Send product list to render template
    html = "Hello World"

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "Checkout")

    ## Return
    return response


@app.route('/thanks')
def thanks():
    ## Create new Response
    response = Response()

    ## Process cookie, and get cookied response and visitID
    response, visitID = processCookie(response)

    ## Get cartCount
    cartcount = model.cartCount(visitID)

    ## Get Items in cart
    products = model.getProductsInCart(visitID)

    ## Send product list to render template
    html = "Thanks"

    ## Set response with html
    response.set_data(html)

    ## Register Page Visit
    model.pageVisit(visitID, "Thanks")

    ## Return
    return response

## JavaScript Routes
@app.route('/cartadd', methods=['POST'])
def addToCart():
    ## Get productId from args
    productId = request.form['p']
    visitId = request.form['id']

    print visitId

    ## Confirm that product exists
    if model.productExist(productId):
        ## If so, add to cart, and return 1
        model.addToCart(visitId, productId)
        return "1"
    ## Else return 0
    return "0"


## Run Application
if __name__ == '__main__':
    app.run(debug=True)
