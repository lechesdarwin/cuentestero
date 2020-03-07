import httpx
glo = None
async def w(url):
    with httpx.get('https://www.example.org/') as r:
        return await r
