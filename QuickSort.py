# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:10:50 2018

@author: onion
"""
#==============================================================================
#快速排序快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，而且快排采用了分治法的思想，
#所以在很多笔试面试中能经常看到快排的影子。可见掌握快排的重要性。

# 从数列中挑出一个元素作为基准数。
# 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
# 再对左右区间递归执行第二步，直至各区间只有一个数。
#==============================================================================
def QuickSort(array):
    length = len(array)
    if length == 0 :
        return False    
    else :    
        center=array[int(length/2)]#取中间的作为基准元素
        
                     
                     
                     
class Solution:
    def addTwoNumbers(self, l1, l2):
        cur=ListNode(0)
       
        big=0
        minisum = 0
        while l1 or l2 or big:            
            minisum += l1.val+l2.val+big
            cur.next=ListNode(minisum%10)
            cur=cur.next
            big=minisum//10
           
            l1=(l1.next if l1.next else 0)
            l2=(l2.next if l2.next else 0)
        return cur.next                    