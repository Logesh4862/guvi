n,s=map(int,raw_input().split())
pow=1
if(s==0):
  print(1)
elif n==0:
  print(0)
else:
  for i in range(s):
    pow=pow*n
  print(pow)
