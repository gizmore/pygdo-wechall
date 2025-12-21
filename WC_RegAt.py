from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Edited import GDT_Edited
from gdo.ui.GDT_Error import GDT_Error
from gdo.ui.GDT_Rank import GDT_Rank
from gdo.ui.GDT_Score import GDT_Score
from gdo.ui.GDT_Success import GDT_Success
from gdo.wechall.GDT_Site import GDT_Site
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.wechall.WC_Site import WC_Site


class WC_RegAt(GDO):

    @classmethod
    def link(cls, user: GDO_User, site: 'WC_Site', onsite_name: str):
        if not site.on_link(user, onsite_name):
            return GDT_Error().text('err_wc_link_site')
        if not (regat := site.on_update(user)):
            return GDT_Error().text('err_wc_update')
        return GDT_Success().text('msg_wc_linked')

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Site('regat_site').primary(),
            GDT_User('regat_user').primary(),
            GDT_UserName('regat_onsite_name').maxlen(64).not_null(),
            GDT_Score('regat_onsite_score'),
            GDT_UInt('regat_onsite_solved'),
            GDT_Rank('regat_onsite_rank'),
            GDT_Created('regat_first_link'),
            GDT_Edited('regat_last_link'),
        ]

    def get_user(self) -> GDO_User:
        return self.gdo_value('regat_user')
