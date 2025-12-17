from gdo.core.GDT_UserName import GDT_UserName
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.mail.GDT_Email import GDT_Email
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_Site import WC_Site


class link_site(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Site('site').linkable().not_null(),
            GDT_UserName('onsite_name').not_null(),
            GDT_Email('onsite_mail').not_null(),
        )
        super().gdo_create_form(form)

    def get_site(self) -> WC_Site:
        return self.param_value('site')

    def form_submitted(self):
        site = self.get_site()
        name = self.param_val('onsite_name')
        mail = self.param_val('onsite_mail')

