'''
912.排序数组（堆排序实现）
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def adjustHeap(nums, i, size):
            lchild = 2 * i + 1
            rchild = 2 * i + 2
            largest = i
            if lchild < size and nums[lchild] > nums[largest]:
                largest = lchild
            if rchild < size and nums[rchild] > nums[largest]:
                largest = rchild
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                adjustHeap(nums, largest, size)

        def buildHeap(nums, size):
            for i in range(len(nums) // 2)[::-1]:
                adjustHeap(nums, i, size)

        size = len(nums)
        buildHeap(nums, size)
        for i in range(len(nums))[::-1]:
            nums[0], nums[i] = nums[i], nums[0]
            adjustHeap(nums, 0, i)
        return nums