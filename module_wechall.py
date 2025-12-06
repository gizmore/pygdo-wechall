from gdo.base.GDO_Module import GDO_Module
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.WC_SiteVote import WC_SiteVote


class module_wechall(GDO_Module):

    def gdo_classes(self):
        return [
            WC_Site,
            WC_SiteVote,
        ]
    