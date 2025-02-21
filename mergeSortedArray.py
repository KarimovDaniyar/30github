class Solution(object):
    def merge(self, nums1, m, nums2, n):
        A = m-1 # последнее число в 1 массиве (не нулевое)
        B = n-1 # последнее число во 2 массиве 
        C = m+n-1 # индекс последнего числа в 1 массиве
        while B >= 0 and A >= 0:
            if (nums1[A]>nums2[B]):
                nums1[C] = nums1[A]
                A-=1
            else:
                nums1[C] = nums2[B]
                B-=1
            C-=1
        while B >= 0:
            nums1[C] = nums2[B]
            C-=1
            B-=1 
        return nums1

a = Solution()
print(a.merge([1,2,3,0,0,0],3,[2,3,6],3))