class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_list = nums1 + nums2
        total_list.sort()

        i = (len(total_list)-1) // 2
        j = i + (len(total_list)+1) % 2

        result = (total_list[i] + total_list[j]) / 2
        return result