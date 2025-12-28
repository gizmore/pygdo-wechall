from gdo.base.GDO import GDO
from gdo.core.GDO_User import GDO_User
from gdo.table.MethodQueryTable import MethodQueryTable


class country_ranking(MethodQueryTable):

    def gdo_searched(self) -> bool:
        return False

    def gdo_table(self) -> GDO:
        return GDO_User.table()

