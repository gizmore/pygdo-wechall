from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.util.href import href
from gdo.table.MethodQueryTable import MethodQueryTable
from gdo.ui.GDT_Bar import GDT_Bar
from gdo.ui.GDT_Link import GDT_Link
from gdo.ui.GDT_Menu import GDT_Menu
from gdo.wechall.WC_Site import WC_Site


class sites(MethodQueryTable):

    def gdo_table(self) -> GDO:
        return WC_Site.table()

    def gdo_table_headers(self) -> list[GDT]:
        s = WC_Site.table()
        return [
            s.column('site_id'),
            s.column('site_name'),
            s.column('site_url'),

        ]

    async def execute(self):
        table = await super().execute()
        menu = GDT_Menu().add_fields(
            GDT_Link().text('link_add_site').href(href('wechall', 'add_site')).text('mt_wechall_add_site'),
        )
        return GDT_Bar().vertical().add_fields(table, menu)
