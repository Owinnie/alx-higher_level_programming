#!/usr/bin/python3
"""Find peak"""

def find_peak(list_of_integers):
    """I find the peak"""
    if A == []:
        return None
    def recursive(A, left=0, right=len(A) - 1):
        """recursive function"""
        mid = (left + right) // 2
        if ((mid == 0 or A[mid - 1] <= A[mid]) and
                (mid == len(A) - 1 or A[mid + 1] <= A[mid])):
            return A[mid]
        if mid - 1 >= 0 and A[mid - 1] > A[mid]:
            return recursive(A, left, mid - 1)
        return recursive(A, mid + 1, right)
    return recursive(A)
