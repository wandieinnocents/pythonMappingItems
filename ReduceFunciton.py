from functools import reduce

listItems = ListItems = [1,2,3,4,5,6,8,10]

#without Recue

sum = 0
for item in listItems:
    sum = sum + item
print("Sum without Reduce: {}".format(sum))

#while using reduce

sum2 = reduce(lambda x,y: x+y ,listItems)
print("Sum with Reduce: {}".format(sum2))