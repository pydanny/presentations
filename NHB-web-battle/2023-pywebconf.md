footer: @pydanny / Kraken Technology :octopus:
slidenumbers: true
autoscale: true
slide-transition: true

# [fit] No Holds Barred

# [fit] Web Framework Battle

## Daniel Roy Greenfeld

---

# [fit] No Holds Barred

# [fit] Web Framework Battle

## Daniel Roy Greenfeld

---

# [fit] Hello Python Web Conf!

![inline](https://2023.pythonwebconf.com/python-web-conference-2023/@@images/logo_image)

---

# [fit] About this talk

- Compare some Python web frameworks
- Compare them in ways that make sense for me
- My preferences may not be your preferences

---

# [fit] Addressing the question of

# [fit] Bias

---

# [fit] Many people think of me as

# [fit] "Django Daniel"

---

# Quick Comparison of my Python Web work

[.column]

# Django

- 5 editions of Two Scoops of Django
- 1 edition of Django Crash Course
- 233 articles: [daniel.feldroy.com/tags/django](https://daniel.feldroy.com/tags/django)
- Countless open source contributions
- Oodles of production projects

[.column]

## FastAPI / Flask / Pyramid

- 3 FastAPI Articles: [daniel.feldroy.com/tags/fastapi](https://daniel.feldroy.com/tags/fastapi)
- 5 Flask Articles: [https://daniel.feldroy.com/tags/flask](daniel.feldroy.com/tags/flask)
- 8 Flask Articles: [https://daniel.feldroy.com/tags/pyramid](daniel.feldroy.com/tags/pyramid)
- About 15 production projects

[.column]

# Zope/Plone

- 2 production projects
- 74 Plone articles: [daniel.feldroy.com/tags/plone](https://daniel.feldroy.com/tags/plone)
- 38 Zope articles: [daniel.feldroy.com/tags/zope](https://daniel.feldroy.com/tags/zope)

---

# [fit] I tend to write more about

# [fit] what I'm being paid to work on

---

# Yes, I've written a lot about Django

- After 14 years I know the pain points of Django
- I know more about the virtues of competitors than flaws

---

# [fit] My nickname is

# [fit] "pydanny"

# [fit] Not "Django Daniel"

---

# [fit] Ready?

# Let's dive in

---

# [fit] Quick Framework Overview

- Django
- FastAPI
- Flask
- Pyramid
- Tornado

---

# Django

- Released: 2005
- Full-stack web framework
  - Web-serving, databases, HTML generation
- Bundled with ORM & form validation
- Admin tool driven by ORM & form systems
- Evolving toward Async
- Sweet spots: HTML sites with SQL backend, package ecosystem, popularity

---

# FastAPI

- Released: 2018
- Almost Microframework
  - Data validation: tightly integrated with pydantic
- Uses type annotations as a superpower
- Async from the start
- Sweet spots: REST/JSON APIs, speed, popularity

---

# Flask

- Released: April 1, 2010
- Microframework
  - Minimal core, lots of extensions
- Very popular with vendors for tutorials
- Async, speed it up by using Quart
- Sweet spots: Simplicity, flexibility, popularity

---

# Pyramid

- Released: 2008
- Microframework
  - Minimal core, lots of extensions
- No globals means no magic
- Sweet spots: Flexibility, explicitness

---

# Tornado

- Released: 2009
- Microframework
- Async from the start
- Backbone of Jupyter notebook
- Sweet spots: Speed, async, backbone of Juptyer notebook

---

[.background-color: #ecd540]

# [fit] Comparing the Big Three

- Django
- FastAPI
- Flask

Popularity and usage is at least an order of magnitude higher than other python frameworks.

---

# [fit] Points of Comparison

[.column]

- Developer experience
- Performance
- Async support

[.column]

- Persistence
- Sweet spots

---

# [fit] Developer Experience

- How easy is it to get started?
- Data validation
- Small projects
- large projects

---

# Developer Experience

## How easy is it to get started?

[.column]

Flask is easy :+1:

```python
# app.py
# Flask can also return JSON by returning dict
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

[.column]

FastAPI is easy :+1:

```python
# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Index": "Page"}

@app.get("/hello")
def hello():
    return {"Hello": "World"}
```

[.column]

Django is harder :-1:

```python
# urls.py
# Not including a bunch of setup
# Also, no one builds Django projects this way
from django.urls import path
from django.views.generic import View

def index(request):
    return "Index Page"

def hello(request):
    return "Hello, World"

urlpatterns = [
    path('', index, name='home'),
    path('/hello', hello, name='home'),
]
```

---

# Developer Experience:

## How easy is it to get started?

[.column]

Flask :+1:

- Easy to get started
- Flask's [quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/) is amazing
- Quickstart covers everything many small projects need

[.column]

FastAPI :+1:

- Easy to get started
- [Quickstart](https://fastapi.tiangolo.com/tutorial/first-steps/) focuses on features

[.column]

Django :-1:

- No such thing as a quickstart in Django
- Tutorial is good, just takes time

---

[.background-color: #00FF00]

# Developer Experience:

## How easy is it to get started?

# [fit] Winner: Flask

---

# Developer Experience

## Incoming data validation

[.column]

FastAPI :+1: :+1:

- Comes with built-in validation
- Powered by the pydantic library, which is awesome
- Type annotations makes it intuitive
- Forces use of validation

[.column]

Django :+1:

- Comes with built-in validation
- Powered by Django's Forms and ORM
- Edge cases require digging
- Encouraged, but not forced

[.column]

Flask :-1:

- No built-in validation
- Documentation doesn't encourage data validation
- flask-wtf is awesome, but no mention in core docs

---

[.background-color: #00FF00]

# Developer Experience

## Data Validation

# [fit] Winner: FastAPI

---

# Developer Experience

## Small projects

[.column]

Flask and FastPI :+1:

- Light and easy to get started
- One file apps are easy to build
- Flexibility on persistence is a virtue

[.column]

Django :+1: :-1:

- Admin tool is great for small projects with SQL persistence
- Overkill for projects without SQL persistence

---

[.background-color: #00FF00]

# Developer Experience

## Small projects

# [fit] Winner: FastAPI & Flask

---

# Developer Experience

## Large projects

[.column]

Django :+1: :+1:

- "app" structure forced by Framework
- Described in core tutorial
- Each app supports a specific feature
- Each app has its own models, views, forms, etc.
- Borrowed from POSIX philosophy

[.column]

Flask :+1:

- Core docs
- Each blueprint supports a specific feature
- Each blueprint has its own models, views, forms, etc.
- In my experience, rarely used

[.column] :+1: :-1:

FastAPI

- No guidance provided
- Framework design encourages separation of concerns

---

[.background-color: #00FF00]

# Developer Experience

## Large projects

# [fit] Winner: Django

---

# Developer Experience
