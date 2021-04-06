import asyncio

# 10 sec
async def lol(seconds = 10):
    print('start ' + str(seconds))
    await asyncio.sleep(seconds)
    print('after ' + str(seconds) + ' second')


async def sync_example():
    print(1)
    await lol()
    # after 10 second should print 2
    print(2)

def asyc_example():
    print(1)
    lol()
    # print 1, 2 after lol task should complite lol
    print(2)

