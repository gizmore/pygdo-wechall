from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Index import GDT_Index
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.wechall.WC_Site import WC_Site


class WC_SiteHistory(GDO):

    def gdo_columns(self) -> list[GDT]:
        from gdo.wechall.GDT_Site import GDT_Site
        return [
            GDT_AutoInc('sh_id'),
            GDT_Site('sh_site').not_null().cascade_delete(),
            GDT_UInt('sh_score').initial('0'),
            GDT_UInt('sh_user_count').initial('0'),
            GDT_UInt('sh_chall_count').initial('0'),
            GDT_Created('sh_created'),
            GDT_Index('sh_index_site').index_fields('sh_site'),
        ]

    @classmethod
    def on_update(cls, site: 'WC_Site', usercount: str, challcount: str):
        cls.blank({
            'sh_site': site.get_id(),
            'sh_score': str(site.calc_site_score()),
            'sh_user_count': usercount,
            'sh_chall_count': challcount,
        }).insert()

