def merge_sort(data_list):
    
    '''1. merge()函数的作用是：把两个已经排好序的数据列表合并成一个排好序的数据列表'''
    def merge(data_list1, data_list2):
            data=[]    # 用来存放排好序的数据
            index1=index2=0    # 对两个列表的数据分别操作
            data_list1.append(99999), data_list2.append(99999) # 为了给数据列表增加长度范围，否则index1和index2会出现一次超范围
            for i in range(len(data_list1)+len(data_list2)-2): # 减去没有意义的循环 
                if data_list1[index1] <= data_list2[index2]:
                    data.append(data_list1[index1])
                    index1 += 1

                else:
                    data.append(data_list2[index2])
                    index2 += 1

            return data
    
    '''2. 把数据列表不断的切分'''
    mid = len(data_list) // 2     # （二分法）每次从靠近中间的位置把数据列表分成两个部分
    
    '''3. 递归调用merge()函数来排序切分好的数据列表'''
    if len(data_list) <= 1:     # 为了控制递归的深度，最终递归得到的就是单个数据
        return data_list
    return merge(merge_sort(data_list[:mid]),merge_sort(data_list[mid:]))




#    """关于merge函数更巧妙的解法"""
#    '''利用神奇的pop()函数很巧妙的解决了要留下来的数据
#    如：left=[3,6]
#       result.append(left.pop(0))
#    先执行括号里面的部分：left.pop(0)导致left变成[6],而执行的结果却是要保存被删去的值[3]
#    所以最后结果就是：result=[3],left=[6]'''
#    def merge(left, right):
#        """
#        left:左边部分的数据列表
#        right:右边部分的数据列表
#        return:合并之后的数据列表
#        """
#        result = []
#        while left and right:
#            result.append((left if left[0] <= right[0] else right).pop(0))
#        return result + left + right   # 最后left和right中，一个为空，一个剩余一个最大数
