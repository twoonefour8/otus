"""
Домашнее задание №4
Асинхронная работа с сетью и бд
доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from homework_04.models import engine, Base, Session
from homework_04.jsonplaceholder_requests import get_data, COUNT


async def create_schemas():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def create_users(users_data):
    async with Session() as session:
        session.add_all(users_data)
        await session.commit()


async def create_posts(posts_data):
    async with Session() as session:
        [session.add_all(posts_data[user_id-1]) for user_id in range(1, COUNT + 1)]
        await session.commit()


async def async_main():
    await create_schemas()
    users, posts = await get_data()
    await create_users(users)
    await create_posts(posts)


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
