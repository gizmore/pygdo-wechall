from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.table.MethodQueryTable import MethodQueryTable
from gdo.ui.GDT_Rank import GDT_Rank
from gdo.user.GDT_ProfileLink import GDT_ProfileLink


class ranking(MethodQueryTable):

    def gdo_searched(self) -> bool:
        return False

    def gdo_table(self) -> GDO:
        return GDO_User.table()

    def gdo_table_headers(self) -> list[GDT]:
        return [
            GDT_Rank('rank'),
            GDT_ProfileLink(),
        ]
