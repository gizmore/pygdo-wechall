from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDO_UserPermission import GDO_UserPermission
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.WeChallConstants import WeChallConstants


class WC_SiteAdmin(GDO):

    @classmethod
    def add_site_admin(cls, user: GDO_User, site: WC_Site):
        cls.blank({
            'sa_site': site.get_id(),
            'sa_user': user.get_id(),
        }).soft_replace()
        GDO_UserPermission.grant(user, WeChallConstants.PERM_SITE_ADMIN)

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Site('sa_site').primary().cascade_delete(),
            GDT_User('sa_user').primary().cascade_delete(),
            GDT_Creator('sa_creator'),
            GDT_Created('sa_created'),
        ]

    def get_site(self) -> WC_Site:
        return self.gdo_value('sa_site')

    def get_site_admin(self) -> GDO_User:
        return self.gdo_value('sa_user')
