from  Mapping.BHeader import HeaderClass as Header
from  Mapping.ABloco  import BlocoClass as Bloco

class EfdClass(dict):
    Headers = []
    # Bloco ecada relatorio EX: EFD 
    Bloco =  Bloco(1,"EFD", 1)
    def __init__(self):
        dict.__init__(self)
        self.LoadHeaders()

    def LoadHeaders(self):
        self.Headers.append(Header("0000", "REG,COD_VER,COD_VER,IND_SIT_ESP,IND_SIT_ESP,IND_SIT_ESP,IND_SIT_ESP,NOME,CNPJ,UF,COD_MUN,SUFRAMA,IND_NAT_PJ,IND_ATIV",
        {
            "COD_VER":"Código da versão do leiaute conforme a tabela",
            "TIPO_ESCRIT":"Tipo de escrituração,0 - Original,1 – Retificadora",
            "IND_SIT_ESP":"Indicador de situação especial,0 - Abertura,1 - Cisão,2 - Fusão,3 - Incorporação,4 – Encerramento",
            "IND_NAT_PJ":"Indicador da natureza da pessoa jurídica:,00 – Pessoa jurídica em geral,01 – Sociedade cooperativa,01 – Sociedade cooperativa,00 – Pessoa jurídica em geral (não participante de SCP como sócia ostensiva),00 – Pessoa jurídica em geral (não participante de SCP como sócia ostensiva),00 – Pessoa jurídica em geral (não participante de SCP como sócia ostensiva),02 – Entidade sujeita ao PIS/Pasep exclusivamente com base na Folha de Salários,03 - Pessoa jurídica em geral participante de SCP como sócia ostensiva,04 – Sociedade cooperativa participante de SCP como sócia ostensiva,05 – Sociedade em Conta de Participação -SCP",
            "IND_ATIV":"Indicador de tipo de atividade preponderante,0 – Industrial ou equiparado a industrial,1 – Prestador de serviços,2 - Atividade de comércio,3 – Pessoas jurídicas referidas nos §§ 6º, 8º e ,9º do art. 3º da Lei nº 9.718, de 1998,4 – Atividade imobiliária,9 – Outros",
        },
        0,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0001", "REG,IND_ATIV",
        {
            "IND_MOV":"Indicador de movimento,0 - Bloco com dados informados;,1 – Bloco sem dados informados.",
        },
        1,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0035", "REG,COD_SCP,COD_SCP,INF_COMP",
        {
        },
        2,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0100", "REG,NOME,CPF,CRC,CNPJ,CEP,END,NUM,COMPL,BAIRRO,FONE,FAX,EMAIL,COD_MUN",
        {
        },
        2,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0110", "REG,COD_INC_TRIB,IND_APRO_CRED,IND_REG_CUM",
        {
            "COD_INC_TRIB":"Código indicador da incidência tributária no período:,1 – Escrituração de operações com incidência exclusivamente no regime não-cumulativo;,2 – Escrituração de operações com incidência exclusivamente no regime cumulativo;,3 – Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo",
            "IND_APRO_CRED":"Código indicador de método de apropriação de créditos comuns, no caso de incidência no regime não-cumulativo (COD_INC_TRIB = 1 ou 3):,1 – Método de Apropriação Direta;2 – Método de Rateio Proporcional (Receita Bruta)",
            "COD_TIPO_CONT":"Código indicador do Tipo de Contribuição Apurada no Período,1 – Apuração da Contribuição Exclusivamente a Alíquota Básica,2 – Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto",
            "IND_REG_CUM":"Código indicador do critério de escrituração e apuração adotado, no caso de incidência exclusivamente no regime cumulativo (COD_INC_TRIB = 2), pela pessoa jurídica submetida ao regime de tributação com base no lucro presumido:,1 – Regime de Caixa – Escrituração consolidada (Registro F500);,2 – Regime de Competência - Escrituração consolidada (Registro F550);,9 – Regime de Competência - Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”",
        },
        2,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0111", "REG,REC_BRU_NCUM_TRIB_MI,REC_BRU_NCUM_TRIB_MI,REC_BRU_ NCUM_EXP,REC_BRU_ NCUM_EXP,REC_BRU_ NCUM_EXP",
        {
        },
        3,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0120", "REG,MES_REFER,INF_COMP",
        {
            "INF_COMP":"Informação complementar do registro. No caso de escrituração sem dados, deve ser informado o real motivo dessa situação, conforme indicadores abaixo:,01 - Pessoa jurídica imune ou isenta do IRPJ,02 - Órgãos públicos, autarquias e fundações públicas ,03 - Pessoa jurídica inativa ,04 - Pessoa jurídica em geral, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos ,05 - Sociedade em Conta de Participação - SCP, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos ,06 - Sociedade Cooperativa, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos ,07 - Escrituração decorrente de incorporação, fusão ou cisão, sem operações geradoras de receitas (tributáveis ou não) ou de créditos ,99 - Demais hipóteses de dispensa de escrituração, relacionadas no art. 5º, da IN RFB nº 1.252, de 2012 ",
        },
        2,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0140", "REG,COD_EST,NOME,CNPJ,UF,IE,COD_MUN,IM,SUFRAMA",
        {
        },
        2,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0145", "REG,COD_INC_TRIB,VL_REC_TOT,VL_REC_ATIV,VL_REC_DEMAIS_ATIV,INFO_COMPL",
        {
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0150", "REG,COD_PART,NOME,NOME,CNPJ,CPF,IE,COD_MUN,SUFRAMA,END,NUM,COMPL,BAIRRO",
        {
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0190", "REG,UNID,DESCR",
        {
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0200", "REG,COD_ITEM,DESCR_ITEM,COD_BARRA,COD_ANT_ITEM,UNID_INV,TIPO_ITEM,COD_NCM,EX_IPI,COD_GEN,COD_LST,ALIQ_ICMS",
        {
            "TIPO_ITEM","Tipo do item – Atividades Industriais, Comerciais e Serviços:,00 – Mercadoria para Revenda;,01 – Matéria-Prima;,02 – Embalagem;,03 – Produto em Processo;,04 – Produto Acabado;,05 – Subproduto;,06 – Produto Intermediário;,07 – Material de Uso e Consumo;,08 – Ativo Imobilizado;,09 – Serviços;,10 – Outros insumos;,99 – Outras"
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0205", "REG,DESCR_ANT_ITEM,DT_INI,DT_FIM,COD_ANT_ITEM",
        {
        },
        4,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0206", "REG,COD_COMB",
        {
        },
        4,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0208", "REG,COD_TAB,COD_GRU,MARCA_COM",
        {
            "COD_TAB":"Código indicador da Tabela de Incidência, conforme Anexo III do Decreto nº 6.707/08:,01 – Tabela I,02 – Tabela II,03 – Tabela III,04 – Tabela IV,05 – Tabela V,06 – Tabela VI,07 – Tabela VII,08– Tabela VIII,09 – Tabela IX,10 – Tabela X,11 – Tabela XI,12 – Tabela XII,Código indicador da Tabela de Incidência, conforme Anexo III do Decreto nº 6.707/08:,01 – Tabela I,02 – Tabela II,03 – Tabela III,04 – Tabela IV,05 – Tabela V,06 – Tabela VI,07 – Tabela VII,08– Tabela VIII,09 – Tabela IX,10 – Tabela X,11 – Tabela XI,12 – Tabela XII"
        },
        4,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0400", "REG,COD_NAT,DESCR_NAT",
        {
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0450", "REG,COD_INF,TXT",
        {
        },
        3,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0500", "REG,DT_ALT,COD_NAT_CC,IND_CTA,NÍVEL,COD_CTA,NOME_CTA,COD_CTA_REF,CNPJ_EST",
        {
            "COD_ NAT_CC":"Código da natureza da conta/grupo de contas:,01 - Contas de ativo,02 - Contas de passivo;,03 - Patrimônio líquido;,04 - Contas de resultado;,05 - Contas de compensação;,09 - Outras"
        },
        2,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0600", "REG,DT_ALT,COD_CCUS,CCUS",
        {
        },
        2,True,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0900", "REG,REC_TOTAL_BLOCO_A,REC_NRB_BLOCO_A,REC_TOTAL_BLOCO_C,REC_NRB_BLOCO_C,REC_TOTAL_BLOCO_D,REC_NRB_BLOCO_D,REC_TOTAL_BLOCO_F,REC_NRB_BLOCO_F,REC_TOTAL_BLOCO_I,REC_NRB_BLOCO_I,REC_TOTAL_BLOCO_1,REC_NRB_BLOCO_1,REC_TOTAL_PERIODO,REC_TOTAL_NRB_PERÍODO",
        {
        },
        2,False,self.Bloco.GetId()
        ))
        self.Headers.append(Header("0990", "REG,QTD_LIN_0",
        {
        },
        2,False,self.Bloco.GetId()
        ))


    def Find_Header(self, id):
        print("Find id =>" + str(id))
        for header in self.Headers:
            print(str(header.Id))
            if header.Id == str(id):
                print("Finded header =>" + header.Id)
                return header

    def Find_Values(self, id):
        print("Find id =>" + str(id))
        list =  []
        for value in self.Values:
            if value.Id == str(id):
                print("Finded value =>" + value.Id)
                list.append(value)
        
        return list

    

   
