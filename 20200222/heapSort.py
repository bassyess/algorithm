'''
堆排序
升序：大根堆，降序：小根堆
'''

# 大根堆
def heapSort(nums):
    def adjustHeap(nums, i, size):
        lchild = 2*i+1
        rchild = 2*i+2
        largest = i
        if lchild<size and nums[lchild]>nums[largest]:
            largest = lchild
        if rchild<size and nums[rchild]>nums[largest]:
            largest = rchild
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            adjustHeap(nums, largest, size)

    # 建立堆
    def buildHeap(nums, size):
        for i in range(len(nums)//2)[::-1]:  # 从倒数第一个非叶子节点开始建立大根堆
            adjustHeap(nums, i, size)        # 对所有非叶子节点进行堆的调整

    # 堆排序
    size = len(nums)
    buildHeap(nums, size)
    for i in range(len(nums))[::-1]:
        nums[0], nums[i] = nums[i], nums[0]
        adjustHeap(nums, 0, i)
    return nums

# 小根堆
def heapSort2(nums):
    def adjustHeap(nums, i, size):
        lchild = 2*i+1
        rchild = 2*i+2
        least = i
        if lchild<size and nums[lchild]<nums[least]:
            least = lchild
        if rchild<size and nums[rchild]<nums[least]:
            least = rchild
        if least!=i:
            nums[least], nums[i] = nums[i], nums[least]
            adjustHeap(nums, least, size)

    def buildHeap(nums, size):
        for i in range(len(nums)//2)[::-1]:
            adjustHeap(nums, i, size)

    size = len(nums)
    buildHeap(nums, size)
    for i in range(len(nums))[::-1]:
        nums[0], nums[i] = nums[i], nums[0]
        adjustHeap(nums, 0, i)
    return nums



if __name__=='__main__':
    print(heapSort([2,5,8,3,4,1,7]))
    print(heapSort2([2,5,8,3,4,1,7]))