class Solution:
    def similarPairs(self, words: List[str]) -> int:
        uniq = [''.join(sorted(''.join(set(word)))) for word in words]
        num = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if uniq[i] == uniq[j]:
                    num += 1
        
        return num
        