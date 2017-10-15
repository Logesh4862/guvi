def prime(n):
  p=1
  for i in range(2,n):
    if n%i==0:
      p=0
      break
    else:
      pass
  if p==1:
    return True
  else:
    return False
    

n,m=map(int,input().split(" "))
#print(n,m)
for j in range(n,m):
  if prime(j):
    print(j,end=" ")
  else:
    pass
