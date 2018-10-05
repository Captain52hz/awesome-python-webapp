import orm
from models import User, Blog, Comment
import asyncio
from aiohttp import web

async def test(loop):
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    u = User(name='Test', email='tt@example.com', admin=True, passwd='1234567890', image='about:blank')
    await u.save()
    
async def find(loop):
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    rs = await User.find('001538627898514f9399b2e0e52480d9a7a899f4f005443003')
    print('查找测试： %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop), find(loop)]))
loop.run_forever()