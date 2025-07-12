print("Variables File")
"""
variables name rule :
1. can not start with number
2. can not have space
3. can not have special characters
4. can not be keyword
5. can not be reserved words
6. can not be uppercase
7. can not be lowercase
8. can not be mixed
9. can not be too long
10. can not be too short

python keywords list :
and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, global, if, import, in, is, lambda, nonlocal, not, or, pass, print, raise, return, try, while, with, yield 
"""
# num1 = 150
# num2 = 88

# print("Sum Of: ", num1 + num2)
# print("Subtraction Of: ", num1 - num2)
# print("Multiplication Of: ", num1 * num2)
# print("Division Of: ", num1 / num2)

name = address = email = "Riju"
print("Name: ", email)



value1 = 50
value2 = 20

print("Int To String: ", str(value1) + str(value2))


glo = "I am global variable"

def myFun():
    global gl
    gl = "I am local variable"
    print(glo)

myFun()
print(gl)
