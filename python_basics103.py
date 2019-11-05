# Functions!
# Functions are like machines
# They can take in inputs and do things to them.
# doings things is called running a block of code!

# syntax

#def <name>(arg1, arg2):
   #Block of code (inside block)
   #Block of code(inside block)
   #>> return something (using the key word return)(inside block)

# (outside block of code) - indentation defines blocks

# functions need to be called to work

def greeting():
    welcome_message = 'Welcome to your life as a coder'
    return welcome_message #need to return a value to use it

print(greeting())



def greeting_person(name):
    welcome_message = 'Welcome my friend'
    full_message = welcome_message + ' ' + name + '!'
    return full_message

print(greeting_person('Jillian'))
print(greeting_person('Fred'))
print(greeting_person('Jack'))
print(greeting_person('Emily'))


def greeting_full_name_anything(f_name, l_name):
    welcome = 'You rock'
    full_message = welcome + ' ' + f_name + ' ' + l_name
    return full_message

print(greeting_full_name_anything('Sam', 'Forrester'))
print(greeting_full_name_anything('Miles', 'Killometers'))

#Topics covered:
# defining functions
# calling function
# using arguments in function
# returning values
