# Best Buy Backend

![Lines of code](https://img.shields.io/tokei/lines/github/varunjha/Best-Buy-Backend?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/varunjha/Best-Buy-Backend)
![Twitter Follow](https://img.shields.io/twitter/follow/varunjha089?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/varunjha/Best-Buy-Backend)
![GitHub top language](https://img.shields.io/github/languages/top/varunjha/Best-Buy-Backend)

This code is the backend portion of a shopping application for college project.

[comment]: <> (## Screenshots)

[comment]: <> (![App Screenshot]&#40;https://via.placeholder.com/468x300?text=App+Screenshot+Here&#41;)

## Tech Stack

**Client:** `React`

**Server:** `Django Rest-API`

**Database:** `PostgreSQL`

**API:** `Django REST framework`

## Requirements

[REST framework](https://www.django-rest-framework.org/) requires the following:

- Python (3.5, 3.6, 3.7, 3.8, 3.9)
- Django (2.2, 3.0, 3.1)

[Django Cors Headers](https://pypi.org/project/django-cors-headers/) is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- 3.8.0 

## Installation

```colsole
ubuntu@ip:~$ git clone https://github.com/varunjha/Best-Buy-Backend.git

(venv) ubuntu@ip:~$ pip install requirements.txt

(venv) ubuntu@ip:~$ python manage.py makemigrations

(venv) ubuntu@ip:~$ python manage.py migrate

(venv) ubuntu@ip:~$ python manage.py runserver
```

## Methods

As we are using **Django Rest-API** to connect between **Frontend** and **Backend**, so several methods which are 
being used as follows:

| Methods | Routes |
|---|---|
| **GET** | **/api/products** |
| **GET** | **/api/products/11** |
| **POST** | **/api/products/create** |
| **PUT** | **/api/products/update/15** |
| **DELETE** | **/api/products/delete/15** |

## Features

- Product
    - 5-Star rating system
    - User can give their feedback

- User Account
    - Authentication
    - Modify Order
    - View Order
    - Create Order
    - Add feedback to product
    - Look for Previous Orders and Re-Order Them

- Admin Account
    - Admin Panel
    - Add Product
    - Update Product Quantity
    - View Orders
    - Send Promotion Message
    - Pin the Feedback

- Shopping Cart

- Search Product

- Payment Integration
    - PayPal
    - Stripe

- Sending **E-Mail**.
    - Confirming Account
    - Order Successful Message
    - Promotion Message

## Command we have used

For **`Back-End`**

```console
(venv) ubuntu@ip:~$ pip install djangorestframework

(venv) ubuntu@ip:~$ pip install markdown                         # Markdown support for the browsable API.

(venv) ubuntu@ip:~$ pip install django-cors-headers

(venv) ubuntu@ip:~$ pip install pillow                           # Image processing library

(venv) ubuntu@ip:~$ 

(venv) ubuntu@ip:~$ 

(venv) ubuntu@ip:~$ 

(venv) ubuntu@ip:~$ 
```

## File Structure

- base
  - urls :- A collection of urls pattern for routing in `base` apps.
  - views :- A collection of views templates which has to be rendered.
  - admin.py :- Database models which has to be registered at admin pannel.
  - apps.py :-
  - models.py :- Database models of `base` apps.
  - serializers.py :-
  - signals.py :-
  - test :-
- BestBuyBackend
  - asgi.py :-
  - settings.py :- Settings related to this projects.
  - urls.py :- Urls routing of this project.
  - wsgi.py :- 
- templates
- .gitignore :- Files to be ignored by git.
- manage.py 
- README.md :- A description of the projects.
- requirements.txt :- Required python modules by this project.

## Important notes about project
- Function based views has been used.

## External Links
- [GitIgnore File](https://github.com/github/gitignore/blob/master/Python.gitignore)

