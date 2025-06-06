#1 If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

'''
#2 If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
'''

#3
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#4 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#5 
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#6 short
if a > b: print("a is greater than b")

#7
a = 2
b = 330
print("A") if a > b else print("B")


#8 One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#9 Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#10 Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#11 Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


#12 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#13 pass 
a = 33
b = 200

if b > a:
  pass


