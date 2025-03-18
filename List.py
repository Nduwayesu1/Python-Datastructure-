def my_list():
    my_lists=[]
    n=int(input("Enter the number of elements:"))

    for i in range(0,n):
       my_lists.append(int(input("Enter an element:")))

    return my_lists

def my_Dict():
    my_dicts={}
    m=int(input("Enter the number of elements(Key-pair):"))

    for i in range(0,m):
       key=input("Enter a Key-value:")
       value=input("Enter a Value:")
       my_dicts[key]=value
    return my_dicts   


print("My List:")
print(my_list())
print("My Dictionary :")
print(my_Dict())