import pyjokes #this is a module(code written by someone else which we can use in our programs) . we can use it by importing in our code
 
#this module is installed using pip (package manager for python) command : "pip install 'module_name'"

# 2 types of modules : built-in modules and third-party modules
#built-in modules (pre installed in python) eg : os, random etc
#third-party modules (installed using pip) eg : pyjokes, tensorflow, flask etc

joke  = pyjokes.get_joke("en", "neutral")
print(joke)