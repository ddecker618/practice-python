import random

#A function do shuffle all the characters of a string
def shuffle(string):
  templist = list(string)
  random.shuffle(templist)
  return ''.join(templist)

  #Main program stars here
  uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
  uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
  uppercaseLetter3=chr(random.randint(65,90))
  #Generate more characters here
  #...

  #Generate a password using all the characters, in a random order
  password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 # + ....
  password = shuffle(password)

  #Output
  print(password)
