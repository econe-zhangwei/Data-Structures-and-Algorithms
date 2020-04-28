def bubble_sort(data):
    for i in range(len(data)-1,-1,-1):# 第一次扫描 n 个数，依次递减
        for j in range(i):
            if data[j] >= data[j+1]: #  比较相邻的两个数
                data[j],data[j+1] = data[j+1],data[j]  # 满足条件则交换数据的位置
