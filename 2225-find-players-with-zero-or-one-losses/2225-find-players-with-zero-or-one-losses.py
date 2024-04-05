class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        
        one_loss = []
        zero_loss = []
        
        for i in range(len(matches)):
            if matches[i][0] not in d:
                d[matches[i][0]] = 0
                
            if matches[i][1] in d:
                d[matches[i][1]] += 1
                
            if matches[i][1] not in d:
                d[matches[i][1]] = 1
                
            
        for k,v in d.items():
            if d[k] == 0:
                zero_loss.append(k)
            elif d[k] == 1:
                one_loss.append(k)
                
        one_loss.sort()
        zero_loss.sort()
            
                
        return [zero_loss,one_loss]
            