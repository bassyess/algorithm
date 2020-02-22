'''
973.最接近远点的K个点
思路：采用分治思想，随机选择一个元素x，将数组分为大于x和小于x两个部分，与快排中选择关键元素方法类似。
'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def partition(nums, left, right):
            midval = dist(left)
            mid = nums[left]
            while left < right:
                while left < right and dist(right) > midval:
                    right -= 1
                nums[left] = nums[right]
                while left < right and dist(left) <= midval:
                    left += 1
                nums[right] = nums[left]
            nums[left] = mid
            return left

        left, right = 0, len(points) - 1
        while left < right:
            midIndex = partition(points, left, right)
            if midIndex == K:
                break
            elif midIndex < K:
                left = midIndex + 1
            else:
                right = midIndex - 1
        return points[:K]