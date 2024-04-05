class Solution:
    def reverseVowels(self, s: str) -> str:
        vowl = ['a','e','i','o','u','A','E','I','O','U']
        lett = [ss for ss in s]
        l = 0
        r = len(s) - 1
        
        while l<r:
            if lett[l] in vowl and lett[r] in vowl:
                lett[l],lett[r] = lett[r],lett[l]
                l += 1
                r -= 1
                
            if lett[l] not in vowl:
                l += 1
            
                
            if lett[r] not in vowl:
                r -= 1
                
        return ''.join(lett)
                