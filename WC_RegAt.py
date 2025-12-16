from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Edited import GDT_Edited
from gdo.ui.GDT_Rank import GDT_Rank
from gdo.ui.GDT_Score import GDT_Score
from gdo.wechall.GDT_Site import GDT_Site


class WC_RegAt(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Site('regat_site').primary(),
            GDT_User('regat_user').primary(),
            GDT_UserName('regat_onsite_name').not_null(),
            GDT_Score('regat_onsite_score').not_null(),
            GDT_UInt('regat_onsite_solved').not_null(),
            GDT_Rank('regat_onsite_rank'),
            GDT_Created('regat_first_link'),
            GDT_Edited('regat_last_link'),
        ]
