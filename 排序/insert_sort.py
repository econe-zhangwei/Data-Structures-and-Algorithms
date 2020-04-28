def insert_sort(data):
    for i in range(1,len(data)):  # 第一个数已经有序，不需要重新排
        tmp = data[i]   # 从第二个数开始作为需要插入的暂存数
        k = i-1      # 被比较数的下标
        '''整个while循环实现的功能就是把符合条件的位置之后所有数据往后挪一位'''
        while k>=0 & tmp < data[k]:       # 符合条件开始插入
            data[k+1] = data[k]    # 被比较数据向后移动一位
            k -= 1
        data[k+1] = tmp    # 比较之后最小的元素放到第一个位置（后面的数已经都向后移了一位）
