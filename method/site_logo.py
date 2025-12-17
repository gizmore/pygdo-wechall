from gdo.base.GDT import GDT
from gdo.file.MethodFile import MethodFile
from gdo.ui.GDT_Image import GDT_Image
from gdo.wechall.module_wechall import module_wechall
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_Site import WC_Site


class site_logo(MethodFile):

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Site('site').not_null(),
        ]

    def get_site(self) -> WC_Site:
        return self.param_value('site')

    def gdo_execute(self) -> GDT:
        file = GDT_Image.column(self.get_site(), 'site_logo').get_file() or module_wechall.instance().cfg_default_logo()
        return self.render_file(file[0]) if file else self.empty()
