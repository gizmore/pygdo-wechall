from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.net.GDT_Redirect import GDT_Redirect
from gdo.ui.GDT_Page import GDT_Page
from gdo.ui.GDT_Success import GDT_Success
from gdo.wechall.WC_SiteAdmin import WC_SiteAdmin


class add_site_admin(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        t = WC_SiteAdmin.blank()
        form.add_fields(
            t.column('sa_site'),
            t.column('sa_user'),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        sa = WC_SiteAdmin.blank(self.param_vals()).insert()
        GDT_Page.flash(GDT_Success().text('msg_wc_added_site_admin', (sa.get_user().render_name(), sa.get_site().render_name())))
        return GDT_Redirect().href(href('wechall', 'site_admins'))
