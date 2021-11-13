# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:52:17 2021

@author: HS
"""


my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]



def flatten(a_list):
    
    str_list = str(a_list)
    str_list = str_list.replace("[","").replace(("]"),"")
    result = str_list.split(",")
    return result
            
            
    
    



    
    
den =  [[1, 2], [3, 4], [5, 6, 7]]    
# [[[7, 6, 5], [4, 3], [2, 1]]
    
def reverse_list_2(my_list):
    my_list = list(reversed(my_list))
    len_of = len(my_list)
    for ind in range(len_of):
        my_list[ind] = list(reversed(my_list[ind]))
        
    return my_list

print(reverse_list_2(den))




    