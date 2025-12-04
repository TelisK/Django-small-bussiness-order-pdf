# Django text to PDF Generator
This is my project while i am learning Django + HTML. 

This app allows users to do enter order details and product, and generate a PDF ready to print

The user has access to history, ordered by date, also can read, reprint or delete the entry from the database

Suitable for small bussinesses, where they can make a simple pdf through text

## Features
* Enter customer, supplier, products and notes into a web form

* Generate PDF by pressing Submit

* Save entries to database

* History page showing all past entries

* On history page, user can :

    * View details

    * Re-print (generate PDF again)

    * Delete entries

## Technologies
* Django

* HTML/CSS(bootstrap)

* xhtml2pdf

## How it works
* User fills out the form
* When the user presses Submit, a new download starts with the pdf file. At the same time the data are saved on a database
* User can see all the orders he made
* User can see, re-print, or delete the entry

