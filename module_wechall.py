from gdo.base.GDO_Module import GDO_Module
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.WC_SiteVoteDiff import WC_SiteVoteDiff
from gdo.wechall.WC_SiteVoteFun import WC_SiteVoteFun


class module_wechall(GDO_Module):

    def gdo_classes(self):
        return [
            WC_Site,
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
