fn=input()
n=int(input())
file=open(fn,"w+")
for i in range (0,n):
  s=input()
  file.write('\n')
  file.write(s)
file.close()
fn=input()
file=open(fn,"r")
text=file.read()
res=len(text.split())
print('Number of words:')
print(res)