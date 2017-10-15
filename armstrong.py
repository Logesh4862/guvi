n=int(input())
temp=n
sum=0
while temp>0:
  sum=(int((temp%10))**3)+sum
  print(sum)
  temp=int(temp/10)
#print(sum)
if sum==n:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")
