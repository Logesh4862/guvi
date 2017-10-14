n=int(input())
m=int(input())
if(n%2!=0):
  for i in range(n+1,m,2):
    print(i)
else:
  for i in range(n,m,2):
    print(i)
