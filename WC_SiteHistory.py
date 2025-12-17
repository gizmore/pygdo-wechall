from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Index import GDT_Index
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.wechall.GDT_Site import GDT_Site


class WC_SiteHistory(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('sh_id'),
            GDT_Site('sh_site').not_null().cascade_delete(),
            GDT_UInt('sh_score').initial('0'),
            GDT_UInt('sh_user_count').initial('0'),
            GDT_UInt('sh_chall_count').initial('0'),
            GDT_Created('sh_created'),
            GDT_Index('sh_index_site').index_fields('sh_site'),
        ]

