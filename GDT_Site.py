from gdo.base.Query import Query
from gdo.core.GDT_ObjectSelect import GDT_ObjectSelect
from gdo.wechall.WC_Site import WC_Site


class GDT_Site(GDT_ObjectSelect):

    _linkable: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._linkable = False
        self.table(WC_Site.table())

    def linkable(self, linkable: bool = True):
        self._linkable = linkable
        return self

    def gdo_query(self) -> Query:
        query =  self._table.select()
        if self._linkable: query.where("site_status='up'")
        return query
