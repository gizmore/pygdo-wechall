from typing import TYPE_CHECKING

from gdo.base.GDT import GDT
from gdo.core.GDO_File import GDO_File
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_UInt import GDT_UInt
from gdo.ui.GDT_Image import GDT_Image
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_SiteFavs import WC_SiteFavs
from gdo.wechall.WeChallSidebar import WeChallSidebar

if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page

from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Link import GDT_Link
from gdo.wechall.WC_Site import WC_Site


class module_wechall(GDO_Module):

    def __init__(self):
        super().__init__()
        self._priority = 612

    def gdo_classes(self):
        from gdo.wechall.WC_RegAt import WC_RegAt
        from gdo.wechall.WC_SiteVoteEdu import WC_SiteVoteEdu
        from gdo.wechall.WC_Site import WC_Site
        from gdo.wechall.WC_SiteTags import WC_SiteTags
        from gdo.wechall.WC_SiteVoteDiff import WC_SiteVoteDiff
        from gdo.wechall.WC_SiteVoteFun import WC_SiteVoteFun
        from gdo.wechall.WC_RegAtHistory import WC_RegAtHistory
        from gdo.wechall.WC_SiteAdmin import WC_SiteAdmin
        from gdo.wechall.WC_SiteHistory import WC_SiteHistory
        return [
            WC_Site,
            WC_SiteHistory,
            WC_SiteFavs,
            WC_SiteAdmin,
            WC_SiteTags,
            WC_SiteVoteDiff,
            WC_SiteVoteEdu,
            WC_SiteVoteFun,
            WC_RegAt,
            WC_RegAtHistory,
        ]

    def gdo_dependencies(self) -> list:
        return [
            'avatar',
            'bootstrap5',
            'contact',
            'country',
            'forum',
            'likes',
            'markdown',
            'vote',
        ]

    async def gdo_install(self):
        from gdo.wechall.WeChallInstall import WeChallInstall
        await WeChallInstall.on_install()

    def gdo_admin_links(self) -> list[GDT_Link]:
        return [
            GDT_Link().href(self.href('import_wc5')).text('mt_wechall_import_wc5'),
            GDT_Link().href(self.href('recalc')).text('mt_wechall_recalc'),
        ]

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        WeChallSidebar.init_sidebar(page, self)

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_js('js/pygdo-wechall.js')
        self.add_css('css/pygdo-wechall.css')

    ##########
    # Config #
    ##########

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Image('default_logo'),
            GDT_Site('wechall1_site').initial('1').not_null(),
            GDT_Site('wechall2_site').initial('107').not_null(),
        ]

    def cfg_default_logo(self) -> list[GDO_File]:
        return self.get_config_value('default_logo')

    def cfg_wechall1_site(self) -> WC_Site:
        return self.get_config_value('wechall1_site')

    def cfg_wechall2_site(self) -> WC_Site:
        return self.get_config_value('wechall2_site')

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('wc1_id'),
        ]

    def gdo_user_settings(self) -> list[GDT]:
        return [
            GDT_Bool('wc_retired').initial('0').not_null(),
        ]
