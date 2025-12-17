from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.wechall.GDT_Site import GDT_Site


class WC_SiteFavs(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Site('sf_site').primary().cascade_delete(),
            GDT_User('sf_user').primary().cascade_delete(),
            GDT_Created('sf_created'),
        ]
