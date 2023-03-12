footer: @pydanny / Octopus Energy :octopus:
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

- I'm going to compare some Python web frameworks
- I'm going to compare them in ways that make sense for me
- My preferences may not be your preferences

---

# What frameworks I'm covering

- Django
- FastAPI
- Flask/Quart

# [fit] The "big three"

---

# [fit] But first...

---

# What frameworks I'm not covering

- Tornado
- Pyramid
- Framework X

---

# Why not Tornado?

- Async from before asyncio
- Backbone of Jupyter projects

## But...

- Very limited usage compared to the "big three"

---

# Why not Pyramid?

- More explicit than Flask
- Some interesting ideas

## But...

- Very limited usage compared to the "big three"

---

# Why not Framework X?

- "It's my favorite framework!!!!"

## But...

- Very limited usage compared to the "big three"

---

# [fit] Back to the Big Three...

---

# [fit] The Big Three

# Django

# FastAPI

# Flask/Quart

---

# [fit] The elephant in the room

---

# [fit] My bias

# [fit] Is not what you expect

---

# [fit] Yes, I've written a lot about

# [fit] Django

---

# [fit] ...but I'm pydanny

# [fit] Not "Django Danny"

---

# [fit] I've used all three frameworks

# [fit] in production

---

# [fit] I like all three frameworks

---

# [fit] I know enough about

# [fit] Django

# [fit] to explain what I don't like about it

---

# [fit] Ready?

Let's do it!

---

# Popular comparisons

- Ease of use
- Performance
- Security
- Community
- Documentation
- Ecosystem
- Features
- Code quality
- Deployment
- Jobs

---

# [fit] Things I really care about

- Explicitness
- Type hints as a superpower
- Gaurdrails
- Developer experience
- Async support
- Sweet spots (where a framework excels)

---

# [fit] Framework sweet spots

- Django for projects that don't need an API (views with templates)
- FastAPI for anything that needs an API
- Flask for quick-and-dirty projects

---

# What I hate about Django

- Sucks for API building

  - DRF is hard
  - Graphene isn't any better
  - django-ninja is a bit better

- Sucks for async

  - django-channels is amazing
  - But using it isn't easy
  - async django is a miracle of engineering, but it's not easy to use

---

# What I hate about Flask

- Fastest to get started

  - Who needs a request parameter anyway?

- No gaurdrails

  - No type hints

- Sucks for API building

  - Flask-RESTful is hard
  - Flask-GraphQL is hard
  - Flask-apispec is hard

- Implicitness

  - requests
  - global object

---

# What I hate about FastAPI

---

# [fit] Performance

(although I don't care much about this)

- FastAPI wins the game of metrics
- Flask is fast too
- Django is slow (but runs fast as a single-module app w/no middleware)

---

# [fit] Data validation

- Django forms/ORM
- FastAPI built-in plus pydantic
- Flask - whatever you want

---

# [fit] Async

- Django - channels
- FastAPI - async
- Flask/Quart

---

# Documentation

- Django and FastAPI are awesome
- Flask is subjective

---

# [fit] API Documentation

- Django via DRF / Django-Ninja
- FastAPI
- Flask via Flask-apispec

---

# [fit]

---

# [fit] Community

---

# Popular comparisons

[.column]

- Ease of use
- Performance
- Community
- Documentation
- Jobs

[.column]

- Ecosystem
- Features
- Code quality
- Deployment

---

# [fit] Things I care about

[.column]

- Explicitness
- Type hints as a superpower
- Gaurdrails
- Developer experience

[.column]

- Security
- Async support
- Persistence
- Sweet spots (where a framework excels)

---

---

<!-- ---

# About Me

[.column]

Daniel Roy Greenfeld

Senior Software Engineer @ Kraken Technologies

Author, Coder, Leader

Husband of Audrey Roy Greenfeld

Father

Superhero saving the planet

[.column]

![fit](assets/facebook-avatar.jpg) -->
