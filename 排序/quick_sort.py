# 方法一
def quick_sort(data):
    if len(data) <= 1:   # 只有一个数时就返回，同时作为限制递归的条件，否则会出现pop了一个空列表
        return data
    else:
        pivot = data.pop()    # 把最后一个数作为基准数。data.pop() 即 data[len(data)-1]
        left_list, right_left = [],[]    # 不可以写作left_list=right_left=[]
        for element in data:  # 遍历所有数据都和基准数据做比较，小的放左边，大的放右边
            if element < pivot:
                left_list.append(element)
            else:
                right_left.append(element)
        '''返回结果应该是：left_list + [pivot] + right_left，左右两个列表加上中间的基准参考值
        但需要递归计算 left_list 和 right_left ,所以实际返回值如下'''
        return quick_sort(left_list) + [pivot] + quick_sort(right_left)





# 方法二
def partition(data, p, r):   # 分区函数
    """
    data:待排序数组
    p:data第一个元素的index
    r:data末尾元素的index"""
    pivot = data[p]
    i = p + 1
    for j in range(i, r+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i-1], pivot = pivot, data[i-1]
    return i-1   # 即pivot的下标

def quick_sort(data, fist_index, last_index):
    pivot_index = partition(data, first_index, last_index)
    # 递归左边和右边数组
    quick_sort(data, first_index, pivot_index-1)
    quick_sort(data, pivot_index+1, last_index)




# 方法三
def quick_sort(data,left_index,right_index):
    '''    
    data：输入的数据序列
    left_index：序列最左边的index
    right_index：序列最右边的index
    '''
    # 递归函数，后面两个参数必须是变量，不能写成 [0, len(data)-1]
    i,j = left_index,right_index
    
    # 注：if语句不能放在pivot=data[i]语句之后。
    # 当序列只有一个数时，右序列递归得到的i=2，会导致超范围。但先执行if语句就直接返回data。
    if i >= j:
        return data
    pivot = data[i]
    
    while i < j:
        if data[j] < pivot:
            data[j],data[i] = data[i],data[j]
            i += 1
        elif data[i] > pivot:
            data[i],data[j] = data[j],data[i]
            j -= 1
    
    quick_sort(data,left_index,i-1)
    quick_sort(data,i+1,right_index)
    
    return data





# 方法四
def quick_sort(data,size,i,j):
    if i < j:
        
        pivot = data[i]
        left_index = i+1
        while data[left_index] < pivot:
            if left_index +1 > size:
                break
            left_index += 1
        
        right_index = j
        while data[right_index] > pivot:
            right_index -= 1
        while left_index < right_index:
            data[left_index],data[right_index] = data[right_index],data[left_index]
            left_index += 1
            while data[left_index] < pivot:
                left_index += 1
            right_index = j
            while data[right_index] > pivot:
                right_index -= 1
        pivot,data[right_index] = data[right_index],pivot
        
        quick_sort(data,size,i,right_index-1)
        quick_sort(data,size,right_index+1,j)
        
