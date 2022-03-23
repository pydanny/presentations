autoscale: true
slide-transition: true

# [fit] Confessions of

# [fit] Joe Developer

Daniel Roy Greenfeld

---

# [fit] Confessions of

# [fit] Joe Developer

Daniel Roy Greenfeld

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

[.background-color: #FF0000]
[.header: #FFFFFF]

## Use markdown because of ease/portability

# Even when I wrote daily in RST I had to look stuff up

---

## Use markdown because of ease/portability

# Markdown is easy to learn

---

## Use markdown because of ease/portability

# Reduce friction in your docs!

---

# Markdown is so awesome it has a logo!

![inline full](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/640px-Markdown-mark.svg.png)

---

### Can't remember things

## When following a talk or tutorial,

# Write down even the slide bullets!

---

# For some people writing down notes enhances learning

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

## Documentation can you look good too:

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

## If you're watching this video, please contact me, my company could use your talents

---

# My history at NASA

- Started in 2005, ended in 2010
- Coded a lot
- Learning Python and Django
- Started what became django-crispy-forms
- Met my wife
- Learned about climate change

---

# My history at NASA

- Started in 2005, ended in 2010
- **Coded a lot**
- Learning Python and Django
- Started what became django-crispy-forms
- Met my wife
- Learned about climate change

---

[.background-color: #ecd540]

# [fit] Coded a Lot

---

# [fit] Code, Code, Code

# [fit] [daniel.feldroy.com/posts/code-code-code](https://daniel.feldroy.com/posts/code-code-code)

---

[.background-color: #00FF00]

## [fit] If you want to get good at anything

# [fit] Practice

---

[.background-color: #00FF00]

## [fit] Practice what you learn from this event

# [fit] Use It

---

[.background-color: #00FFFF]

# [fit] Always be typing

---

# [fit] Pairing is great

---

# [fit] But if you're trying to improve?

---

[.background-color: #00FFFF]

# [fit] Always be the person typing

---

# [fit] Taking a class?

---

[.background-color: #00FFFF]

# [fit] Always be typing

---

# [fit] No exercises in the class?

---

[.background-color: #FF0000]
[.header: #FFFFFF]

# [fit] Then you are watching

# [fit] a spectator sport

---

# [fit] You will learn as a spectator

# [fit] just not as fast

# and...

---

[.background-color: #FF0000]
[.header: #FFFFFF]

# [fit] Mastery can't be

# [fit] found as a spectator

---

# [fit] "You can't become a tech CEO by

# [fit] watching the social network"

---

# [fit] You can't win at

# [fit] sports by watching TV

---

# [fit] To master anything...

---

# [fit] To master coding...

---

[.background-color: #00FF00]

# [fit]... you have to practice

---

[.background-color: #00FF00]

# [fit] Practice makes perfect

---

[.background-color: #00FFFF]

# [fit] Always be typing

---

# [fit] Code, Code, Code

# [fit] [daniel.feldroy.com/posts/code-code-code](https://daniel.feldroy.com/posts/code-code-code)

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

# [fit] Want to use your skills to fight climate change?

![inline](assets/super_octo.png)

# Want to be a planet-saving superhero?

---

## Join me at Octopus Energy. We're hiring!

# [fit] [octopusenergy.com/careers](https://octopusenergy.com/careers)

![inline](assets/browsing.png)

---

# [fit] Questions

# [fit] 🤔
