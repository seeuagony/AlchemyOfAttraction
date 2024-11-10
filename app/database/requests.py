from app.database.models import async_session, User
from sqlalchemy import select

def connection(func):
    async def inner(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)
    return inner

@connection
async def set_user(session, tg_id):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    
    if not user:
        session.add(User(tg_id=tg_id))
        await session.commit()

@connection
async def get_users(session):
    return await session.scalars(select(User))