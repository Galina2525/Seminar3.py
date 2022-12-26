# Напишите программу, которая определит позицию второго вхождения строки в списке
# либо сообщит, что ее нет
# список ['qwe','asd','zxc','qwe','ertqwe'], ищем 'qwe', ответ 3
#['йцу','фыв','ячс','цук','йцукен', 'йцу'], ищем 'йцу', ответ 5
#['йцу','фыв','ячс','цук','йцукен'], ищем 'йцу', ответ -1
#['123','234',123,'567'], ищем '123', ответ -1
#[], ищем '123', ответ -1

my_list = ['йцу','фыв','ячс','цук','йцукен', 'йцу']
def found(list_,x):
    count = 0
    for i in range(len(list_)):
        if list_[i] == x:
            count += 1
            if count == 2:
                return i 
    return -1 
                    
print(found(my_list,'йцу') )

# my_list = ['123','234',123,'567']
# def found(list_,x):
#     new_list = []
#     for i in range(len(list_)):
#         if x == list_[i]:
#             new_list.append(i)
#     if len(new_list)<=1:
#         return -1
#     return new_list[1]    

# print(found(my_list,'123'))           
 

      