print('input your elements(one by one in a column) then just enter:')
try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 

except: 
    print('your list: ', my_list, end='\n\n') 
for i in my_list:
    if i%3 == 0 :
      print(i)
input('press enter to exit')
