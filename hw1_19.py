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

def pla50(w, inputs):
  loop = 1
  # success = False
  changes = 0
  print "pla start....."

  while changes < 50:
    # print ("round", loop)  
    # result = []    
        
    for row in inputs:        
      x = row[:(row.size-1)]
      y = row[(row.size-1)]

      dotp = w.dot(x)      

      if dotp > 0 and y <0: 
        w = w - x*0.5
        changes +=1
      elif dotp <=0 and y >0:
        w = w + x*0.5 
        changes +=1        
      
      if changes > 50:
        break;
      
    loop = loop + 1;
    # print ("loop: changes", loop, changes)
  
  verifyData = processInput("hw1_18_test.dat")
  errors = 0

  i = 0
  for row in verifyData:
    i += 1
    # print row
    x = row[:(row.size-1)]
    y = row[(row.size-1)]
    dotp = w.dot(x) 

    if dotp*y <0:
      errors +=1

  # print (errors, i)    
  return float(errors)/float(i)
      

def runPla50():
  w = np.array([0,0,0,0,0])  
  inputs = processInput('hw1_18_train.dat')  
  records = []
  for x in range(2000):    
    np.random.shuffle(inputs)
    records.append(pla50(w, inputs))
  # print records
  print np.average(np.array(records))


if __name__ == "__main__":  
  runPla50()
