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

def checkErrors(w, inputs):
  errors = 0

  i = 0
  for row in inputs:
    i += 1
    # print row
    x = row[:(row.size-1)]
    y = row[(row.size-1)]
    dotp = w.dot(x) 

    if dotp*y <=0:
      errors +=1

  #print (errors, i)    
  return (errors, i)  

def pocket50(w, inputs): 
  changes = 0
  pocket_changes = 0
  print "pocket start....."

  pocket_w = w
  pla_w = w

  # consecutive correct
  #pla_run = 0
  #pocket_run = 0

  # total correct
  pla_num = 0
  pocket_num = 0

  loop = 0

  while changes < 50:

    np.random.shuffle(inputs)
    for row in inputs:   
      # print row
      x = row[:(row.size-1)]
      y = row[(row.size-1)]
      dotp = pla_w.dot(x)  

      #print ((changes, pocket_changes), (pla_run, pocket_run), (pla_num, pocket_num))

      if dotp > 0 and y <0: 
        pla_w = pla_w - x
        changes +=1
        #pla_run = 0
        # print "pla update"
      elif dotp <=0 and y >0:
        pla_w = pla_w + x
        changes +=1
        #pla_run = 0
        # print "pla update"
      else: # correct, see if pocket_w needs to be updated
        #pla_run += 1

        #if pla_run > pocket_run:
        error, total = checkErrors(pla_w, inputs)
        pla_num = total - error
        if pla_num > pocket_num:
          print (loop, "pocket update",  error, pla_num, pocket_num)
          pocket_changes += 1
          pocket_w = pla_w
          #pocket_run = pla_run
          pocket_num = pla_num          
        #else:  
          #print (loop, "pocket skip",  error, pla_num, pocket_num)
          
        if error == 0:          
          changes = 50;
          break;
    
    loop += 1     

  verifyData = processInput("hw1_18_test.dat")
  final_error, final_count = checkErrors(pocket_w, verifyData)  
  return float(final_error)/float(final_count) 

def runPocket50():
  w = np.array([0,0,0,0,0])  
  inputs = processInput('hw1_18_train.dat')  
  records = []
  for x in range(2000):    
    #np.random.shuffle(inputs)
    records.append(pocket50(w, inputs))
  print records
  print np.average(np.array(records))


if __name__ == "__main__":  
  runPocket50()
