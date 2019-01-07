def is_prime(n):
     '''(number)->bool
     Returns True if a given positive number n>=2  is prime and false otherwise
     Precondition n>=2
     '''
     for divisor in range(2, n//2+1):
          if n % divisor == 0:
               return False
     return True

for i in range(2,15):
     print(i, "is", is_prime(i))
 
       
