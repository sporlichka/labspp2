x = "hello world"
print(len(x))
## 11
txt = "Hello World"
x = txt[0]
print(x)
## H
txt = "Hello World"
x = txt[0:8]
print(x)
## Hello Wo
txt = " Hello World "
txt = txt.strip()
print(txt)
##Hello World
txt = "Hello World"
txt = txt.upper()
print(txt)
txt = txt.lower()
print(txt)
##
txt = "Hello World"
txt = txt.replace("l", "y")
print(txt)
##Jello world
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))