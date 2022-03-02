import time
delayTime = 0.5
def slowsearch(target, llist):
  head = llist.head


  for i in range(llist.count):
   time.sleep(delayTime)
   if head.data == target:
     print(head.data, "\n"+ ("^ "*i))
     print("\nFound!",target)
     break
   else:
     if i == 0:
       s= ("\n^")
     else:
       s = ""
     print(head.data, s, "\n"+ ("^ "*i), end="")
    
     head= head.next
    