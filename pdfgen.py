# -*- coding: utf-8
from __future__ import with_statement
import fpdf 
import configparser
import sys, os, time
                     
def gera_pdf(arquivo):
    pdf = fpdf.FPDF()    
    pdf.set_font('Courier', 'B', 7)            
    with open(arquivo) as file:        
        for line in file.readlines():                        
            if TOKEN_CAB in line:                               
                pdf.add_page()
            pdf.write(2, line)
            pdf.ln()
                                              
    saida = arquivo+".pdf"
    print(saida)                   
    pdf.output(saida,"F")            
    comando = "lp -d "+ IMPRESSORA + " " + saida
    print(comando)
    os.system(comando)
    data_hora = time.strftime('%Y%m%d%H%M%S')
    os.rename(saida,DIR_IMPRESSOS+os.sep+data_hora+'-'+os.path.basename(saida))
                                                                                         

if __name__ == "__main__":
   cfg = configparser.ConfigParser()
   cfg.read('config.ini')
   DIR_ORIGEM = cfg.get("geral","dir_origem")
   IMPRESSORA = cfg.get("geral","impressora")
   DIR_IMPRESSOS = cfg.get("geral","dir_impressos")   
   TOKEN_CAB = cfg.get("geral","token_cab")
   EXTENSAO = cfg.get("geral","extensao")
       
   while True:
       print('Aguardando arquivos '+DIR_ORIGEM)
       for root, dirs, arquivos in os.walk(DIR_ORIGEM, topdown=True):
           for arquivo in arquivos:
               nome_abs = os.path.join(root, arquivo)
               print(nome_abs)
               ext = nome_abs[-3:].lower()       
               if ext == EXTENSAO.lower():
                   gera_pdf(nome_abs)
                   data_hora = time.strftime('%Y%m%d%H%M%S')
                   os.rename(nome_abs,DIR_IMPRESSOS+os.sep+data_hora+'-'+os.path.basename(arquivo))
           
       for i in range(5):        
           time.sleep(1)
           print('.') 
           