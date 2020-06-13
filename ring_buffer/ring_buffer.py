class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.queue = []

    def append(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            if len(self.queue) == self.capacity:
                self.queue.pop()
                self.queue.append(item)
                
    def get(self):
        return self.queue


# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is 
# full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history information, 
# where you typically want to store information up until it reaches a certain age, 
# after which you don't care about it anymore and don't mind seeing it overwritten by newer data.



# def sum_to(n):
#     """ Return the sum of 1+2+3 ... n """
#     ss  = 0
#     v = 1
#     while v <= n:
#         ss = ss + v
#         v = v + 1
#     return ss

# # For your test suite
# test(sum_to(4) == 10)
# test(sum_to(1000) == 500500)