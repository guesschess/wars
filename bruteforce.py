# brute-force search for "next bigger number with the same digits"
from datetime import datetime
def next_bigger(n):
    start = datetime.now()
    i,ss = n, sorted(str(n))
    if list(str(n)) == sorted(str(n), reverse = True):
       return -1
    while True:
       i +=1
       if sorted(str(i)) == ss and i != n:
           print datetime.now() - start
           return i
