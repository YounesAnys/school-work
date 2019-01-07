#ITI1120
#Assignment Number 1
#Gorji, Mahyar
#8135109

########################
#Question 1
########################

def in_or_out_square(xbot, ybot, sidelength, x, y):
      '''(number, number, number, number, number) --> (true/false)
      Function takes a pair of coordinates of the bottom left corner of a square,
      xbot, ybot, and uses a sidelength to contstruct a square and test if a query point,
      x, y, is inside that square.'''
      
      varinvalid = 'Invalid Side Length'
      varinsidetrue = str('The given query point ('+str(x)+ ' , '+str(y)+') is inside of the square.')
      varinsidesquare = ' '
      xboundary = xbot + sidelength
      yboundary = ybot + sidelength
      if sidelength < 0:
            print(varinvalid)
      elif x <= xboundary and y <= yboundary:
            varinsidesquare = 'yes'
      else:
            varinsidesquare = 'no'
      if varinsidesquare == 'yes':
            return(varinsidetrue)
      else:
            return(varinsidefalse)


########################
#Question 2
########################

def factorial(n):
      '''(integer n) --> (integer)
      Takes value (n) and completes the factorial function with it, multiplying it
      by every positive integer that comes before it'''
      
      newproduct = 1
      for i in range(n):
            newproduct = newproduct * (i+1)
      #Using for loop to distribute i to range of n, which is 0 --> n-1, and the multiplication of these will provide us with the factorial of the number.
      return(newproduct)

########################
#Question 3
########################

def strange_count(s):
      '''(String) --> (integer)
      Takes input (s) and using string dot operators to count how many instances
      of certain characters are involved with that string, raising the counter each
      time one is found, and returning the counter (which is an integer)'''
      
      counter = 0
      for char in s:
            if char in 'bcdefghijklmnopqrstuvwxyz34567':
                  counter = counter + 1
      return(counter)
#This could also be done using string.count,
#although it would be incredibly tedious
#to write s.count(sample) so many times for each occurence
#of the given alphanumerical values shown above.

########################
#Question 4
########################

def vote_percentage(results):
      '''(String) --> (float) --> (string)
      Takes the (results) and counts the instances of 'yes' and compares it to the total
      of 'yes' and 'no', returning a float, which is then converted to a string again to be
      returned'''
      
      yescounter = results.count('yes')
      nocounter = results.count('no')
      abstaincounter = results.count('abstain')
      finalpercentage = str(float(yescounter/(yescounter+nocounter)))
      return(finalpercentage)

########################
#Question 5
########################

def vote():
      '''(string) --> (float) --> (string) --> (uses a boolean) --> (string)
      Takes the user input and stores in in variable 'voting', which then runs that variable
      through the previous function, and completes question 4's function. Using
      question 4's result, it then uses if statements and boolean expressions to determine
      whether or not the result of question 4 inside question 5 meets a certain criteria,
      and afterwards, a specific string that maps from each criteria is printed'''
      
      voting = input('Enter the yes, no, abstained one by one and press enter:')
      newvotepercentage = float(vote_percentage(voting))
      if newvotepercentage == 1.0:
            print('proposal passes unanimously')
      if newvotepercentage >= 0.666 and newvotepercentage <1:
            print('The proposal passes with super majority')
      elif newvotepercentage >= 0.50 and newvotepercentage <0.666:
            print('The proposal passes with simple majority')
      elif newvotepercentage <.50:
            print('The proposal fails')

########################
#Question 6
########################

def roman():
      '''(String) --> (int) --> (string)
      Takes user input and stores it inside 'romaninput' as a string, then using string dot operators,
      the instances of each letter were counted and multiplied by their respective value as
      an integer, and lastly returned as a string, after all the integers were added up.'''
      
      romaninput = str(input('Enter a roman number using capital letters M, D, C, X, and I: '))
      romaninputM = int((romaninput.count('M'))*1000)
      romaninputD = int((romaninput.count('D'))*500)
      romaninputC = int((romaninput.count('C'))*100)
      romaninputX = int((romaninput.count('X'))*10)
      romaninputV = int((romaninput.count('V'))*5)
      romaninputI = int((romaninput.count('I'))*1)
      FinalRomanAnswer = str(romaninputM + romaninputD + romaninputC + romaninputX + romaninputI)
      return(FinalRomanAnswer)

########################
#Question 7
########################

def roman_v2():
      '''(string) --> (integer) --> (string)
      Takes inputs as strings, and using for loops that detect the presence of a character in a
      phrase, the counters went up by one for every instance, and was then multiplied
      by their respective values and returned as a string'''
      
      Mcounter = 0
      Dcounter = 0
      Ccounter = 0
      Xcounter = 0
      Vcounter = 0
      Icounter = 0
      romaninput = str(input('Enter a roman number using capital letters M, D, C, X, and I: '))
      for char in romaninput:
            if char in 'M':
                  Mcounter = Mcounter + 1
            if char in 'D':
                  Dcounter = Dcounter + 1
            if char in 'C':
                  Ccounter = Ccounter + 1
            if char in 'X':
                  Xcounter = Xcounter + 1
            if char in 'V':
                  Vcounter = Vcounter + 1
            if char in 'I':
                  Icounter = Icounter + 1
      FinalRomanv2Answer = str(int(Mcounter *1000) + int(Dcounter *500) + int(Ccounter *100) + int(Xcounter*10) + int(Vcounter * 5) + int(Icounter *1))
      return (FinalRomanv2Answer)

########################
#Question 8
########################

def emphasize(s):
      '''(string) --> (string)
      Takes the given string 's' and finds its length, using that length as the range
      for a for loop. Later, a blank variable was created as a string where the
      compounding data would be written, and was later returned as a string'''
      
      lengthS = len(s)
      stringvar = ' '
      for i in range(lengthS):
            stringvar = stringvar + s[i] + ' '
      return (stringvar)

########################
#Question 9
########################

