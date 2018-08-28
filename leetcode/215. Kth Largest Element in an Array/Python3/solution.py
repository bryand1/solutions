class Solution:
    def merge(self, arr, lo, mid, hi):
        n1 = mid - lo + 1
        n2 = hi - mid
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = arr[lo + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]
        k = lo
        i = 0
        j = 0
        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergesort(self, arr, lo, hi):
        if lo < hi:
            mid = lo + (hi - lo) // 2
            self.mergesort(arr, lo, mid)
            self.mergesort(arr, mid + 1, hi)
            self.merge(arr, lo, mid, hi)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.mergesort(nums, 0, len(nums) - 1)
        return nums[-k]

