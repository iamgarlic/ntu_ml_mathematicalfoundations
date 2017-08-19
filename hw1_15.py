import csv
import numpy as np
import time

def stof(s):
  return float(s);

def stoi(s):
  return int(s);

def generateInputPair(row):    
  y = stoi(row[len(row)-1])
  del row[-1]
  x = ['1']
  x.extend(row)  
  transformed = map(stof, x)    
  return (np.array(transformed), y)

loop = 1
success = False
changes = 0
w = np.array([0,0,0,0,0])

while success == False:
  print ("round", loop)  
  result = []
  index = 0
  
  with open('hw1_15_train.dat', 'rb') as train_set:
    for row in train_set:  
      index = index + 1     
      pair = generateInputPair(row.split())
      x = pair[0]
      y = pair[1]
              
      # initialize w
      # if loop == 1:        
      #   w = w + x
      #   w[0] = 0

      #print (x, y)
      #print ("weight", w)  

      dotp = w.dot(x)  
      #print (dotp, y)

      if dotp > 0 and y <0: 
        w = w - x
        result.append(1)
        #print (index, "fix weight", w)  
        #print result
      elif dotp <=0 and y >0:
        w = w + x 
        result.append(1)
        #print (index, "fix weight", w)  
        #print result
      else:
        result.append(0)
        #print (index, "pass", w)
    

      # print ("index", index)
      # print "\n\n"      
    
  check = sum(result)
  changes = changes + sum(result)
  print ("sum(result)", changes, check, result)

  if check == 0: 
    success = True;  
  loop = loop + 1;
