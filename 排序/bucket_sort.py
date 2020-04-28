def bucket_sort(alist, bucketsize):
    """
    alist: 输入列表
    bucketsize: 每个桶的大小
    """
    # 先找出list中的最大值和最小值，方便确定桶的数量
    # 当然直接用 max()和 min()函数其实也不影响时间复杂度
    minvalue = alsit[0]
    maxvalue = alist[1]
    for element in alist:
        if element < minvalue:
            minvalue = element
        else: maxvalue = element
    
    bucketcount = (maxvalue - minvalue + 1) // bucketsize + 1   # 桶的数量
    bucket_lists = list([] for _ in range(bucketcount))   # 初始化每个桶
    
    # 把数据分到这些有序的桶里
    for i in alist:
        bucket_index = (i - minvalue) // bucketsize 
        bucket_lists[bucket_index].append(i)
        
    # 对每个桶用快排处理(上面快排的方法二)
    for bucket in bucket_lists:
        quick_sort(bucket, 0, len(bucket)-1)
        
    # 合并数据
    result = []
    for bucket in bucket_lists:
        if len(bucket) != 0:
            result.extend(bucket)
    
    return result
