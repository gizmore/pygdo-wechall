from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Query import Query
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

    def gdo_cached(self) -> bool:
        return False

    @classmethod
    def link(cls, user: GDO_User, site: 'WC_Site', onsite_name: str):
        if not site.on_link(user, onsite_name):
            return GDT_Error().text('err_wc_link_site')
        if not (regat := site.on_update(user)):
            return GDT_Error().text('err_wc_update')
        return GDT_Success().text('msg_wc_linked')

    @classmethod
    def calc_scores(cls, site: WC_Site, user: GDO_User = None):
        max = site.gdo_val('site_max_score')
        powarg = site.gdo_val('site_pow_arg')
        challcount = int(site.gdo_val('site_chall_count') or 0)
        sitescore = site.gdo_val('site_score')
        if challcount > 0:
            and_user = f' AND regat_user={user.get_id()}' if user else ''
            Query().raw(f"UPDATE wc_regat SET regat_score=POW(LEAST(1,regat_onsite_score/{max}),(1+({powarg}/{challcount})))*{sitescore} WHERE regat_site={site.get_id()}{and_user}").exec()
            where_user = f'WHERE regat_user={user.get_id()}' if user else ''
            Query().raw(f"""
                        INSERT INTO gdo_usersetting (uset_user, uset_key, uset_val)
                        SELECT r.regat_user, 'score', COALESCE(SUM(r.regat_score), 0)
                        FROM wc_regat r
                        GROUP BY r.regat_user
                        {where_user}
                        ON DUPLICATE KEY UPDATE uset_val = VALUES(uset_val)
                        """)



    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Site('regat_site').primary(),
            GDT_User('regat_user').primary(),
            GDT_UserName('regat_onsite_name').maxlen(64).not_null(),
            GDT_Score('regat_score'),
            GDT_Score('regat_onsite_score'),
            GDT_UInt('regat_onsite_solved'),
            GDT_Rank('regat_onsite_rank'),
            GDT_Created('regat_first_link'),
            GDT_Edited('regat_last_link'),
        ]

    def get_user(self) -> GDO_User:
        return self.gdo_value('regat_user')

