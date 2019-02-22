class Solution:
    def reverse(self,start,end,s):
        i = start
        j = end
        while(i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i + 1
            j = j - 1
    
    def reverseWords(self, str: 'List[str]') -> 'None':
        """
        Do not return anything, modify str in-place instead.
        """
        self.reverse(0,len(str) - 1,str)
        start = 0
        for i in range(len(str)):
            if str[i] == " " :
                self.reverse(start,i - 1,str)
                start = i + 1
            if i == len(str) - 1 :
                self.reverse(start,i,str)
        print(str)
        


sol = Solution()
sol.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
