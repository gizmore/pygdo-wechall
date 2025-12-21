from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Container import GDT_Container


class about(Method):
    def gdo_execute(self) -> GDT:
        return  GDT_Container().vertical()
