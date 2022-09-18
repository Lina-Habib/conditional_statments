
count = 0

arr_of_num = []


while count < 5:
    num = input("Enter a number: ")
    arr_of_num.insert(count,num)
    count +=1

max = arr_of_num[0]

for index in arr_of_num:
    if index > max:
        max = index

min = arr_of_num[0]

for index in arr_of_num:
    if index < min:
        min = index

print("The max num = " + str(max))
print("The min num = " + str(min))