# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[int(len(nums1)/2)]
        else:
            return (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1]) / 2

def main():
    solution = Solution()
    print(solution.findMedianSortedArrays([],[2]))

if __name__ == '__main__':
    main()