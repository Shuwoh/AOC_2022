import requests


class dataManager:
    current_credentials:object
    credentials_path:str
    
    def __init__(self,credentials_path:str=".credentials"):
        self.credentials_path=credentials_path
        self.set_credentials()

    def set_credentials(self):
        self.current_credentials={"Cookies":self.readFile(self.credentials_path)}

    def readFile(self,path:str,output_type:str="str"):
        data=None
        try:
            if path.startswith(("http://","https://")):
                data=self.getAuthentifiedRessource(path)
            else:
                datafile=open(path,"r")
                data=datafile.read()
                datafile.close()
        except:
            print(f"Error while gathering {path}")
        data=data.split("\n") if output_type=="list" else data
        return data

    def getAuthentifiedRessource(self,path:str,credentials_path:str=".credentials"):
        cookies=self.current_credentials
        return requests.get(path,cookies=cookies).text
 
