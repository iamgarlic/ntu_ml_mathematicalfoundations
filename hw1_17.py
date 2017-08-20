import csv
import numpy as np
import time

def stof(s):
  return float(s);

def stoi(s):
  return int(s);

def generateInputArray(row):    
  x = ['1']
  x.extend(row)  
  transformed = map(stof, x)    
  return np.array(transformed)

def processInput(filename):
  inputs = []
  with open(filename, 'rb') as train_set:
    for row in train_set:  
      inputs.append(generateInputArray(row.split()))
  return np.array(inputs)

def pla(w, inputs):
  loop = 1
  success = False
  changes = 0
  print "pla start....."

  while success == False:
    # print ("round", loop)  
    result = []    
        
    for row in inputs:           
      x = row[:(row.size-1)]
      y = row[(row.size-1)]

      dotp = w.dot(x)      

      if dotp > 0 and y <0: 
        w = w - x*0.5
        result.append(1)
      elif dotp <=0 and y >0:
        w = w + x*0.5 
        result.append(1)        
      else:
        result.append(0)    
      
    check = sum(result)
    changes = changes + sum(result)
    # print ("sum(result)", changes, check, result)
    
    if check == 0: 
      print ("sum(result)", loop, changes)
      success = True; 
      return changes 
    loop = loop + 1;

def runPLA():
  w = np.array([0,0,0,0,0])  
  inputs = processInput('hw1_15_train.dat')  
  records = []
  for x in range(2000):    
    np.random.shuffle(inputs)
    records.append(pla(w, inputs))
  # print records
  print np.average(np.array(records))


if __name__ == "__main__":  
  runPLA()
