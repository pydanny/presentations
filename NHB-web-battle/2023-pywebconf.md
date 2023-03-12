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

# Quick review of my Python web work

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

[.background-color: #ecd540]

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

Flask :+1: :+1:

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

FastAPI :+1: :+1:

- Light and easy to get started
- One file apps are easy to build
- Flexibility on persistence is a virtue
- Built-in validation
- Built-in REST API is awesome

[.column]

Flask :+1:

- Light and easy to get started
- One file apps are easy to build
- Flexibility on persistence is a virtue

[.column]

Django :+1: :-1:

- Admin tool is great for small projects with SQL persistence
- Overkill for projects without SQL persistence
- Single file apps require advanced knowledge of Django

---

[.background-color: #00FF00]

# Developer Experience

## Small projects

# [fit] Winner: FastAPI

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

[.column]

FastAPI :+1: :-1:

- No guidance provided
- Framework design encourages separation of concerns

---

[.background-color: #00FF00]

# Developer Experience

## Large projects

# [fit] Winner: Django

---

# TODO: Table with summaries

---

[.background-color: #00FF00]

# Developer Experience

## Composite

# [fit] Winner: FastAPI

---

[.background-color: #ecd540]

# [fit] Performance

---

# About performance metrics

- Often the database is the bottleneck real projects face
- Indexing and caching are often the best ways to improve performance rather than changing the framework

---

# "Lies, Damn Lies and Statistics"

So many variables that it's easy to get lost in the weeds.

1. FastAPI is really fast with JSON serialization
2. Flask tends to have better composite scores
3. Django run as a single file app without middleware, context processors, etc is comparable to Flask and FastAPI

---

# Performance Summary

Source: [techempower.com/benchmarks/](https://www.techempower.com/benchmarks/)

1. Flask or FastAPI depending on the conditions :+1:
2. Django :-1:

---

[.background-color: #00FF00]

# Performance

# [fit] Winner: Flask & FastAPI

---

[.background-color: #ecd540]

# [fit] Async Support

---

# Async Support

## Why it matters

- Websockets
- Blocking I/O
  - File streaming
  - Slow APIs
  - Tarpits

---

# Async Support

[.column]

FastAPI :+1:

- Designed from the outset to support async
- All of the framework is async by default
- [Good documentation](https://fastapi.tiangolo.com/async/)

[.column]

Flask :+1: :-1:

- Slow, hence [recommendation](https://flask.palletsprojects.com/en/2.2.x/async-await/#when-to-use-quart-instead) to use Quart instead
- Modern Flask supports async
- [Light documentation](https://flask.palletsprojects.com/en/2.2.x/async-await/)
- Much of Flask and ecosystem is synchronous

[.column]

Django :+1: :-1:

- Herculean effort to bring async support to Django
- Not for beginners
- [Docs](https://docs.djangoproject.com/en/4.2/topics/async/) cover the fundamanetals, but not much else
- Nifty `sync_to_async()` decorator
- Much of ecosystem is synchronous

---

[.background-color: #00FF00]

# Async

# [fit] Winner: FastAPI

---

[.background-color: #ecd540]

# [fit] Persistence

---

# Persistence engines I like to use

- Relational Databases (SQL for short)
- DynamoDB, specifically single-table designs
- Firebase, especially in hackathons

---

# Persistence

[.column]

FastAPI :+1:

- Use whatever you want

[.column]

Flask :+1:

- Use whatever you want

[.column]

Django :+1:

- Designed for SQL databases
- Key/value stores used for caching
- Universality of SQL empowers the package ecosystem
- [Using No-SQL is always a mistake](https://daniel.feldroy.com/posts/when-to-use-mongodb-with-django)

---

[.background-color: #00FF00]

# Persistence

# [fit] Winner: ???

---

[.background-color: #ecd540]

# [fit] Sweet Spots

---

# Sweet Spots

[.column]

FastAPI :+1: :+1:

- REST/JSON APIs
- Small projects
- Async
- Elegant design

[.column]

Flask

- Small projects

[.column]

Django :+1:

- Large projects
- Third-party packages
- Django Templates + HTMX

---

[.background-color: #00FF00]

# Sweet Spots

# [fit] Winner: FastAPI

---

[.background-color: #ecd540]

# [fit] Conclusion

# (what do I use on new projects?)

---

# Django or FastAPI or Flask?

---

# FastAPI

- Sweet design that's fun to use
- Async support from the beginning
- Persistence is up to you
- Small projects
- I have the architecture experience to use it on large projects

---

[.background-color: #00FF00]

# Grand Winner

# [fit] Winner: FastAPI

---

[.background-color: #00FF00]

# [fit] Join me in the good fight against climate change

[.column]

<br>

Octopus Energy Group is hiring

[octopus.energy/careers](https://octopus.energy/careers/join-us/#/)

[.column]

![inline](assets/super_octo.png)

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]
[.text: #FFFFFF, Avenir Next Bold]

# [fit] Octopus doesn't work for you?

- Wrong country
- Wrong skills
- Don't like eight legged mascots

---

[.background-color: #ecd540]

# [fit] That's Okay

---

[.background-color: #00FF00]

# [fit] Work for the competition

## Doesn't matter which green firm "wins"

# [climatebase.org](https://climatebase.org/)

---

# About Me

[.column]

Daniel Roy Greenfeld

Code @ Kraken Technologies

Author, Coder, Leader

Husband of Audrey Roy Greenfeld

Father

Superhero saving the planet

[.column]

![fit](assets/facebook-avatar.jpg)
