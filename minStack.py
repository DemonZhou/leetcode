class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            if x >=  self.minstack[-1]:
                self.minstack.append(x)
            elif x <= self.minstack[0]:
                self.minstack.insert(0,x)
            else:
                for i in range(1,len(self.minstack)):
                    if x <= self.minstack[i]:
                        self.minstack.insert(i,x)
                        break

    def pop(self):
        """
        :rtype: None
        """
        nx = self.stack.pop()
        self.minstack.remove(nx)


    def top(self):
        """
        :rtype: int
        """
        return None if not self.stack else self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return None if not self.minstack else self.minstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()