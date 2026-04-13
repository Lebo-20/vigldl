import asyncio
import httpx

async def test():
    cookies = {
        "CloudFront-Policy": "eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vc2VjdXJlLWNvbnRlbnQudmlnbG9vLmNvbS9tZWRpYS9rcjAwOS9wMDcvczAxL2UwMDEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc3NjAxODk5Nn19fV19",
        "CloudFront-Signature": "YHQzvE5QQMb2u3uFO60e~cAM9beiKKiedkAY6530d3v4GWLu9vYw18wneSk63Y9Ex7UnzR3qNQdq-ruTd22eIutLgc3WCWWlfGWSGQAxgZ0Sl5FOtZt8L7jb1QC9xnIcWf3ApebWQTHOO4csVb-0Ce7ep6ZfqIJeTSC5ssl~j-Tp8RMR2P6DeRCnRqKJ34PskaHJRVYxYD0Fq1dEYYT87584WC6SLB9wtd41thauHbtFRZe89X3DXH7DBsHNM2xEGxrw7wUOV-qwSgczVZJNMU7S3QVWyJ6qRGNkwpRi51q6m6Yzn1qtqJVjthUbiZEqXZ9iZR8GLH~Ot8f8LoMA6A__",
        "CloudFront-Key-Pair-Id": "K2O1AA815RS45N"
    }
    url = "https://secure-content.vigloo.com/media/kr009/p07/s01/e001/aad7fb3fa739485eae260aaf2c9e5e4c.m3u8"
    
    headers = {
        "User-Agent": "Vigloo/1.1.0 (com.vigloo.android; build:110; Android 13; Model:SM-G998B)"
    }
    
    async with httpx.AsyncClient(headers=headers) as client:
        try:
            r = await client.get(url, cookies=cookies)
            print(f"Status: {r.status_code}")
            if r.status_code == 200:
                print("--- M3U8 CONTENT ---")
                print(r.text)
                print("--- END ---")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
