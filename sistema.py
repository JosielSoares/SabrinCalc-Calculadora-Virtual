import bge

class SabrinCalc():    
    def Iniciar(self):
        
        operacao = "" 
    def Atualizar(self): 
        cont = bge.logic.getCurrentController()
        obj = bge.logic.getCurrentScene().objects  
        own = cont.owner     
        self.Operacoes()
        self.Escrever()
        self.Exibir()
        
        if cont.sensors['mo_j'].positive and cont.sensors['mbutton'].positive:
            own['valor1'] = 0
            own['valor2'] = 0
            own['resultado']  = 0
            own['operacao'] = ""
            own['auxiliar'] = ""
            own['ligado'] = True
            
        elif cont.sensors['mo_i'].positive and cont.sensors['mbutton'].positive:
            own['valor1'] = 0
            own['valor2'] = 0
            own['resultado']  = ""
            own['operacao'] = ""
            own['auxiliar'] = ""
            own['ligado'] = False
    def Exibir(self):
        cont = bge.logic.getCurrentController() 
        own = cont.owner 
        saida = bge.logic.getCurrentScene().objects['saida']
        saida['Text'] = str(own['resultado'][0:9])
    def comparar_resultado(self):
        cont = bge.logic.getCurrentController()
        own = cont.owner 
        if own['resultado']  != "":
            own['auxiliar'] = own['resultado']
    def Escrever(self):
        # Para adicionar os números pressionados ao Display
        cont = bge.logic.getCurrentController()
        obj = bge.logic.getCurrentScene().objects  
        own = cont.owner 
        saida = obj['saida']
        
        if len(saida['Text']) <8 and own['ligado']==True:
            #Para adicionar o primeiro valor:
            if own['operacao']  == "" and own['valor1'] == 0 and own['valor2'] == 0:
                if cont.sensors['mo_0'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']!="":
                        own['valor1'] = 0
                        own['resultado']  = 0               
                    else:
                        own['valor2'] = 0
                        own['resultado']  =  0              
                if cont.sensors['mo_1'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = 1
                        own['resultado']  =  1
                    else:
                        own['valor2'] = 1  
                        own['resultado']  =  1          
                if cont.sensors['mo_2'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = 2
                        own['resultado']  =  2
                    else:
                        own['valor2'] = 2  
                        own['resultado']  =  2          
                if cont.sensors['mo_3'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = 3
                        own['resultado']  =  3
                    else:
                        own['valor2'] = 3    
                        own['resultado']  =  3         
                if cont.sensors['mo_4'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = 4
                        own['resultado']  =  4
                    else:
                        own['valor2'] = 4   
                        own['resultado']  =  4          
                if cont.sensors['mo_5'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = 5
                        own['resultado']  =  5
                    else:
                        own['valor2'] = 5    
                        own['resultado']  =  5         
                if cont.sensors['mo_6'].positive and cont.sensors['mbutton'].positive:   
                    if own['operacao']=="":
                        own['valor1'] = 6
                        own['resultado']  =  6
                    else:
                        own['valor2'] = 6  
                        own['resultado']  =  6            
                if cont.sensors['mo_7'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = 7
                        own['resultado']  =  7
                    else:
                        own['valor2'] = 7      
                        own['resultado']  =  7       
                if cont.sensors['mo_8'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = 8
                        own['resultado']  =  8
                    else:
                        own['valor2'] = 8    
                        own['resultado']  =  8         
                if cont.sensors['mo_9'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = 9
                        own['resultado']  =  9
                    else:
                        own['valor2'] = 9   
                        own['resultado']  =  9
            #Agora para adicionar caso ja exista algum numero
            else:
                if cont.sensors['mo_0'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']!="":
                        own['valor1'] = int(saida['Text'] + str(0))
                        own['resultado']  =  int(saida['Text']+ str(0))            
                    else:
                        own['valor2'] = int(saida['Text'] + str(0))
                        own['resultado']  =  int(saida['Text']+ str(0))            
                if cont.sensors['mo_1'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(1))
                        own['resultado']  =  int(saida['Text']+ str(1))
                    else:
                        own['valor2'] = int(saida['Text'] + str(1))  
                        own['resultado']  =  int(saida['Text']+ str(1))          
                if cont.sensors['mo_2'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(2))
                        own['resultado']  =  int(saida['Text']+ str(2)) 
                    else:
                        own['valor2'] = int(saida['Text'] + str(2))  
                        own['resultado']  =  int(saida['Text']+ str(2))           
                if cont.sensors['mo_3'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(3))
                        own['resultado']  =  int(saida['Text']+ str(3))
                    else:
                        own['valor2'] = int(saida['Text'] + str(3))   
                        own['resultado']  =  int(saida['Text']+ str(3))         
                if cont.sensors['mo_4'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(4))
                        own['resultado']  =  int(saida['Text']+ str(4))
                    else:
                        own['valor2'] = int(saida['Text'] + str(4))  
                        own['resultado']  =  int(saida['Text']+ str(4))          
                if cont.sensors['mo_5'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(5))
                        own['resultado']  =  int(saida['Text']+ str(5))
                    else:
                        own['valor2'] = int(saida['Text'] + str(5))    
                        own['resultado']  =  int(saida['Text']+ str(5))         
                if cont.sensors['mo_6'].positive and cont.sensors['mbutton'].positive:   
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(6))
                        own['resultado']  =  int(saida['Text']+ str(6))
                    else:
                        own['valor2'] = int(saida['Text'] + str(6))  
                        own['resultado']  =  int(saida['Text']+ str(6))            
                if cont.sensors['mo_7'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(7))
                        own['resultado']  =  int(saida['Text']+ str(7))
                    else:
                        own['valor2'] = int(saida['Text'] + str(7))      
                        own['resultado']  = int(saida['Text']+ str(7))       
                if cont.sensors['mo_8'].positive and cont.sensors['mbutton'].positive: 
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(8))
                        own['resultado']  =  int(saida['Text']+ str(8))
                    else:
                        own['valor2'] = int(saida['Text'] + str(8))    
                        own['resultado']  =  int(saida['Text']+ str(8))         
                if cont.sensors['mo_9'].positive and cont.sensors['mbutton'].positive:
                    if own['operacao']=="":
                        own['valor1'] = int(saida['Text'] + str(9))
                        own['resultado']  =  int(saida['Text']+ str(9))
                    else:
                        own['valor2'] = int(saida['Text'] + str(9))  
                        own['resultado']  =  int(saida['Text']+ str(9))
    def Entradas():
        pass
    def Operacoes(self):
        cont = bge.logic.getCurrentController()
        obj = bge.logic.getCurrentScene().objects  
        own = cont.owner 
        if cont.sensors['mo_b'].positive and cont.sensors['mbutton'].positive and own['auxiliar'] == "":
        
            if own['operacao'] == "soma":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] + own['valor2'])
                                    
            elif own['operacao'] == "subtracao":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] - own['valor2'])
            elif own['operacao'] == "multiplicacao":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] * own['valor2'])
            elif own['operacao'] == "divisao":
                if (str(own['resultado'] )!=""):
                    if own['valor2'] !=0:
                        own['resultado'] =  str(own['valor1'] / own['valor2'])
                    else:  
                        own['resultado']  = "ERRO"  
            own['operacao'] = ""
            own['valor1'] = 0
            own['valor2'] = 0
        elif cont.sensors['mo_b'].positive and cont.sensors['mbutton'].positive and own['auxiliar'] != "":
            if own['operacao'] == "soma":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] + own['valor2'])
                                    
            elif own['operacao'] == "subtracao":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] - own['valor2'])
            elif own['operacao'] == "multiplicacao":
                if (str(own['resultado'] )!=""):
                    own['resultado'] =  str(own['valor1'] * own['valor2'])
            elif own['operacao'] == "divisao":
                if (str(own['resultado'] )!=""):
                    if own['valor2'] !=0:
                        own['resultado'] =  str(own['valor1'] / own['valor2'])
                    else:  
                        own['resultado']  = "ERRO"  
            own['operacao'] = ""
            own['valor1'] = 0
            own['valor2'] = 0
        if cont.sensors['mo_c'].positive and cont.sensors['mbutton'].positive:
            self.comparar_resultado()
            own['resultado']  = ""
            own['operacao'] = "soma"      
        if cont.sensors['mo_d'].positive and cont.sensors['mbutton'].positive:
            self.comparar_resultado()
            own['resultado']  = ""
            own['operacao'] = "subtracao"
        if cont.sensors['mo_e'].positive and cont.sensors['mbutton'].positive:
            self.comparar_resultado()
            own['resultado']  = ""
            own['operacao'] = "multiplicacao"
        if cont.sensors['mo_f'].positive and cont.sensors['mbutton'].positive:
            self.comparar_resultado()
            own['resultado']  = ""
            own['operacao'] = "divisao" 
    def Saidas():
        pass
def main():
    sc = SabrinCalc()
    sc.Atualizar()
def iniciar():
    sc = SabrinCalc()
    sc.Iniciar()
    