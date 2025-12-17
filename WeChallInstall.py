from gdo.core.GDO_File import GDO_File
from gdo.core.GDO_Permission import GDO_Permission
from gdo.core.GDO_User import GDO_User
from gdo.core.GDO_UserPermission import GDO_UserPermission
from gdo.wechall.module_wechall import module_wechall
from gdo.wechall.GDT_SiteState import GDT_SiteState
from gdo.wechall.WeChallConstants import WeChallConstants
from gdo.wechall.WC_Site import WC_Site


class WeChallInstall:

    @classmethod
    async def on_install(cls):
        await cls.site_admin_permissions()
        cls.create_wechall()

    @classmethod
    def create_wechall(cls):
        WC_Site.blank({
            'site_id': '107',
            'site_status': GDT_SiteState.UP,
            'site_name': 'PyGDO-WeChall',
            'site_short_name': 'WC2',
            'site_class_name': 'Base',
            'site_description': 'A remake of WeChall in PyGDO. Old site is linked as WeChallPHP.',
        }).soft_replace()
        mod = module_wechall.instance()
        if not mod.cfg_default_logo():
            file = GDO_File.from_path(mod.file_path('img/default_logo.png')).insert()
            mod.save_config_val('default_logo', file.get_id())

    @classmethod
    async def site_admin_permissions(cls):
        permission = GDO_Permission.get_or_create(WeChallConstants.PERM_SITE_ADMIN)
        for admin in GDO_User.admins():
            await GDO_UserPermission.grant_permission(admin, permission)
