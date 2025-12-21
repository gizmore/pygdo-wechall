import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.core.GDT_UserName import GDT_UserName
from gdo.core.method.clear_cache import clear_cache
from gdo.wechall.WC_Site import WC_Site
from gdotest.TestUtil import GDOTestCase, reinstall_module, install_module, cli_plug


class WeChallTest(GDOTestCase):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        install_module('wechall')
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()
        await clear_cache().gdo_execute()

    async def test_01_wechall_import(self):
        reinstall_module('wechall')
        sites = WC_Site.table().all()
        self.assertGreaterEqual(len(sites), 1, 'sites no work.')
        out = cli_plug(None, '$wechall.import_wc5 --submit=1')
        self.assertIn('imported', out, 'import does not work.')

    async def test_02_username_pattern(self):
        gdt = GDT_UserName('regat_user').maxlen(64)
        self.assertTrue(gdt.validate('0213'), 'Username validation failed.')
        self.assertTrue(gdt.validate('abcdefghijklmnopqrstuvwxyz0123451234'), 'Username validation failed.')
        self.assertFalse(gdt.validate('abcdefghijklmnopqrstuvwxyz012345abcdefghijklmnopqrstuvwxyz012345a'), 'Username validation failed.')
