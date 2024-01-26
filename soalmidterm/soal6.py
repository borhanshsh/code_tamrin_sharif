def modify_objects(obj1, obj2):
    obj1[0] = 'X'
    obj1.append(obj2[0])
    obj2 = obj2 + 'Y'
    print(obj2)
my_list = [1, 2, 3, ['A', 'B']]
my_string = 'ABC'
modify_objects(my_list, my_string)
print("List:", my_list)
print("String:", my_string)