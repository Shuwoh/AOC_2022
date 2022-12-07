import requests

def getAuthentifiedRessource(path:str,credentials_path:str=".credentials"):
    cookies={"Cookies": open(credentials_path,"r").read()}
    print(cookies)
    return requests.get(path,cookies=cookies).text

def getInputData(path:str,mode:str="str"):
    data=None
    if path.startswith(("http://","https://")):
        data=getAuthentifiedRessource(path)
    else:
        data=open(path,"r").read()
    data=data.split("\n") if mode =="list" else data
    return data

