from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Link import GDT_Link
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.WC_SiteDescription import WC_SiteDescription
from gdo.wechall.WC_SiteTags import WC_SiteTags
from gdo.wechall.WC_SiteVoteDiff import WC_SiteVoteDiff
from gdo.wechall.WC_SiteVoteFun import WC_SiteVoteFun


class module_wechall(GDO_Module):

    def gdo_classes(self):
        return [
            WC_Site,
            WC_SiteDescription,
            WC_SiteTags,
            WC_SiteVoteDiff,
            WC_SiteVoteFun,
        ]

    def gdo_dependencies(self) -> list:
        return [
            'bootstrap5',
            'contact',
            'country',
            'forum',
            'vote',
        ]

    def gdo_admin_links(self) -> list[GDT_Link]:
        return [
            GDT_Link().href(self.href('import_wc5')).text('btn_import_wc5'),
        ]
