# Задайте список. Напишите прграмму, которая определяет, присутствует ли в
# заданном списке некое число
my_list = ['sdf13','fds66','34']

def found(list_, x):
    #a = ['sdf13','fds66','34']
    for i in list_:
        if x in i:
            print(i)
        #else:
            #print('нет')    
    
            
found(my_list,'3')            
