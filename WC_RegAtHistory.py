from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Index import GDT_Index
from gdo.core.GDT_Percent import GDT_Percent
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.core.GDT_UserName import GDT_UserName
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Edited import GDT_Edited
from gdo.ui.GDT_Rank import GDT_Rank
from gdo.ui.GDT_Score import GDT_Score
from gdo.wechall.GDT_Site import GDT_Site


class WC_RegAtHistory(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('rh_id'),
            GDT_Site('rh_site').not_null(),
            GDT_User('rh_user').not_null(),
            GDT_Score('rh_score').not_null().initial('0'),
            GDT_Percent('rh_percent').not_null().initial('0'),
            GDT_Score('rh_gain_score').not_null().initial('0'),
            GDT_Percent('rh_gain_percent').not_null().initial('0'),
            GDT_Score('rh_onsite_score').not_null(),
            GDT_UInt('rh_onsite_solved').not_null(),
            GDT_Rank('rh_onsite_rank'),
            GDT_Created('rh_created'),
            GDT_Enum('rh_type').choices({'gain': 'gain', 'lost': 'lost', 'ban': 'ban', 'unban': 'unban', 'link': 'link', 'unlink': 'unlink', 'hardlink': 'hardlink', 'unknown': 'unknown'}).not_null().initial('unknown'),
            GDT_Index('rh_index_site').index_fields('rh_site'),
            GDT_Index('rh_index_user').index_fields('rh_user'),
        ]
