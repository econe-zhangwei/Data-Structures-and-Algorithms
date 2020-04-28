# 方法一
def counting_sort(alist):
    if len(alist) <= 1: return
    
    counts = [0] * (max(alist) + 1)   # 初始化计数序列
    for num in alist:
        counts[num] += 1   # 如上图的最下面数据
    
    result = []
    for i in range(1, len(counts)):
        result.extend( [i] * counts[i] )   # 以index为单个列表，value作为列表中元素的个数，不断拓展列表
    
    return result





# 方法二
def counting_sort(alist):
    if len(alist) <= 1: return
    
    counts = [0] * (max(alist) + 1)   # 初始化计数序列
    for num in alist:
        counts[num] += 1   # 如上图的最下面数据
    
    result = [0] * len(alist)
    for num in reversed(alist):
        index = counts[num] - 1
        result[index] = num
        counts[num] -= 1
    
    return result
