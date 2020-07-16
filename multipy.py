class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        M = len(num1)
        N = len(num2)

        res = [ 0 ] * (M + N)
        print(res)

        for i in range(M - 1,-1, -1):
            for j in range(N - 1, -1, -1):
                n1 = int(num1[i])
                n2 = int(num2[j]) 

                summ = n1 * n2 + res[i + j + 1]
                res[i + j + 1] = summ % 10
                res[i + j] += summ // 10
        
        return ''.join(map(str,res))
print( Solution().multiply("2","3"))