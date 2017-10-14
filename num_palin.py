temp=int(input())
n=temp
rev=0
while temp>0:
  rev=((rev*10)+(temp%10))
  temp=int(temp/10)
#print(n,rev)
if n==rev:
  print("Palindrome")
else:
  print("Not Palindrome")
