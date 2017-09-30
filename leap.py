def leap(n):
  if n%400==0 or n%4==0:
    print ("Leap Year")
  elif n%100==0:
    return ("Non Leap Year")
  else:
    return ("Non Leap Year")
n=int(input())
leap(n)
