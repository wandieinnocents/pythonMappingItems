
listItems = ListItems = [1,2,3,4,5,6,8,10]
#without Filter

tempList = []
for item in listItems:

    if(item % 2 == 0):
        tempList.append(item)

print("\nWithout Filter: {}".format(tempList))


#printing list using filters
tempList2 = list(filter(lambda x:x%2 == 0, listItems))
print("With Filter: {}".format(tempList2))






