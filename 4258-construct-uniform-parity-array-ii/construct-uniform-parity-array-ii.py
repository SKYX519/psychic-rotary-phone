class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # Make everything odd
        if mn % 2 == 1:
            return True

        # Make everything even
        # If minimum is even, odd numbers cannot become even
        # unless there is a smaller odd number, which is impossible.
        for x in nums1:
            if x % 2 == 1:
                return False

        return True