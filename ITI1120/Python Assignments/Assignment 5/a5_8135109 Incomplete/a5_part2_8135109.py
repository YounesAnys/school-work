#Assignment 5 part 2
#Mahyar Gorji
#8135109
#ITI1120

#Main

#2a)
def largest_two(a):
      '''Sorts given list 'a' in ascending order, and takes the
      last two entries and sums them.'''
      a.sort()
      value = (a[-1] + a[-2])
      return(value)

#2b)
def smallest_half(a):
      '''Takes given list 'a' and int. divides it in 2.
      Computes sum of first half.'''
      a.sort()
      b = len(a)//2
      c = b-1
      value = 0
      for i in range(a[c]):
            value = value + a[i]
      return (value)

#2c)
def median(a):
    a.sort()
    lenlist = len(a)
    index = (lenlist - 1) // 2
    if (lenlist % 2):
        return a[index]
    else:
        return (a[index] + a[index + 1])/2.0

#2d)
def at_least_third(a):
      #a.sort()
      #occurrences = len(a)//3
      #times = collections.Counter(a)
      #times.split( )
      #print(times)
      b = [x for x in a if a.count(x) == (len(a)//3)]
      if len(b)==0:
            return None
      elif len(b)==(len(a)//3):
            c = list(set(b))
            d = c[0]
            return d

#2e)
def triple_sum(a,x):
      for i in range(len(a)):
            for j in range(len(a)):
                  for k in range(len(a)):
                        if (a[i] + a[j] + a[k]) == x:
                              return True
      return False




