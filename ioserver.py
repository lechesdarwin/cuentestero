import re
from aiofile import AIOFile
from sanic import Sanic
from sanic.request import Request
from sanic.response import json
import httpx
from laseno.down import down_e

app = Sanic(__name__)

async def down_img(link):
    regex = r"([\w-]+\.(?:jpg|jpeg|svg|png|gif|webp|webp))"
    m = re.search(regex, link)
    name = ""
    if m:
        name = m.group(1)
    else:
        name = str(random.getrandbits(32))
    h = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36"}
    data = await httpx.get(link, headers=h)
    async with AIOFile("{}/{}".format("img", name), "wb") as f:
        await f.write(data.content)
        await f.fsync()
    print("write into","{}/{}".format("img", name))
    return "{}/{}".format("img", name)

@app.post("/")
async def post_dump(request:Request):
    print(request.load_json()["url"])
    da = await down_e(request.load_json()["url"])
    img = da["img"]
    img_link = []
    if img:
        for i in img:
            name = await down_img(i)
            img_link.append(name)
    da["img"] = img_link
    return json(da)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888,debug=True)