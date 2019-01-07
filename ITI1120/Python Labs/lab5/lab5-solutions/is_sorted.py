def is_sorted(l):
     '''(list)->bool
       Returns True if list l is sorted from smallest to largest number,
       False otherwise
       Precondition: Elements of l are numbers'''

     if(len(l)<2):
         return True
     
     # check that the difference between consecutive numbers is
     # equal to the difference between the first two numbers
     
     for i in range(0, len(l)-1):
        if l[i+1] - l[i] < 0:
            return False
     return True
