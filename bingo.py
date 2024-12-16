import time
import random
import asyncio

async def generator(xlimit):
    count = 0
    while count < xlimit:
        yield random.randint(0, 100)
        count += 1

async def player(name, card, queue, bingo_event):
    marked = set()
    while not bingo_event.is_set():
        num = await queue.get()
        if num in card:
            marked.add(num)
        print(f"{name} {num} {card} {len(marked)}")
        if len(marked) == len(card):
            bingo_event.set()
            print(f"{name} is the WINNER {set(card)} {marked}")
            break

async def narrator(players_info, xlimit=1000):

    random.seed(time.time())  
    queues = []
    bingo_event = asyncio.Event()
    for (name, card) in players_info:
        q = asyncio.Queue()
        queues.append((name, card, q))
    player_tasks = [asyncio.create_task(player(name, card, q, bingo_event)) for (name, card, q) in queues]

    async for num in generator(xlimit):
        if bingo_event.is_set():
            break
        print(f"Number is {num}")
        for (_, _, q) in queues:
            await q.put(num)
        await asyncio.sleep(0.01)

    if not bingo_event.is_set():
        print("No WINNER found within limit")

    print("Game is over")
    for task in player_tasks:
        if not task.done():
            task.cancel()
    await asyncio.gather(*player_tasks, return_exceptions=True)

async def main():
    players_list = [
        ("player-1", [5,10,48,55]),
        ("player-2", [8,46,80,99]),
        ("player-3", [17,29,78,95])
    ]
    await narrator(players_list, xlimit=1000)

if __name__ == "__main__":
    asyncio.run(main())
