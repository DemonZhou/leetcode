class WeightUnion(object):
    def __init__(self):
        self.parent = {}
        self.parent_div_cur = {}
    
    def find(self,x):
        if x == self.parent[x]:
            return x , self.parent_div_cur[x]
        else:
            root , root_div_parent = self.find(self.parent[x])
            self.parent[x] = root
            self.parent_div_cur[x] = root_div_parent * self.parent_div_cur[x]
            return self.parent[x] , self.parent_div_cur[x]

    def union(self, x, y, x_div_y):
        if x not in self.parent:
            self.parent[x] = x
            self.parent_div_cur[x] = 1.0
        if y not in self.parent:
            self.parent[y] = y
            self.parent_div_cur[y] = 1.0

        root_x, root_x_div_x = self.find(x)
        root_y, root_y_div_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x
            self.parent_div_cur[root_y] = root_x_div_x / root_y_div_y * x_div_y
        
    def calc(self,x ,y):
        if x not in self.parent or y not in self.parent:
            return -1.0
        if x == y:
            return 1.0
        else:
            root_x, root_x_div_x = self.find(x)
            root_y, root_y_div_y = self.find(y)

            if root_x != root_y:
                return -1.0
            return root_y_div_y / root_x_div_x
            

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        Union = WeightUnion()
        for (x,y) , x_div_y in zip(equations,values):
            Union.union(x,y ,x_div_y)
        
        res = []
        for (x,y) in queries:
            res.append(Union.calc(x,y))
        return res
