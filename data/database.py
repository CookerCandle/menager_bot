import aiosqlite


class Database:
    def __init__(self, db_path: str = "./data/database.db"):
        self.db_path = db_path
    
    async def initialize(self) -> None:
        async with aiosqlite.connect(self.db_path) as db:

            # Create the users table if it does not exist
            await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE NOT NULL
            )
            """)

            # Create the channels table if it does not exist
            await db.execute("""
            CREATE TABLE IF NOT EXISTS channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный ID канала
                name TEXT NOT NULL, -- Название канала
                link TEXT NOT NULL, -- Ссылка на канал
                member INTEGER -- id Канала -100351353
            )
            """)        

            # save changes
            await db.commit()

# <---------------USER----------------->
    async def user_exists(self, user_id):
        async with aiosqlite.connect(self.db_path) as conn:
            async with conn.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)) as cursor:
                result = await cursor.fetchone()
                return bool(result)
              
    async def add_user(self, user_id):
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
            await conn.commit()


# <---------------ADMIN----------------->
    async def get_channels(self):
        async with aiosqlite.connect(self.db_path) as conn:
            async with conn.execute('SELECT name, link, member FROM channels') as cursor:
                result = await cursor.fetchall()
                return result
            
    async def add_channel(self, name, link, member):
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute('INSERT INTO channels (name, link, member) VALUES (?, ?, ?)', (name, link, member))
            await conn.commit()

    async def delete_channel(self, name):
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute('DELETE FROM channels WHERE name = ?', (name,))
            await conn.commit()