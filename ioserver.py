from sanic import Sanic
from sanic.request import Request
from sanic.response import json
app = Sanic(__name__)


@app.post("/")
async def post_dump(request:Request):
    print(request.load_json()["url"])
    return json({
        "parsed": "🔥",
        "url": request.url,
        "args": request.args,
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888,debug=True)