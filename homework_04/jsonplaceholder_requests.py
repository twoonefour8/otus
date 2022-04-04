"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from http import HTTPStatus
from aiohttp import ClientSession
from homework_04.models import User, Post
from typing import List, Any


COUNT = 10
USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> Any:
    async with session.get(url) as response:
        if response.status == HTTPStatus.OK:
            response_json = await response.json()
            return response_json

        return None


async def get_user(user_id: int) -> User:
    async with ClientSession() as session:
        response = await fetch_json(session, f'{USERS_DATA_URL}/{str(user_id)}')

    if response:
        return User(
            id=response.get('id', 1),
            name=response.get('name', ''),
            username=response.get('username', ''),
            email=response.get('email', '')
        )


async def get_user_posts(user_id: int) -> List:
    async with ClientSession() as session:
        response = list(await fetch_json(session, f'{POSTS_DATA_URL}?userId={str(user_id)}'))

    if response:
        return [
            Post(
                user_id=post.get('userId', 0),
                title=post.get('title', ''),
                body=post.get('body', '')
            )
            for post in response
        ]
    return []


async def fetch_users_data():
    return [await get_user(user_id) for user_id in range(1, COUNT + 1)]


async def fetch_posts_data():
    return [await get_user_posts(user_id) for user_id in range(1, COUNT + 1)]


async def get_data():
    users, posts = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )
    return users, posts


if __name__ == '__main__':
    asyncio.run(get_data())
