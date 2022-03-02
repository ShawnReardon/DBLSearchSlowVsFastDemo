from dblls import *
import time
from slowsearch import slowsearch
delayTime = 0.5
start = time.time()

myList = DoublyLinkedList()

for i in range(0, 11):
  #print(i)
  myList.push_back(i)



head = myList.head
tail = myList.tail
target = 7

def visualSearch(target, head, tail):
  lo = head
  hi = tail
  

  for i in range(myList.count):
      print(lo.data, end=" ")
      lo = lo.next


  lo = head
  print()
  for i in range(myList.count):
   time.sleep(delayTime)
   if hi == lo and hi.data == target:
      return hi.data
  

   if lo.data != target or hi.data != target:
     s = ("^" + "  "*i)
     if i == 0:
      print(i*"  " + "^"+ s.rjust((i+1)*21, " "))
     else:
      print(i*"  " + "^"+ s.rjust((20 - (i*2)), " "))

      
     
     #lo = lo.next
     
     #hi = hi.prev
     if hi.data == target:
      return hi.data
     elif lo.data == target: 
      return lo.data
     else:
       hi = hi.prev
       lo = lo.next
 
  return "Element Not Found!"



def search(target, head, tail):
  lo = head
  hi = tail
  

  for i in range(myList.count):
   time.sleep(delayTime)
   if lo.data != target:
     lo = lo.next
     
   else: 
     return lo.data
   if hi.data != target:
     hi = hi.prev
   else: 
     return hi.data
  return "Element Not Found!"

slowsearch(9, myList)
end = time.time()
print("Slow", end - start)
start = time.time()
#print(search(9, head, tail))

print("Visual Faster: ", visualSearch(9, head, tail))

end = time.time()
print("Faster", end - start)