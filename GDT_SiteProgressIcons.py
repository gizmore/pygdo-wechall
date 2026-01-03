from gdo.core.GDT_Field import GDT_Field
from gdo.wechall.WC_Site import WC_Site


class GDT_SiteProgressIcons(GDT_Field):

    def __init__(self, name: str):
        super().__init__(name)

    def render_label(self) -> str:
        return ''

    def render_html(self) -> str:
        return ''

    def active_sites(self) -> list[WC_Site]:
        return WC_Site.all_joined()

    def render_cell(self) -> str:
        back = '<div class="wc_progress_cell">'
        for site in self.active_sites():
            data = self.get_data(site)
            back += site.render_progress_icon(self._gdo, data[0], data[1])
        back += '</div>'
        return back

    def to_value(self, val: str):
        back = {}
        for data in val.split(','):
            site_id, score, wc_score = data.split(':')
            back[site_id] = (int(score), int(wc_score))
        return back

    def get_data(self, site: WC_Site) -> tuple[int, int]:
        if v := self.get_value():
            return v.get(site.get_id(), (0, 0))
        return 0, 0
