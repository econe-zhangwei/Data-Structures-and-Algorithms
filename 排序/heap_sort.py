# 排序
def heap_sort(self, List):
    Heap.bulid_heap(List)   # 建堆
    k = len(List)
    while k > 0:
        List[0], List[k] = List[k], List[0]   # 交换顺序
        k -= 1
        self.Heap._siftdown(k)   # 堆化（自上而下）
        

# 建堆
class Heap(object):
    def __init__(self, List):
        self._size = len(List)
        self._elements = List
        self._count = 0
        
    def build_heap(self):
        for ndx in range((self._size//2), 0, -1):
            self._siftsown(ndx)
            
    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        largest = ndx
        if (left < self._count and
            self._elements[left] >= self._elements[largest] and
            self._elements[left] >= self._elements[right]):     
            largest = left
        elif right < self._count and self._elements(right) >= self._elements(largest):
            largest = right
        if largest != ndx:
            self._elements[largest], self._elements[ndx] = self._elements[ndx], self._elements[largest]
            self._siftdown(largest)      
