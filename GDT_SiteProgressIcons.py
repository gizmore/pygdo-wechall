from gdo.base.GDT import GDT
from gdo.base.WithName import WithName
from gdo.core.WithGDO import WithGDO
from gdo.wechall.GDT_SiteState import GDT_SiteState


class GDT_SiteProgressIcons(WithGDO, WithName, GDT):

    _states: list[str]

    def __init__(self, name: str):
        super().__init__()
        self._states = []
        self._name = name

    def joined(self):
        self._states = [GDT_SiteState.UP, GDT_SiteState.DOWN]
        return self

    def render_label(self) -> str:
        return ''

    def render_html(self) -> str:
        return ''

    def render_cell(self) -> str:
        return 'ABC'
