class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        hash_t={}
        for char in t:
            hash_t[char]= hash_t.get(char,0)+1

        window_counts={}

        #need is the number of unique characters in t
        need = len(hash_t)
        have = 0

        #now we keep track of the minimum substring found
        min_len = float("inf")
        min_window= ""

        #now we expand r
        l = 0
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char,0) +1

            #check if the current character satisfies its count requirement in hash_t
            if char in hash_t and window_counts[char] == hash_t[char]:
                have += 1
            while have == need:
                if (r-l+1) < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                # Remove the character at `l` from our window and move `l` forward
                left_char = s[l]
                window_counts[left_char] -= 1

                if left_char in hash_t and window_counts[left_char] < hash_t[left_char]:
                    have -=1
                l+=1
        return min_window