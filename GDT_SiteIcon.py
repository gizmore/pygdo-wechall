from gdo.ui.GDT_Image import GDT_Image


class GDT_SiteIcon(GDT_Image):

    def __init__(self, name: str):
        super().__init__(name)

    def render_html(self) -> str:
        return super().render_html()