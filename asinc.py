import httpx
import asyncio
import pickle
import requests


URL = []
data = []
with open("url.pkl","rb") as f:
    URL = pickle.load(f)

# if all ok comment next line
URL = URL[:5]
print(URL)
h = {"Connection":"keep-alive"}
async def download(url:str):
    
    resp = requests.post("http://127.0.0.1:8888/",json={"url":url})
    if resp.status_code == 200:
        print(url," Ok")
        data.append(resp)

if __name__ == "__main__":
    try:    
        loop = asyncio.get_event_loop()
        task = [download(url) for url in URL]
        loop.run_until_complete(asyncio.gather(*task))
    except Exception as e:
        print(str(e))
        print("fallo")
    finally:
        loop.close()
        print("Voy a scribir")
        with open("data.pkl","wb") as f:
            pickle.dump(data,f)
