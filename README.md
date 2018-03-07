
- [x] 堆排序
- [x] 希尔排序
- [x] 快速排序
- [x] 插入排序
- [x] 直接选择排序
- [x] 冒泡排序

总结如下：

![示意图 ](http://img.blog.csdn.net/20130801171021937?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvam51X3NpbWJh/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


所有排序为从小到大;
python3。

# 一、冒泡排序 BubbleSort
介绍：

冒泡排序，如果您想把大的放到最后，所以从第一位开始比较（每次都与下一位比它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。）

步骤：

比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

优化1：最差版，排序次数最多，如果中途就已经排好顺序，则没有必要在进行排序。
 #即（某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了，用一个标记记录这个状态即可。）
优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。

# 二、选择排序 SelectionSort
介绍：

选择排序无疑是最简单直观的排序。它的工作原理如下。

步骤：

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
源代码：(python实现)

# 三、插入排序 InsertionSort

1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
重复步骤2~5。

操作过程示意图：

![示意图 ](http://wuchong.me/img/Insertion-sort-example-300px.gif)


# 四、希尔排序 ShellSort

【1】介绍：

希尔排序，也称递减增量排序算法，实质是分组插入排序。由 Donald Shell 于1959年提出。希尔排序是`非稳定排序算法`。

希尔排序的基本思想是：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

【2】例如

假设有这样一组数[ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]，如果我们以步长为5开始进行排序，我们可以通过将这列表放在有5列的表中来更好地描述算法，这样他们就应该看起来是这样：

    13 14 94 33 82
    25 59 94 65 23
    45 27 73 25 39
    10

然后我们对每列进行排序：

    10 14 73 25 23
    13 27 94 33 39
    25 59 94 65 82
    45

将上述四行数字，依序接在一起时我们得到：`[ 10 14 73 25 23 13 27 94 33 39 25 59 94 65 82 45 ]`。这时10已经移至正确位置了，然后再以3为步长进行排序：

    10 14 73
    25 23 13
    27 94 33
    39 25 59
    94 65 82
    45

排序之后变为：

    10 14 13
    25 23 33
    27 25 59
    39 65 73
    45 94 82
    94

最后以1步长进行排序（此时就是简单的插入排序了）。