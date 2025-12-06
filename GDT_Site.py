from gdo.core.GDT_ObjectSelect import GDT_ObjectSelect
from gdo.wechall.WC_Site import WC_Site


class GDT_Site(GDT_ObjectSelect):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(WC_Site.table())
