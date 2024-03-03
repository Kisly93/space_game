import asyncio

async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)