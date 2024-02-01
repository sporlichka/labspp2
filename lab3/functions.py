#1
def my_funciton():
    print("hello from the function")
#2
def my_funciton():
    print("hello from the function")
my_funciton()
#hello from the function
#3
def my_function(fname, lname):
  print(fname)
#prints fname
#4
def my_function(x):
   return x + 5
#5
def my_function(*kids):
  print("The youngest child is " + kids[2])
#"The youngest child is " + third elemnt of kids
#6
def my_function(**kid):
  print("His last name is " + kid["lname"])
