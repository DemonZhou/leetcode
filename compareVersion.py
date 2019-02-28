class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1_int = list(map(int,v1))
        v2_int = list(map(int,v2)) 
        if len(v1_int) > len(v2_int):
            for i in xrange(len(v1_int) - len(v2_int)):
                v2_int.append(0)
        if len(v2_int) > len(v1_int):
            for i in xrange(len(v2_int) - len(v1_int)):
                v1_int.append(0)
        
        for i in xrange(len(v1_int)):
            if v1_int[i] > v2_int[i]:
                return 1
            if v2_int[i] > v1_int[i]:
                return -1
        return 0
