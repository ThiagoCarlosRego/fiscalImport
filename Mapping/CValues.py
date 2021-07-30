class ValuesClass(dict):
    def __init__(self, id, columns):
        self.id = id
        self.columns = columns
        dict.__init__(self, id=id,columns=columns)

    def GetId(self):
        return self.id
        
    def GetColumns(self):
        return self.columns