class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=k*threshold
        window=0
        for i in range(k):
            window+=arr[i]
        c=0
        if window>=target:
            c+=1
        for i in range(k,len(arr)):
            window+=arr[i]
            window-=arr[i-k]
            if window>=target:
                c+=1
        return c
