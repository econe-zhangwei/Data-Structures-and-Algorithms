def shell_sort(data):
    size = len(data)
    gap = size // 2     # gap 为同组数内的间距

    while gap>0:   # 控制循环次数，分组数必须是正整数
        '''整个for循环实现插入排序的功能，与插排的区别就是把1变成gap（间隔不同）'''
        for i in range(gap,size):
            tmp = data[i]
            k = i-gap
            while k>=0 & tmp<data[k]:
                data[k+gap] = data[k]
                k-=gap
            data[k+gap]=tmp
        gap //= 2
