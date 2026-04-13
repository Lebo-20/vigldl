import asyncio
import httpx

async def check():
    url = "https://drakula.dramabos.my.id/api/vigloo/getstream?lang=id&code=A8D6AB170F7B89F2182561D3B32F390D&seasonId=15001024&ep=1&videoId=15022079"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        data = r.json()
        m3u8 = data.get("url")
        cookies = data.get("cookies")
        print(f"URL: {m3u8}")
        
        # Baca konten m3u8
        r2 = await client.get(m3u8, cookies=cookies)
        print("--- CONTENT ---")
        print(r2.text[:500]) # Print first 500 chars

if __name__ == "__main__":
    asyncio.run(check())
