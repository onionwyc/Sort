# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:34:23 2018

@author: onion
"""

#冒泡排序
#==============================================================================
# 冒泡排序原理，重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 默认从小到大（想把大的放到最后，所以从第一位开始比较，每次都与下一位比）
# 步骤：
# 
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
#==============================================================================
# 最差版
def BubbleSort1(array):
    length = len(array)
    if length == 0 :
        return False
    else :
        for i in range(length):#总共需要遍历length次,第一次排完后，最大的被排到了末位
            for j in range (1,length-i):
                if array[j-1] > array[j]:
                    array[j-1],array[j] = array[j],array[j-1]
        return array
 # 最差版，排序次数最多，如果中途就已经排好顺序，则没有必要在进行排序。
 #即（某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了，用一个标记记录这个状态即可。）           

# 优化版1
def BubbleSort2(array):
    length = len(array)
    if length == 0 :
        return False
    else :
        for i in range(length):#总共需要比较length次,第一次排完后，最大的被排到了末位
            m = 0 #标记,记录交换位置的次数
            for j in range (1,length-i):            
                if array[j-1] > array[j]:
                    m+=1
                    array[j-1],array[j] = array[j],array[j-1]
            if m == 0:#此次排序没有交换位置，说明已经排序好，退出即可
                break                  
        return array
    
## 优化版2==============================================================================
#  记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。
#  因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。  
def BubbleSort3(array):
    length = len(array)
    
    if length == 0 :
        return False
    
    else :
        zone = length #循环的范围，初始值length
        for i in range(length):#总共需要比较length次,第一次排完后，最大的被排到了末位
            m = 0 #标记,记录交换位置的次数 
            for j in range (1,zone):            
                if array[j-1] > array[j]:
                    m += 1    
                    array[j-1],array[j] = array[j],array[j-1]
                zone = j#记录最后交换的位置
            if m == 0:#此次排序没有交换位置，说明已经排序好，退出即可
                break                  
        return array
    
