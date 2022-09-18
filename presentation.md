![inline](django-houston.jpeg)

---

![inline](django-houston.jpeg)

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]

# [fit] Django and Python Anti-Patterns

---

# [fit] Don't do any of this if you want to do well

---

# Adding these techniques to an existing codebase is called:

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]

# [fit] Re\*\*\*\*toring

---

# Let's do it!

---

# Don't use `request.POST or None`

```python
def someview(request):
    form = MyForm(request.POST or None)
    # …
```

# Be more explicut

```python
def someview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES) # …
    else:
        form = MyForm() # …
```

---

# Don't switch databases to improve performance

Instead, learn how to:

- Index tables correctly
- Optimize slow queries
- Add caching

---

# Do use the right database for each task

- SQL or columnar DB for column-based data
- Unstructured databases for unstructured data

---

# Dont engage in fancy settings configurations

- Simple is better than complex
- Keep settings out of databases
  - Especially what Django apps are being installed

---

# Don't put complex business logic in wrong places

- Templates (Although JQuery/Vanilla JS made this fun)
- Settings
- Context processors
- Middleware

---

# Don't Use Metaclasses in Django

---

# Don't Use Metaclasses in Django

- Meta != Metaclasses
- Use of Metaclasses in Django is **architecture astronauting**
- 13 years of Django and I've never seen a reason outside of building FOSS efforts
  - Even in FOSS it is rare

---

# What is Architecture Astronauting?

---

# What is Architecture Astronauting?

- Finding reasons to use obscure design techniques because they look "nifty"
- Often results in hard-to-maintain and debug code
- Usually created by intermedate-to-senior engineers getting pretentious

---

# Stay away from Concrete Models

- Abstract models are the way to go to re-use model code
- Concrete models are a stupid inclusion
- Anyone who finds a way to justify concrete models is **architecture astronauting**

---

# Don't set model fields in setting files

---

# Don't set model fields in setting files

In `settings.py`:

```python
from django.db import models

blog_fields = [
    models.CharFields("title", max_length=50),
    models.TextField("note")
]
```

Instead, define models in models modules.
It's where people expect to find them.

---

[.background-color: #660300]
[.header: #8C0500, Avenir Next Bold]

# Don't present using low contrast between text and slides

---

# Don't overload Python built-ins

```python
object = MyObject()
map = Map()
zip = 90213 # common US developer mistake
id = 34 # I still make this mistake

```

---

# Don't flip the booleans!

```python
true = False
false = True
```

Usually to support an API

---

# Fun fact: This worked in Python 2

```python
True = False
```

---

# Don't identify variable types with prefixes

```python
strColor = "green"
boolActive = False
intPythonYears = 20
dtPythonFirstUsed = "10/20/2005"
```

Mixing case doesn't help at all

---

# Don't try to save pixels on the screen by removing vowels

```python
clr = "green"
ctv = "False"
pythnYrs = 20
pythnFrstSd = "10/20/2005"
```

---

# OMG WTF!?

```python
c = "green"
a = "False"
p = 20
t = "10/20/2005"
```

---

# The pixel shortage ended years ago

- We have big monitors and screens
- Use reasonably descriptive variable names
- Don't get overly long

---

# Do use type hinting

- Speeds up documentation writing
  - Because you don't have to write so much of it
- Empowers IDEs
- Allows some neat tricks in performance optimization that are starting to emerge

---

# Be aware of the enumerate built-in

```python
foo = [1, 2, 3]

for i, item in zip(range(len(foo)), foo):
    print(i, item)
```

---

# Don't get hung up on semantic quizzes

"What is the result of this slicing?"

```python
foo = [1, 2, 3]
foo[0:-3:-5]{!}
```

Often found in community language groups.

It doesn't matter, these games of semantics don't make you a better coder.

---

# Don't use property setters as action methods

```python
class WebService:

    @property
    def connect(self):
        self.proxy = xmlrpc.Server('https://service.xml')

if __name__ == '__main__':
    ws = WebService()
    ws.connect
```

---

# Don't Pass Generic Exceptions Silently

```python
try:
    do_akshun(value)
except:
    pass
```

- Ignorance is **not** bliss
- You have no idea what your system is doing
- Arguably better to not have this in your code

---

# Do use specific exceptions

```python
class CustomException(Exception):
    pass

try:
    do_akshun(value)
except AttributeError as e:
    # do something here
except Exception as e:
    raise CustomException(e)
```

---

# [fit] About Me

---

# [fit] Daniel Roy Greenfeld

<br>

# [fit] AKA "pydanny"

---

# [fit] Coder

# [fit] Leader

# [fit] Speaker

---

# [fit] Author, Husband

![inline](https://www.feldroy.com/_next/image?url=%2Fimages%2FTwo-Scoops-of-Django-3-Alpha-Cover_1080x.jpg&w=3840&q=75)![inline](https://daniel.feldroy.com/images/danny-and-audrey-tsd111.jpg)![inline](https://daniel.feldroy.com/images/two-scoops-django-co-authors-M.jpg)![inline](https://daniel.feldroy.com/images/tsd15-beta.png)

---

# [fit] Father

![inline full](https://daniel.feldroy.com/images/uma-2020.png)

# [fit] Working to give her the best planet possible

---

# [fit] Want to use your skills to fight climate change?

![inline](confessions-joe-dev/assets/super_octo.png)

# Want to be a planet-saving superhero?

---

## Join me at Octopus Energy. We're hiring!

# [fit] [octopusenergy.com/careers](https://octopusenergy.com/careers)

![inline](confessions-joe-dev/assets/browsing.png)

---

# [fit] Questions

# [fit] 🤔
