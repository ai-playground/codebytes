import heapq
import logging as log


if __name__ == "__main__":
    #set logging
    log.basicConfig(level=log.DEBUG)
    #create a seed list
    L = [(0,"zero"), (1,"one"), (2,"two"), (3,"three"), (-1,"negative one")]
    log.info("\nseed list = {}".format(L))
    
    #create a heap
    heapq.heapify(L)
    log.info("\nheap created = {}".format(L))
    
    e = (-2,"negative two")
    heapq.heappush(L,e)
    log.info("\nheap after pushing one element = {}".format(L))
    

    b = heapq.heappop(L)
    log.info("\nheap after popping one element = {}\nThe element popped is {}".format(L,b))
    
    a =(-3,"negative three")
    c = heapq.heappushpop(L,a)
    log.info("\nheap after pushing one element and popping one element = {}\n \
        The element popped is {}".format(L,c))

    