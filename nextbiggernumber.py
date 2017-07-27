def next_bigger(n):
    bigger = []
    ln = list(reversed(list(str(n))))
    biggest = sorted(ln)
    if ln == biggest:
       return -1
    else:
      for i in range(len(ln)-1):
          if ln[i] > ln[i+1]:
          # sorted the from 0 to i
             bigger.extend(sorted(ln[:i+1], reverse = True))
             index = i+1
             break  
      bigger.extend(ln[i+1:])
      for i in range(index,-1,-1):
          if bigger[index] < bigger[i]:           
             bigger[i], bigger[index] = bigger[index], bigger[i]            
             break
      return int("".join((reversed(bigger))))
