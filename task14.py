my_list = []
num = int(input('number of elements  '))
for i in range(0, num):
    val = int(input( 'Enter an integer value  '))
    my_list.append(val)
    print(my_list)
    for ev in my_list:
        if ev % 2 == 0:  
            print (ev)