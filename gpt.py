import os
from h2ogpte import H2OGPTE
#sk-K5QxsL7wfhg8SoUr14ZniUTwV4yRf9iLXJmO2lMDPuAjXlN8
#sk-ropeHDcTRJk3JqgQTBQzZpftzoH7mw5trhWsSRq3mFeE3Q5y
#sk-ZQqN8TE7kyDa8RUL3ctosCekkXFc8UAG64fnzr0NHoA3r8GK

class ReplyWizard:
    def __init__(self) -> None:
        self.client = H2OGPTE(address='https://h2ogpte.genai.h2o.ai',
                         api_key='sk-uGKAAChaNWiEBC3yUs83vMGaQQzDZ35Gay0QE5uqMiH64zYm',)
        
        self.chat_session_id = self.client.create_chat_session_on_default_collection()
        self.session = self.client.connect(self.chat_session_id)  
        self.collection_id = self.client.get_collection_for_chat_session(self.chat_session_id).id
    
    def query(self,text):
        with self.client.connect(self.chat_session_id) as session:
            reply = session.query(text,timeout=120)
        return reply
        
    def upload_file(self, file):
        dir = os.getcwd()+'\\data\\f\\'
        path = dir + file
        with open(path,'rb',encoding='utf8') as f:
            upload_file = self.client.upload(path.split('\\')[-1], f)
            
        self.client.ingest_uploads(self.collection_id,[upload_file])    
        
    def get_documments(self):
        list_doc = self.client.list_documents_in_collection(self.collection_id, 0, 100)
        return list_doc
    
if __name__ == '__main__':
    gpt = ReplyWizard()
    print(gpt.query('Ola'))

