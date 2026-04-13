import asyncio
import httpx
import json

async def find_subs():
    base_url = "https://drakula.dramabos.my.id"
    # Drama ID: 15001590 (Omniscient Evolution)
    # Season ID: 15001557
    params = {
        "lang": "id",
        "code": "A8D6AB170F7B89F2182561D3B32F390D"
    }
    
    headers = {
        "User-Agent": "Vigloo/1.1.0 (com.vigloo.android; build:110; Android 13; Model:SM-G998B)"
    }

    endpoints = [
        f"/api/vigloo/drama/15001590/season/15001557/episodes",
        f"/api/vigloo/getstream?seasonId=15001557&ep=1&videoId=15026732"
    ]

    async with httpx.AsyncClient(headers=headers) as client:
        for ep in endpoints:
            print(f"Testing: {ep}")
            r = await client.get(f"{base_url}{ep}", params=params)
            data = r.json()
            # Cari kata kunci subtitle di seluruh JSON
            dump = json.dumps(data).lower()
            if "sub" in dump or "vtt" in dump or "srt" in dump or "caption" in dump:
                print(f"!!! FOUND SOMETHING in {ep} !!!")
                print(json.dumps(data, indent=4))
            else:
                print(f"No subtitle info in {ep}")

if __name__ == "__main__":
    asyncio.run(find_subs())
