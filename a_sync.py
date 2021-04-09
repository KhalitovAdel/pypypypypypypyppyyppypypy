import asyncio

# 10 sec
import threading


async def lol(seconds = 10):
    print('start ' + str(seconds))
    await asyncio.sleep(seconds)
    print('after ' + str(seconds) + ' second')
    return seconds


async def sync_example():
    print('sync start')
    await lol()
    # after 10 second should print 2
    print('sync finished')

def async_example():
    thread = threading.Thread(target=asyncio.run, args=(lol(2),))
    thread.start()
    print('async start')
    # print 1, 2 after lol task should complete lol in other thread
    print('async finished')
    return 123

result = async_example()
print('it is async result', result)
# awaiting of async_example thread end a work
asyncio.run(asyncio.sleep(2))

print('--------- Then WE CALL SYNC EXAMPLE -----------')

asyncio.run(sync_example())

while True:
    asyncio.run(asyncio.sleep(1))