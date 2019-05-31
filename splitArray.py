#将一个大数组分解为 固定元素的若干个小数组 ， 并把这些小数组的均值放到一个新数组

#LIUYANG    2019-05-31 



import numpy as np
from statistics import mean 

#a=[1, 2, 3, 4, 5, 6, 7,8,9,10,11]
#a_split=np.array_split(a, 4)     # 这是把数组分解为  4个子数组 
#print(a_split)

 



my_list = [1, 2, 3, 4, 5, 6, 7,8,9,10,11]
  
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def SplitArrayAndCalAver(arraySrc,arrayDst,n):
    x = list(divide_chunks(arraySrc, n)) 
    for j in range(len(x)):
        arrayDst.append(mean(x[j]))
     


# How many elements each 
# list should have 
n = 3
  
#x = list(divide_chunks(my_list, n)) 

result=[]

#for j in range(len(x)):
#    print(x[j])
#    print(mean(x[j]))
#    result.append(mean(x[j]))

SplitArrayAndCalAver(my_list,result,3)

print(result) 




