class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        coins = 0
        j = 1
        for i in range(len(piles)//3):
            coins += piles[j]
            j += 2

        return coins
        
        