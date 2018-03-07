# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:02:32 2018

@author: onion
"""
#==============================================================================
# 选择排序 SelectionSort
# 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到 "已排序序列"的末尾。
# 以此类推，直到所有元素均排序完毕
#核心，开始时，锁定最小元素应该存放的位置：第0位。然后从余下元素中找出最小值，替换第0位
#比如a=[2,5,1,3],a[0]=2,从[5,1,3]中找出最小的是第二位元素a[2]=1,交换a的第0元素与第2元素（而不是每次都与a[0]比较，得：【1，5，2，3】
#=从小到大排列=============================================================================
def SelectionSort(array):
    
    length = len(array)
    
    if length == 0 :
        
        return False

    else :
               
        for i in range(0,length):
            
           
            mini =i#此次遍历的min值在数组中的位置
            
            for j in range(i+1,length):                                             
                if array[j] > array[mini]: 
                    mini=j #此次比较产生了更小的值，记录它的下标
                    
                array[j],array[mini] = array[mini],array[j]        
            
        return array   