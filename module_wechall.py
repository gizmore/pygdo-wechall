from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page

from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Link import GDT_Link

from gdo.wechall.WC_RegAt import WC_RegAt
from gdo.wechall.WC_SiteVoteEdu import WC_SiteVoteEdu
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.WC_SiteTags import WC_SiteTags
from gdo.wechall.WC_SiteVoteDiff import WC_SiteVoteDiff
from gdo.wechall.WC_SiteVoteFun import WC_SiteVoteFun


class module_wechall(GDO_Module):

    def gdo_classes(self):
        return [
            WC_Site,
            WC_SiteTags,
            WC_SiteVoteDiff,
            WC_SiteVoteEdu,
            WC_SiteVoteFun,
            WC_RegAt,
        ]

    def gdo_dependencies(self) -> list:
        return [
            'bootstrap5',
            'contact',
            'country',
            'forum',
            'likes',
            'markdown',
            'vote',
        ]

    def gdo_admin_links(self) -> list[GDT_Link]:
        return [
            GDT_Link().href(self.href('import_wc5')).text('btn_import_wc5'),
        ]

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        page._top_bar.add_field(
            GDT_Link().href(self.href('sites')).text('mt_wechall_sites'),
        )
