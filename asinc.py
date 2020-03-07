import httpx
import asyncio
import pickle


URL = []
data = []
with open("url.pkl","rb") as f:
    URL = pickle.load(f)

async def download(url:str):
    resp = await httpx.post("http://127.0.0.1:5555/",json={"url":url})
    if resp.status_code == 200:
        print(url," Ok")
        data.append(resp)
        return 200
    else:
        return 400

if __name__ == "__main__":
    try:    
        loop =asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*[download(url) for url in URL]))
    except Exception:
        print("fallo")
    finally:
        loop.close()
        with open("data.pkl","wb") as f:
            pickle.dump(data,f)
