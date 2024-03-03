import time
import asyncio
import curses
import random
from fire_animation import fire

TIC_TIMEOUT = 0.1


async def blink(canvas, row, column, symbol):
    while True:
        dim_time = random.randint(1, 20)
        bold_time = random.randint(1, 5)
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(dim_time):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(bold_time):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(0)
    canvas.border('|', '|', '-', '-', '+', '+', '+', '+')
    max_y, max_x = canvas.getmaxyx()
    num_coroutines = random.randint(10, 50)
    coroutines = []
    for _ in range(num_coroutines):
        x = random.randint(1, max_x - 2)
        y = random.randint(1, max_y - 2)
        symbol = random.choice('+*.:')
        coroutines.append(blink(canvas, y, x, symbol))

    x = max_x // 2
    y = max_y - 2
    fire_coroutine = fire(canvas, y, x)

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        try:
            fire_coroutine.send(None)
        except StopIteration:
            pass

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.wrapper(draw)