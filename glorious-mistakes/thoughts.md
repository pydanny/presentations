Segments to include

0. First trip back to Lithuania in over 100 years

- My great-grandfather left a long time ago
- When my daughter is little older, we'll go to the hold home town. I'll put my feet in the river/lake/stream

1. Missed interview

Done

2. Zope
   - Mostly known for old Zope guys saying, "What Django can learn from zope"
   - Unnecessary use of XML (built in the Java days)
   - Most of the time those talks were saying "Django isn't handling this edge case, add more complexity!"
   - Victim of pissing contests to demonstrate sophistication of code
   - Overlying sophisticed code == overly complex

   However,
   - Simple underlying components
      - ZODB, late 1990s no-SQL that was pickled, indexed, Python object (with all the familiar types)
      - URL routing! They invented it

   - But the community added complexity via Plone and other frameworks on top of Zope
      - Interfaces felt like Java AbstractAbstractFactoryFactory
      - More and more complex systems to account for the 5% edge case
      - Easy things were made hard, hard things were made nigh impossible
   
   - Eventually the community left
      - Django was easier
      - Grok was an attempt to simplify the tooling, but it wasn't really easy
      - Then Flask made it even easier
      - Pyramid had some neat ideas, but never got traction

3. My own example making easy things hard in the Zope world

- false = True
- true = False

4. Environment that led to Two Scoops of Django
   - Pissing contest to demonstrate sophistication of code
      - Database-powered installed apps
      - Let's reinvent None!
      - Unnecessary Metaclasses instead of standard inheritence 
      - Concrete models, generic foreign keys, etc
      - My own mistakes with webhook packages
   - Tons of implicit behaviors
   - Upgrades made hard
   - Flask bypassed all that at the right time (and with a funny April fool's day joke)

5. Types - Love and hate it
   - "I like types but they aren't always good" David Seddon
   - For control of behaviors they are bliss
   - At least some components borrow from Zope (typing.Prototol are Zope subtypes)
   - For catching bugs before they reach production?
   - Sometimes types are hard to implement
   - Mypy is slow even on modest projects
   - Upgrading mypy can be really hard
   - contention:
      - Are types the Zope of this era?
      - Apologies to Stephen More: typing.Any is my safety valve

6. Climate



Here's an outline for a talk on "Lessons Learned Over 25 Years of Making Mistakes Coding with Python":

I. Introduction
   A. Personal journey with Python
   B. Importance of learning from mistakes

II. Early Mistakes and Lessons
   A. Indentation errors
   B. Naming conventions
   C. Misunderstanding scope

III. Design and Architecture Pitfalls
   A. Lack of modularity
   B. Spaghetti code
   C. Premature optimization

IV. Testing and Debugging Woes
   A. Neglecting unit tests
   B. Ineffective debugging techniques
   C. Overlooking edge cases

V. Performance Blunders
   A. Inefficient algorithms
   B. Improper use of data structures
   C. Ignoring profiling

VI. Collaboration and Version Control Mishaps
   A. Merge conflicts
   B. Poor code review practices
   C. Lack of documentation

VII. Security and Robustness Oversights
   A. Input validation vulnerabilities
   B. Handling exceptions properly
   C. Dependency management

VIII. Staying Up-to-Date and Future-Proofing
   A. Embracing new language features
   B. Keeping up with best practices
   C. Avoiding technical debt

IX. Lessons for the Next Generation
   A. Cultivating a growth mindset
   B. Embracing continuous learning
   C. Sharing knowledge and mentoring

X. Conclusion
   A. Recap of key lessons
   B. Importance of learning from mistakes
   C. Call to action for self-improvement





Some of the key points in the outline:

III. Design and Architecture Pitfalls
    A. Lack of modularity
       1. Monolithic code becomes hard to maintain and extend
       2. Importance of separating concerns and writing modular code
    B. Spaghetti code
       1. Convoluted control flow and deeply nested conditionals
       2. Readability and maintainability issues
    C. Premature optimization
       1. Sacrificing code clarity for performance without profiling
       2. "Make it work, make it right, make it fast" principle

IV. Testing and Debugging Woes
    A. Neglecting unit tests
       1. Short-term gain, long-term pain
       2. Benefits of test-driven development (TDD)
    B. Ineffective debugging techniques
       1. Print statement debugging vs. proper use of debuggers
       2. Importance of logging and error handling

VI. Collaboration and Version Control Mishaps
    A. Merge conflicts
       1. Frequent merging and communication to avoid conflicts
       2. Resolving merge conflicts effectively
    B. Poor code review practices
       1. Importance of code reviews for catching issues early
       2. Constructive feedback and code ownership

VII. Security and Robustness Oversights
    A. Input validation vulnerabilities
       1. Injection attacks and data sanitization
       2. Principle of least privilege
    B. Handling exceptions properly
       1. Catch specific exceptions and provide meaningful error messages
       2. Avoid catching broad exceptions like Exception

IX. Lessons for the Next Generation
    A. Cultivating a growth mindset
       1. Embracing challenges and seeing failures as learning opportunities
       2. Humility and openness to feedback
    B. Embracing continuous learning
       1. Keeping up with language updates and best practices
       2. Participating in community events and staying involved

I can provide more details and examples for each of these points to further flesh out the content of the talk.