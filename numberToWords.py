class Solution:
    def numberToWords(self, num: int) -> str:
        suffix = {
            0: "",
            1: " Thousand",
            2: " Million",
            3: " Billion"
        }
        step = 0 #mean it has caculated 3 * step digits
        res = ""
        if num == 0:
            return "Zero"
        while num > 0:
            t  = num % 1000
            if t != 0:
                res = " " + self.numberToWordsRaw(t) + suffix[step] + res
            num = int(num / 1000)
            step = step + 1
        res = res.strip()
        print(res)
        return res
            

    def map1(self,num:int) -> str:
        num_to_string = {
            0 : "",
            1 : "One",
            2 : "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five",
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 : "Eleven",
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
        }
        return num_to_string[num]

    def map2(self,num:int) -> str:
        num_to_string2 = {
            0 : "",
            2 : "Twenty",
            3 : "Thirty",
            4 : "Forty",
            5 : "Fifty",
            6 : "Sixty",
            7 : "Seventy",
            8 : "Eighty",
            9 : "Ninety"
        }
        return num_to_string2[num]
    


    def numberToWordsRaw(self,num:int) -> str:
        res = ""
        val = int(num / 100)
        val2 = num - val * 100
        if val != 0:
            res += self.map1(val) + " Hundred"
            if val2 > 0:
                res += " "
        if val2 < 20:
            res +=  self.map1(val2)
        else :
            res +=  self.map2(int(val2 / 10)) 
            s = self.map1(val2 % 10 )
            if s != "":
                res += " " + s
        return res

Sol = Solution()
Sol.numberToWords(50868)
        
