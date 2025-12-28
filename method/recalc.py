from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_Site import WC_Site


class recalc(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_Site('site').positional())
        super().gdo_create_form(form)

    def get_site(self) -> WC_Site:
        return self.param_value('site')

    def form_submitted(self):
        if site := self.get_site():
            sites = [site]
        else:
            sites = WC_Site.all_joined()
        for site in sites:
            site.recalc_site()
        return self.msg('msg_wechall_calced')
