from gdo.base.GDO import GDO
from gdo.tags.GDO_Tag import GDO_Tag


class WC_SiteTag(GDO_Tag):

    def gdo_tag_object_table(self) -> GDO:
        from gdo.wechall.WC_SiteTags import WC_SiteTags
        return WC_SiteTags.table()
