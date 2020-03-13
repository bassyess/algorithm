'''
347. 前k个高频元素
思路1：字典存储元素次数，排序找出前k个元素
思路2：字典存储元素次数，建立大小为k的最小堆，找出前k个元素
'''
def topKFreqI(nums, k):
    freq_count = {}
    for num in nums:
        freq_count[num] = freq_count.get(num, 0)+1
    freq_list = sorted(freq_count.items(), key=lambda x:x[1], reverse=True)
    res = []
    for i in range(k):
        res.append(freq_list[i][0])
    return res

def topKFreqII(nums, k):
    import heapq
    freq_count = {}
    for num in nums:
        freq_count[num] = freq_count.get(num, 0) + 1
    p = []
    for i, counts in freq_count.items():
        heapq.heappush(p, (counts, i))
    return [i[1] for i in heapq.nlargest(k, p)]



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print(topKFreqII(nums, 2))
