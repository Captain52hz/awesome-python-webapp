import asyncio 
import aiomysql 
 
async def sql_test(): 
    conn = await aiomysql.connect(host="127.0.0.1", port=3306, user="root", password="password", db="awesome", loop=loop) 
    cur = await conn.cursor(aiomysql.DictCursor)
    # sql = "insert into `users` (`email`, `passwd`, `admin`, `name`, `image`, `created_at`, `id`) values ('?', '?', '?', '?', '?', '?', '?')"
    # args = ['test@example.com', '1234567890', True, 'Test', 'about:blank', 1538627898.5145798, '001538627898514f9399b2e0e52480d9a7a899f4f005443000']
    args = ['test@example.com', '1234567890', True, 'Test', 'about:blank', 1538627898.5145798, '001538627898514f9399b2e0e52480d9a7a899f4f005443000']
    # await cur.execute("insert into users (email, passwd, admin, name, image, created_at, id) values ('test@example.com', '1234567890', True, 'Test', 'about:blank', 1538627898.5145798, '001538627898514f9399b2e0e52480d9a7a899f4f005443000')") 
    await cur.execute("insert into users (email, passwd, admin, name, image, created_at, id) values (%s, %s, %s, %s, %s, %s, %s)", ['tes@emple.com', '1234567890', True, 'Test', 'about:blank', 1538623398.5145768, '001538627898514f9399b2e0e52480d9a7a899f4f00544313']) 
    await cur.execute("select * from users")
    rs = await cur.fetchall()
    await conn.commit()
    print(rs)
    await cur.close() 
    conn.close() 
loop = asyncio.get_event_loop()
loop.run_until_complete(sql_test())
loop.run_forever()