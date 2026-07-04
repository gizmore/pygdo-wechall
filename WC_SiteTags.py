from gdo.base.GDO import GDO
from gdo.tags.GDO_TagObject import GDO_TagObject


class WC_SiteTags(GDO_TagObject):

    def gdo_tags_table(self) -> GDO:
        from gdo.wechall.WC_SiteTag import WC_SiteTag
        return WC_SiteTag.table()

    def gdo_tag_object_table(self) -> GDO:
        from gdo.wechall.WC_Site import WC_Site
        return WC_Site.table()
