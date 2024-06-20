
""" 
Topic: Metaclass

Defination:

A metaclass is a class that allows for other classes to be instantiated 
as objects of the metaclass.

Usage:

Metaclasses allow for code not only to manipulate data, but to manipulate classes. 
Often this change happens when an object of the class is instantiated. 
Using metaclasses also helps to abstract our code, making it more readable and 
helping to reduce the amount of code written by avoiding repetition in code.

A metaclass might be created that prohibits classes that are instances of the metaclass
from being created more than once. This is an example of the Singleton design pattern, 
which can be helpful for creating classes that connect to external sources, as it prevents 
more than one connection from being open at a time.

Metaclasses allow for something called metaprogramming. Metaprogramming is the creation of
classes that assist programmers when writing code by creating an infrastructure that the 
programmer can build on top of, rather than starting from scratch. Metaclasses provide these
frameworks through their attributes, methods, and objects that the programmer can use.

This metaprogramming nature of the metaclass means that often metaclasses are used by programmers,
but are less often created by them. However, they are extremely useful for programmers creating 
the frameworks that so many other programmers use.
"""

url_sentry = "https://sentry.io/answers/what-are-Python-metaclasses/"
url_youtube = "https://www.youtube.com/watch?v=NAQEj-c2CI8"