class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []

        p_count=[0]*26
        window=[0]*26

        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        
        ans=[]
        l=len(p)

        for r in range(len(s)):
            window[ord(s[r])-ord('a')]+=1

            if r>=l:
                window[ord(s[r-l])-ord('a')]-=1
            if window==p_count:
                ans.append(r-l+1)

        return ans
