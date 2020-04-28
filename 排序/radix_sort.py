def radix_sort(data):
    radix = 1       # 从个位开始，可以实现每位数上的比较
    max_digit_length = len(str(max(data)))       # 最大数的位数长度
    length = 0
    
    while length < max_digit_length:
        result=[]          # 每轮位数比较之后的总列表
        tmp = [[] for _ in range(10)]        # 设置一行十列的空数组（‘[]’也可写成‘list()’）

        for element in data:         # 遍历出序列中的所有数,并按第k位放入不同的列表中
            k = element // radix % 10
            tmp[k].append(element)

        for i in range(10):result += tmp[i]        # 按位数排好的列表整合到一个列表中
        data = result
        radix *= 10
        length += 1
    return data
