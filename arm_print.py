def arm(n):
  temp=n
  sum=0
  while temp>0:
    sum=(int((temp%10))**3)+sum
    #print(sum)
    temp=int(temp/10)
    #print(sum)
  if sum==n:
    print(n)
  else:
    pass
  
  
x,y=map(int,input().split(" "))
for i in range(x,y):
  arm(i)
