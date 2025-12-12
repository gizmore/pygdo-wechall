import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdotest.TestUtil import GDOTestCase, reinstall_module, web_plug, cli_plug


class WeChallTeet(GDOTestCase):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        reinstall_module('wechall')
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()

    async def test_wechall_import(self):
        out = cli_plug(None, '$wechall.import_wc5 --submit=1')
        self.assertIn('imported', out, 'import does not work.')
