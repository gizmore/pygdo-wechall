from gdo.base.UserTemp import UserTemp
from gdo.base.util.href import href
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.net.GDT_Redirect import GDT_Redirect
from gdo.ui.GDT_Divider import GDT_Divider
from gdo.ui.GDT_Error import GDT_Error
from gdo.ui.GDT_Success import GDT_Success
from gdo.wechall.WC_Site import WC_Site


class add_site(MethodForm):

    def get_site(self) -> WC_Site:
        return WC_Site.table()

    def gdo_create_form(self, form: GDT_Form) -> None:
        t = self.get_site()
        form.add_fields(
            GDT_Divider().title('naming'),
            t.column('site_name', False),
            t.column('site_short_name', False),
            t.column('site_class_name', False),
            GDT_Divider().title('scoring'),
            t.column('site_base_score', False),
            t.column('site_pow_arg', False),
            GDT_Divider().title('demographics'),
            t.column('site_country', False),
            t.column('site_language', False),
            t.column('site_join_date', False),
            t.column('site_launch_date', False),
            GDT_Divider().title('presentation'),
            t.column('site_description', False),
            t.column('site_logo', False),
            t.column('site_fg_color', False),
            t.column('site_bg_color', False),
            GDT_Divider().title('integration'),
            t.column('site_url', False),
            t.column('site_url_mail', False),
            t.column('site_url_score', False),
            t.column('site_url_profile', False),
        )
        if self._env_user.is_staff():
            form.add_field(t.column('site_authkey'))
        form.add_fields(
                t.column('site_x_authkey', False),
            GDT_Divider().title('socialization'),
            t.column('site_irc', False),
            t.column('site_discord', False),
            t.column('site_telegram', False),
            t.column('site_signal', False),
            t.column('site_whatsapp', False),
            GDT_Divider().title('options'),
            t.column('site_status', False),
            t.column('site_auto_update', False),
            t.column('site_has_onsite_rank', False),
            t.column('site_no_urlencode', False),
            t.column('site_no_v1_scripts', False),
            t.column('site_onsitename_case_s', False),
            t.column('site_linear_challs', False),
            t.column('site_has_no_email', False),
        )

        super().gdo_create_form(form)

    def form_submitted(self):
        site = WC_Site.blank(self.param_vals()).insert()
        return self.redirect_msg(href('wechall', 'sites'), 'msg_wc_site_added')
