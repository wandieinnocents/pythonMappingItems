


def main():

    #list_items
    ListItems = [1,2,3,4,5]

    print("lst+items: {} ".format(ListItems))
    # with mapping
    tempList = []
    for item in ListItems:
        tempList.append(item*2)
    print("temp list+items: {} ".format(tempList))

    #with mapping
    listItems2 = list(map(lambda  x:x*2 , ListItems))
    print(listItems2)

    #adding 3 on each value
    listAdd = list(map(lambda x:x+3 , ListItems))
    print(listAdd)

if __name__ == '__main__':main()
