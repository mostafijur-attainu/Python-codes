# Implient Queues using stacks
#Answer:-
class MyQueue(object):
    
    def _init_(self):
        self.l1 = []
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        
        self.l1.append(x)
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if self.empty():
            return
        x = self.l1[0]
        self.l1.pop(0)
        return x
            
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """  
    def peek(self):
        if self.empty():
            return
        return self.l1[0]
    
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        return len(self.l1) == 0
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
if _name_ == "_main_":
    sol = MyQueue()
    print(sol.push(1))
    print(sol.push(2))
    print(sol.push(3))
    print(sol.peek())
    print(sol.pop())
    print(sol.empty())
