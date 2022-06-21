autoscale: true
slide-transition: true

[.background-color: #003c80]
[.header: #FFFFFF, Avenir Next Bold]
[.text: #FFFFFF, Avenir Next Bold]

# [fit] Scaling from One to Billions

# [fit] How to change the world as a software engineer

Daniel Roy Greenfeld

---

[.background-color: #003c80]
[.header: #FFFFFF, Avenir Next Bold]
[.text: #FFFFFF, Avenir Next Bold]

# [fit] Scaling from One to Billions

# [fit] How to change the world as a software engineer

Daniel Roy Greenfeld

---

[.background-color: #003c80]
[.header: #FFFFFF, Avenir Next Bold]

# [fit] Olá Portugal!

![inline](assets/dc-logo-blug.png)

---

# Way back in

# [fit] 2004

---

[.background-color: #90EE90]

# [fit] I had long hair

![inline](assets/long%20hair.png)

---

[.background-color: #ecd540]

# Got interview at NASA

![inline full](assets/280_NASAMeatball.jpg)

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]

# [fit] 😞

# [fit] No way I was going to work for NASA

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]
[.text: #FFFFFF, Avenir Next Bold]

# [fit] No computer science degree

# [fit] Only 7 years professional experience

---

# [fit] Plan

---

# [fit] Treat interview as a practice session

![inline full](assets/jackie-benny.jpeg)

### Still from Jackie Chan's 1984 movie "Meals of Wheels"

---

# [fit] Test new approaches to typical questions

![inline full](assets/sat-test.jpeg)

---

[.background-color: #00FFFF]

# [fit] Have fun!

---

# [fit] How it went

---

# [fit] **"What's your biggest weakness?"**

## - NASA Interviewer

---

<br><br>

# **"My biggest weakness is that I'm emotionally tied to my work so if I'm not doing well I take it personally. Then I work longer and harder to improve."**

## - My normal response

---

[.background-color: #ecd540]

# This time:

<br>

# [fit] "I'm stupid and lazy"

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]

# NASA Interviewer

<br>

# [fit] "WTF?!"

---

[.background-color: #FF0000]
[.header: #FFFFFF, Avenir Next Bold]

# NASA Interviewer

<br>

# [fit] "You going to explain that?"

---

[.background-color: #ecd540]

# [fit] I'm stupid

---

# I'm stupid

- Can't figure things out
- Can't remember things
- Too stupid not to ask stupid questions

---

# [fit] Let's go over each item

---

### I'm stupid

## Can't figure things out

---

[.background-color: #00FFFF]

### I'm stupid

## Can't figure things out

# Always look for libraries first

---

## Can't figure things out

# OMG argparse

```python
import argparse

# sub-command functions
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

parser.parse_args()
```

---

## Can't figure things out

# Yay Typer!

```python
import typer

app = typer.Typer()


@app.command()
def foo(y: float, x: int = 1 ):
    print(x * y)

@app.command()
def bar(z: str):
    print(f'(({z}))')


if __name__ == '__main__':
    app()
```

---

![inline](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)

# [fit] [typer.tiangolo.com](https://typer.tiangolo.com/)

---

[.background-color: #00FFFF]

### I'm stupid

## Too stupid not to ask stupid questions

---

[.background-color: #00FF00]

## _hint:_

# There are no stupid questions

---

[.background-color: #00FFFF]

## _hint:_

# The only bad question is the one you do not ask

---

[.background-color: #00FF00]

## _important professional advice:_

# Don't try to impress people by not asking questions

---

[.background-color: #00FFFF]

### Ashamed to ask questions?

## No one cares

## No one remembers

---

## Too stupid not to ask stupid questions

# Obey the Thirty Minute Rule

# [fit] [daniel.feldroy.com/30](https://daniel.feldroy.com/30-minute-rule)

![inline](assets/young-me.jpg)

---

# Obey the Thirty Minute Rule

## Don't waste more than 30 minutes on a problem without asking questions

---

# Obey the Thirty Minute Rule

## Change to 60 minutes if you like

---

# Important: Don't be a jerk and not let other people ask questions

![inline full](assets/young-me.jpg)

---

## I'm stupid

# Can't remember things

---

[.background-color: #00FFFF]

## Can't remember things

# Docstrings are awesome

---

[.background-color: #00FF00]

## Can't remember things

# Typehints are awesome too, use them to reduce docstrings

---

# Remember this?

## Typehints means we don't have to write so many docs

```python
import typer

app = typer.Typer()


@app.command()
def foo(y: float, x: int = 1 ):
    print(x * y)

@app.command()
def bar(z: str):
    print(f'(({z}))')


if __name__ == '__main__':
    app()
```

---

[.background-color: #00FFFF]

## Can't remember things

# Use markdown because

# of ease and portability

---

# Markdown is so awesome it has a logo!

![inline full](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/640px-Markdown-mark.svg.png)

---

### Can't remember things

## When following a talk or tutorial,

# Write down even the slide bullets!

---

# For most people writing down notes enhances learning

---

## I'm stupid

# Can't remember things

Me back in the day:

- [pydanny-event-notes.readthedocs.io/](https://pydanny-event-notes.readthedocs.io/)
- [daniel.feldroy.com/posts/2011-12-story-of-live-noting](https://daniel.feldroy.com/posts/2011-12-story-of-live-noting)

---

### I'm stupid

## Can't remember things

# Documentation makes

# me look good!

---

## Documentation makes me look good!

# I can pull out old tech details that others don't have

---

[.background-color: #ecd540]

## Documentation makes me look good!

# Can be used later on other projects

---

## Documentation makes me look good!

# Great for book content

![inline full](assets/Two-Scoops-of-Django-3-Alpha-Cover_1080x.jpg)

---

## Documentation can make you look good too:

# [docs.python-requests.org](https://docs.python-requests.org/)

# [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

![inline](https://docs.python-requests.org/en/latest/_static/requests-sidebar.png)![inline](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

---

[.background-color: #ecd540]

# [fit] I'm lazy

---

# I'm lazy

- Don't wanna do anything twice
- Don't wanna debug code when I had it working before
- Don't wanna look hard for docs

---

# [fit] Here we go on laziness!

---

### I'm lazy

## Don't wanna do anything twice

# If I write the same code twice I stick in a function

---

### I'm lazy

## Don't wanna do anything twice

# I use typehints so I write less docs

---

### I'm lazy

## Don't wanna do anything twice

# I stick the function into a `utils` module

---

### I'm lazy

## Don't wanna do anything twice

# I put the function on GitHub so I don't lose it

---

### I'm lazy

## Don't wanna do anything twice

# Isn't this the foundation of open source?

---

[.build-lists: true]

## I'm lazy

# Don't wanna debug code that worked before

- Manually testing code by watching it run is hard
- ...and boring
- ...and hence is error prone
- ...meaning you have to do more work

---

### I'm lazy

## Don't wanna debug code when I had it working before

# Write down how to test lest you forget

![inline](assets/running-tests.png)

---

## I'm lazy

# Don't wanna look hard for docs

Every project should have a README that covers:

- Installation
- Running the code
- Testing the code

---

## I'm lazy

# Don't wanna look hard for docs

Longer form docs should use:

- readthedocs.io
- GitHub pages
- Whatever

---

# [fit] Did I get the job at NASA?

<br>

# [fit] ?

---

[.background-color: #ecd540]

# [fit] Yes

---

# [fit] In hindsight I was lucky

---

# [fit] Thank you

# [fit] Sharon Campbell

---

# [fit] One of my favorite managers ever

# [fit] Sharon Campbell

## If you're watching this video, please contact me, Octopus Energy could use your talents

---

# [fit] Sharing Code

- Books
- Blog
- Open source

---

# [fit] Ethics in Code

![inline](https://media.giphy.com/media/mCClSS6xbi8us/giphy.gif)

---

# [fit] Our Work used for evil

- Cambridge Analytica
- CIA/NSA attack systems
- OpenCV (and other tools) used to spy on citizens

---

![inline](assets/1920px-Cambridge_Analytica_logo.svg.png)

- Private intelligence company
- Used unethically gathered facebook data
- Used open source tools to be build an analytics platform
- Affected multiple elections

---

Cambridge Analytica

- Private intelligence company

- Used unethically/illegally gathered facebook data

- Used open source tools to be build an analytics platform

- Affecte elections around the world

---

# [fit] Challenge of Open Source and Open Knowledge Share

- We share so everyone can benefit
- Unfortunately "everyone" includes causes we do not like

---

# [fit] IMO this is an Unfixable Problem

- Knowledge is like the current state of firearms in the USA
- Distribution is too easy
- TODO this might distract from the talk

---

# [fit] Instead, focus on ethical causes

- We cannot change society easily
- Another approach is to use our skills for the direct good
- My choice is climate change

---

# [fit] What's your choice?

- Better medical care
- Use OpenCV to do analytics on crops, not people
- Build the future we want, not what dudebros/dudesisters are trying to exit on
- TODO come up with a bunch more

---

# [fit] About Me

![inline full](https://2022.pythonwebconf.com/speakers/daniel-roy-greenfeld/@@images/6ff422d2-3007-40af-9441-3ca9ef5a940d.jpeg)

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

[.background-color: #00FF00]

# [fit] Using my skills to fight climate change!

# [fit] Working at Octopus Energy

![inline](assets/super_octo.png)

# Want to be a planet-saving superhero?

---

[.background-color: #c9e9f6]

# [fit] Questions

# [fit] 🤔

---

# [fit] Links

- [https://daniel.feldroy.com/posts/thirty-minute-rule](daniel.feldroy.com/posts/thirty-minute-rule)
- [https://daniel.feldroy.com/posts/code-code-code](daniel.feldroy.com/posts/code-code-code)
- [pydanny-event-notes.readthedocs.io/](https://pydanny-event-notes.readthedocs.io/)
- [daniel.feldroy.com/posts/2011-12-story-of-live-noting](https://daniel.feldroy.com/posts/2011-12-story-of-live-noting)
- [typer.tiangolo.com/](https://typer.tiangolo.com/)
- [fastapi.tiangolo.com/](fastapi.tiangolo.com/)
- [meetup.com/django-houston/events/285599646/](https://www.meetup.com/django-houston/events/285599646/)
