import asyncio, time, aiohttp

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

async def ask(session, idx):
    payload = {"model": MODEL, "stream": True, "messages": [{"role": "user", "content": f"Explain batching in LLM serving. request={idx}"}]}
    t0 = time.perf_counter(); t_first = None
    async with session.post(URL, json=payload) as r:
        async for _ in r.content:
            if t_first is None: t_first = time.perf_counter()
    t1 = time.perf_counter()
    return idx, t0, t_first, t1

async def main(n=4):
    async with aiohttp.ClientSession() as s:
        rows = await asyncio.gather(*(ask(s, i) for i in range(n)))
    base = min(r[1] for r in rows)
    for idx, t0, tf, t1 in rows:
        print(idx, f"start={t0-base:.3f}s first={tf-base:.3f}s end={t1-base:.3f}s")

asyncio.run(main())
