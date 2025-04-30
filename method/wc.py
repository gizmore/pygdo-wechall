import aiohttp

from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_String import GDT_String


class wc(Method):

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_String('username'),
        ]

    async def gdo_execute(self) -> GDT:
        if username := self.param_val('username'):
            return await self.for_user(username)
        return await self.for_user(self._env_user.get_name())

    async def for_user(self, username: str) -> GDT:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://python.org') as response:
                pass

        pass
