import aiohttp
import asyncio
import time
import pytest
import sys

sys.argv[1:]

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


@pytest.mark.asyncio
async def test_app():
    session = aiohttp.ClientSession()
    tasks = []
    for number in range(1, 151):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

    original_pokemon = await asyncio.gather(*tasks)
    for pokemon in original_pokemon:
        print(pokemon)

    print("--- %s seconds ---" % (time.time() - start_time))
