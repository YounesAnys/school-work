import random

def perform_test():
      '''takes user input of either 0 or 1 to determine what set of functions to perform, using
      an in statement to separate the separate functions.
      Then uses another user input to figure out how many functions to do, placing that number
      within a for loop range, and using the imported random dot operators to come up
      with random one-digit integers to create a question. If the answer matches what the
      question SHOULD equal to, then a point is given to the 'correct'
      counter, which is a variable, otherwise it prints the correct answer.
      In the end, the number of correct answers is divided by the number of questions that were
      initially requested, and it provides a score. Based on the provided score, the
      user is then given a message about what they should do as a next step, after this practice.'''
      
      OpeningMessage = 'Hello and welcome to the arithmetic operations assistant. \n With this tool, learning addition and multiplication has never been easier!'
      print (OpeningMessage)
      addORMul = input('Please select which operations you\'d like to work with. \n Inputting 0 gives addition questions, whereas 1 gives multiplcation questions: ')
      if addORMul == ('0'):
            print ('You\'ve selected addition!')
            numques = input('Please type in how many questions you\'d like to work with today. ')
            numquesint = int(numques)
            print ('You have selected to work with',  numquesint, 'questions today. \n Let us now begin.')
            #Now we have addition selected, as well as number of questions.
            #Now we can set the range for how many questions are generated.
            correct = 0
            for test in range(numquesint):
                  intA = random.randint(1,9)
                  intB = random.randint(1,9)
                  question = int(input(str(intA) + '+' + str(intB) + '= '))
                  if question == (intA + intB):
                        correct = correct + 1
                  else:
                        print('Incorrect. The correct answer is', intA + intB)
            FinalResultPercent = float((correct/numquesint)*100)
            if FinalResultPercent >= 80:
                  resultstring = 'Well done! Congratulations!'
            elif FinalResultPercent >= 60 and FinalResultPercent <80:
                  resultstring = 'Not too bad, but please study and practice some more.'
            else:
                  resultstring = 'Please study more and ask your teacher for help'
      if addORMul == ('1'):
            print ('You\'ve selected multiplication!')
            numques = input('Please type in how many questions you\'d like to work with today. ')
            numquesint = int(numques)           
            print ('You have selected to work with',  numquesint, 'questions today. \n Let us now begin.')
            #Now we have multiplication selected, as well as number of questions.
            #Now we can set the range for how many questions are generated.
            correct = 0
            for test in range(numquesint):
                  intA = random.randint(1,9)
                  intB = random.randint(1,9)
                  question = int(input(str(intA) + '*' + str(intB) + '= '))
                  if question == (intA * intB):
                        correct = correct + 1
                  else:
                        print('Incorrect. The correct answer is', intA * intB)
            FinalResultPercent = float((correct/numquesint)*100)
            if FinalResultPercent >= 80:
                  resultstring = 'Well done! Congratulations!'
            elif FinalResultPercent >= 60 and FinalResultPercent <80:
                  resultstring = 'Not too bad, but please study and practice some more.'
            else:
                  resultstring = 'Please study more and ask your teacher for help'
      return(resultstring)

perform_test()




            

