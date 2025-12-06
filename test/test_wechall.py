import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdotest.TestUtil import GDOTestCase, install_module


class WeChallTeet(GDOTestCase):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        install_module('wechall')
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()

    async def test_wechall(self):
        pass
