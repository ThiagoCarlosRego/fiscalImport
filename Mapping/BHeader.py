class HeaderClass(dict):
    def __init__(self, id, columns, descripitonColumn, nivel, required, bloco = 1):
        dict.__init__(self,id=id, columns=columns, descripitonColumn=descripitonColumn,nivel=nivel,required=required, bloco = bloco)

    def List_Column(sefl):
        return sefl.Columns.split(',')