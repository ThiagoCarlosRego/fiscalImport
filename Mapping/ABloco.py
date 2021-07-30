class BlocoClass(dict):
    def __init__(self, id,description, version):
        self.id =id
        self.description = description
        self.version = version
        dict.__init__(self, code=id,description=version)

    def GetId(self):
        return self.id