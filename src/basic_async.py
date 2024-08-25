import asyncio
import time


async def async_fun_1():
    print('async fun 1 start')
    await async_fun_2()
    print('async fun 1 end')
    return 42

async def async_fun_2():
    print('async fun 2 start')
    time.sleep(2)
    print('async fun 2 end')
    return


if __name__ == '__main__':
    result = asyncio.run(async_fun_1())
    asyncio.gather()
    print(f'async: {result}')
    print('main fun finished')
