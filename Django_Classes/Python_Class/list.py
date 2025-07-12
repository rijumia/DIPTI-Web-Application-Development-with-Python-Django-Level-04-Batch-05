list = ["Rahim", "Karim", "Kuddus", "Shakib", "Khan", "Tamim", "Mushfiq"]
print("********************** Copy List  ***********************")
old_list = list.copy()

print("Full List: ",list)
print("First 3 Items: ",list[:3])
print("Index 2: ",list[1])
print("Index 3 to 4: ",list[2:4])
print("Last Item: ",list[-1])
print("Last 2nd Item: ",list[-2])
print("Random Item: ", list[3]," & ", list[5])
print(list[-5:-3])
print("*******************Append**************************")

list.append("Hasan")
print(list)

print("*********************0 Index Replace************************")

list[0] = "akkash"
print(list)

print("**********************Insert***********************")

list.insert(1, "Santo")
print(list)

print("**********************Old List***********************")
print("Old List: ", old_list)

print("**********************Remove***********************")
list.remove("akkash")
print("After Remove: ", list)
print("**********************Pop***********************")
list.pop(2)
print("After Pop: ", list)

list2 = [1, 2, 3]
print("**********************List Extend***********************")
list2.extend(list)
print("Extend List: ", list2)

