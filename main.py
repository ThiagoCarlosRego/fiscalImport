
from Report.Efd import EfdClass as Efd
from Mapping.CValues import ValuesClass as Value
from pymongo import MongoClient
from Mapping.Encoder import MyEncoder as Encoder
import uuid


print("start")
value = Value("0000",[])
strFile = "./files/EFDoriginal-out2020.txt"
#
try:
  print("Parameters")
  row = 0
  efd = Efd()
  headers = efd.Headers
  dbMongoCli = MongoClient('localhost', 27017)
  dbFiscal = dbMongoCli["DbFiscal"] 
  dbValues = dbFiscal["Values"]
  jsonValues = []

  print("start ready file")
  with open(strFile) as f: # read file
    for line in f:
      break # remove to import
      #print("############################################################################ LINE " + str(row) + " ############################################################################ ")
      print("line => " + str(row) + " : " +line )
      values = line.split("|")  #Values line
      objectValue = Value(id=values[1], columns=values)
      dbValues.insert({
        "_id" : str(uuid.uuid4()),
        "id" : objectValue.GetId(),
        "columns" : objectValue.GetColumns()
      })
      row = row +1
      

  x = dbValues.find_one()
  print(x)
  print("Imported")

          
except FileNotFoundError as e:
  print(e)
except Exception as e:  
  print("An exception occurred:")
  print(e)


