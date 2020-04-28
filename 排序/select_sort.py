def select_sort(data):
    for i in range(len(data)-1):  # 被选择排序的数是 n-1 个
        for j in range(i+1,len(data)): # 找第 i 个数后面的最小值与第 i 个数作比较
            if data[j]<data[i]:
                data[j],data[i]=data[i],data[j]
