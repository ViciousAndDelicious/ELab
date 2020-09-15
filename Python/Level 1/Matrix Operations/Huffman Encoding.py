import queue
class HuffmanNode(object):
  def __init__(self, left=None, right=None, root=None):
    self.left = left
    self.right = right
    self.root = root
    
  def children(self):	
    return((self.left, self.right))

a=input()
b=input()
c=input()
d=c.split()
freq=[]
freq1=[]

l1=[]
l2=[eval(x) for x in d]

for x in range(len(b)):
  l1.append(b[x])

for x in range(len(l1)):
  freq1.append([])
  for y in range(0,1):
    freq1[x].append(l2[x])

for x in range(len(l1)):
  for y in range(0,1):
    freq1[x].append(l1[x])
  freq.append(tuple(freq1[x]))

def create_tree(frequencies):
  p = queue.PriorityQueue()
  for value in frequencies:
    p.put(value)
  while p.qsize() > 1:
    l, r = p.get(), p.get()
    node = HuffmanNode(l, r)
    p.put((l[0]+r[0], node))
  return p.get()

node = create_tree(freq)

def walk_tree(node, prefix="", code={}):
  if isinstance(node[1].left[1], HuffmanNode):
    walk_tree(node[1].left,prefix+"0", code)
  else:
    code[node[1].left[1]]=prefix+"0"
  if isinstance(node[1].right[1],HuffmanNode):
    walk_tree(node[1].right,prefix+"1", code)
  else:
    code[node[1].right[1]]=prefix+"1"
  return(code)

code = walk_tree(node)

l3=[]
for j in code.values():
  l3.append(eval(j))
print(l3)