#Python Lab 4

#Task 1.
s1 = 'good'
s2 = 'bad'
s3 = 'silly'

#a
print (s3[2:4:1])
#c
print (s1 + s2 + s3)
#d
#e
print (10*(s1+s2+s3))
#f
lengthofe = (10*(s1+s2+s3))
print (len(lengthofe))

print('end of task 1')

#Task 2
aha = 'abcdefgh'
#a
print (aha[0:4:1])
#b
print (aha[3:6:1])
#c
print (aha[7:])
#d
print (aha[5:7:1])
#e
print (aha[3:8:1])
#f
print (aha[5:8:1])
#g
print (aha[0:7:3])
#h
print (aha[1:5:3])


#Task 3
s = '''It was the best of times, it was the worst of times;it was the age of wisdom, it was the age of foolishness;it was the epoch of belief, it was the epoch of incredulity;it was ...'''
newS = s.replace('.', ' ')
newS = newS.replace(',', ' ')
newS = newS.replace(';', ' ')
print (newS)

#lowercase
newS = s.lower()
print (newS)

#It was counter
numocc = s.count('it was')
print (numocc)

#was --> is
newS = newS.replace('was', 'is')
print (newS)


