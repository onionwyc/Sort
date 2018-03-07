# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:48:49 2018

@author: onion
"""

#插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

def InsertionSort(array):
    length = len(array)
    if length == 0 :
        return False    
    else :    
        for i in range(1,length):#每个未排序数据
            if array[i]<array[i-1]:    
                mini=array[i]#给array[i]找到合适的插入位置
                index=i
                for j in range (i-1,-1,-1):#和已排序序列比较
                    if array[j] > mini:
                        array[j+1] = array[j]
                        index = j      #目前最合适的插入位置               
                    else :
                        break
                array[index]=mini#和已排序序列比较完了，将array[i]插入合适位置
        return array
            
    
