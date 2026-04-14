import os 
import json
import requests

class Assistant:
    def __init__(self,api_key):
        self.key=api_key
        self.history=self.load_history()

    def prompt(self):
        print('type to chat...')
        while True:
            msg=input('')
            if  msg.strip():
                return msg

    def load_history(self):
        self.create_history_ifmissing()
        try:
            with open('history.json','r') as f:
                data=json.load(f)
                return data
        except Exception as e:
            print(f"error {e}")
            return [] 

    def create_history_ifmissing(self): 
        if not(os.path.exists(os.path.join(os.getcwd(),'history.json'))):
            with open('history.json','w') as f:
                json.dump([],f)  

    def store(self,role,content):
        self.history.append({'role':role,'content':content})
    
    def save_history(self):
        with open('history.json','w') as f:
            json.dump(self.history,f )
    
    def chat(self):
        while True:
            msg=self.prompt()
            self.store('user',msg)
            url = "https://api.groq.com/openai/v1/chat/completions"
            header = {"Authorization": f"Bearer {self.key}","Content-Type": "application/json"}
            body = {"model": "llama-3.1-8b-instant","messages": self.history,"max_tokens": 1024}
            try:
                rep = requests.post(url,headers=header,json=body)
                rep.raise_for_status()
            except requests.exceptions.RequestException as e:
                print("api error :", e)
                self.history.pop()  
                continue            
                
            data=rep.json()
            reply =data['choices'][0]['message']['content']
            print(reply)
            self.store('assistant',reply)
            while True :
                print('continue ? Y/N')
                answr=input('')
                answr=answr.upper()
                if answr in['Y','N']:
                    break
            if answr.upper() =='N':
                    self.save_history()
                    break 
                    


if __name__ == "__main__":
    api_key=input("type ur api key here")
    assistant=Assistant(api_key)
    assistant.chat()