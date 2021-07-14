from numpy import little_endian
from Mapping.Efd import EfdClass as efd

strFile = "./EFDoriginal-out2020.txt"
#

try:
  row = 0
  with open(strFile) as f: # read file
        for line in f:
            print("############################################################################ LINE " + str(row) + " ############################################################################ ")
            values = line.split("|")  #Values line
            print(len(values))
            hValues = efd.codes.get(values[1]).split(",") #get header by code
            for head in range (len(hValues)): # For each header
                print(hValues[head] + " => " + values[head+1]) # Header + value
            row = row +1
            if row >2: 
                break
            
except FileNotFoundError as e:
  print(e)
except Exception as e:  
  print("An exception occurred:")
  print(e)
  # continue  