numbers = [12, 85, 98, 47, 69, -9]

print("************Print Odd Or Even Number**********")
for num in numbers:
    if num%2==0:
        print(num, " is Even Number")
    else:
        print(num, " is Odd Number")

print("*************Print Possitive Or Negative Number****")
for num in numbers:
    if num>=0:
        print(num, " is Possitive Number")
    else:
        print(num, " is Negative Number")

print("************Print Odd Or Even Number from 1 to 20**********")
for item in range(1,21):
    if item%2==0:
        print(item,"Is Even Number")
    else:
        print(item,"Is Odd Number")



print("************Print Sum of the all number from a list**********")
total = 0
for num in numbers:
    total += num
print("Sum Of List Number :", total)


print("**********Count How Many Odd Or Even Numbers From 1 To 20**********")
even = 0
odd = 0
even_sum =0
odd_sum =0
for n in range(1, 21):
    if n%2==0:
        even += 1
        even_sum += n
    else:
        odd += 1
        odd_sum += n
print("Total Odd Num:",odd,"Total Even Num: ",even)
print("Sum Odd Num:",odd_sum,"Sum Even Num: ",even_sum)


print("**********Find Largest Number in a list**********")
largest = 0
for num in numbers:
    if num > largest:
        largest = num
print("Largest Number is: ", largest)


print("**********Print the Multiplication Table of Number 5**********")
for m in range(1,11):
    print("5*",m,"=",m*5)




