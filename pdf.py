import pandas as pd
from jinja2 import Environment
from jinja2 import FileSystemLoader
import pdfkit

def all_for_one(row):
    dump = ''
    for col in row.keys():
        dump += 'coluna: '+str(col)+' valor: ' + str(row[col]) + '|' 
    return dump


            
if __name__ == '__main__':
    #PRE-PROCCESS DATA TO INGEST IN TEMPLATE
    df = pd.read_csv('votorantim_2023.csv',sep=',',encoding='utf-8', nrows=15000)
    df.drop_duplicates(subset=['Titulo','materia'], keep='last', inplace=True)
    df.set_index(['Titulo','materia'], inplace=True)
    
    
    #LOAD TEMPLATE
    env = Environment(loader=FileSystemLoader('C:\\Users\\Junio\\OneDrive\\Documentos\\Python_Scripts\\conjecto_wave\\templates'))
    template_vars = {
        'nome_empresa': df['nome_empresa'].values[0],
        'dataframe': df
    }
    template = env.get_template('dump_noticias.html')
    html = template.render(template_vars)
    pdfkit.from_string(html, 'out.pdf')
    
    
    
           


