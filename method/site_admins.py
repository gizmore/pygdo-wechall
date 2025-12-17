from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.util.href import href
from gdo.table.MethodQueryTable import MethodQueryTable
from gdo.ui.GDT_Bar import GDT_Bar
from gdo.ui.GDT_Link import GDT_Link
from gdo.ui.GDT_Menu import GDT_Menu
from gdo.wechall.WC_SiteAdmin import WC_SiteAdmin


class site_admins(MethodQueryTable):

    def gdo_table(self) -> GDO:
        return WC_SiteAdmin.table()

    def gdo_execute(self) -> GDT:
        table = super().gdo_execute()
        return GDT_Bar().vertical().all_fields(
            table,
            GDT_Menu().add_fields(
                GDT_Link().href(href('wechall', 'add'))
            )
        )