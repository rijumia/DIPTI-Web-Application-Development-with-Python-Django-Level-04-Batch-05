def greet(name='Guest'):
    print('Hello ', name)
    print(f'I am f string {name}')
    
greet('Mr Admin')
greet()


#Create a function with three parameter and print four time first empty, second print two number sum three number sum, fourth sum four number
def Num(num1=0, num2=0, num3=0):
    print('Sum Num: ',num1+num2+num3)
    
Num()
Num(3)
Num(3,4)
Num(3,5,9)


def color(*col):
    print('Color are :',col[1])
color('Black','Blue')