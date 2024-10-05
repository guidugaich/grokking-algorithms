def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = sorted([i for i in (nums1 + nums2) if i != 0])
    

print(sorted(merge([1,2,3,0,0,0], 3, [2,5,6], 3)))