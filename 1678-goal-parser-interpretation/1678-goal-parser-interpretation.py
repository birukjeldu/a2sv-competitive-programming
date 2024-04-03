class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        left = 0
        right = 1
        word = ''
        while right <= len(command):
            if command[left] == '(' and command[right] == ')':
                word += 'o'
            
            elif command[left] == 'a':
                word += 'al'
                
            elif command[left] == 'G':
                word += 'G'
                
            left += 1
            right = left + 1
            
        return word