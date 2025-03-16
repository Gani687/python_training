import sys
import asyncio
import time
import aiohttp

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  
                return await response.text()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None


async def download_single():
    url = "http://httpbin.org/get"
    result = await fetch(url)
    return result


async def download_multiple(count):
    urls = ["http://httpbin.org/get" for _ in range(count)]
    results = await asyncio.gather(*[fetch(url) for url in urls])
    return results

if __name__ == '__main__':
    start_time = time.time()   
    asyncio.run(download_single())
    print("Time taken for single download:", time.time() - start_time, "secs")   
    print('Now running multiple downloads in parallel...')
    start_time = time.time()  
    results = asyncio.run(download_multiple(10))
    print("Time taken for parallel downloads:", time.time() - start_time, "secs")
    print("Results:", results)
    