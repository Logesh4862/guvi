n=int(input())
flag=0
for i in range(2,n-1):
  if n%i==0:
    flag=1
    break
  else:
    pass
if flag==0:
  print("Prime")
else:
  print("Non Prime")
