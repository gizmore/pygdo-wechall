from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.ui.GDT_Divider import GDT_Divider
from gdo.wechall.WC_Site import WC_Site


class add_site(MethodForm):

    def get_site(self) -> WC_Site:
        return WC_Site.blank()

    def gdo_create_form(self, form: GDT_Form) -> None:
        t = self.get_site()
        form.add_fields(
            t.column('site_status'),
            GDT_Divider().title('naming'),
            t.column('site_name'),
            t.column('site_short_name'),
            t.column('site_class_name'),
            GDT_Divider().title('scoring'),
            t.column('site_base_score'),
            t.column('site_pow_arg'),
            GDT_Divider().title('demographics'),
            t.column('site_country'),
            t.column('site_language'),
            t.column('site_join_date'),
            t.column('site_launch_date'),
            GDT_Divider().title('presentation'),
            t.column('site_description'),
            t.column('site_logo'),
            t.column('site_fg_color'),
            t.column('site_bg_color'),
            GDT_Divider().title('integration'),
            t.column('site_url'),
            t.column('site_url_mail'),
            t.column('site_url_score'),
            t.column('site_url_profile'),
        )
        if self._env_user.is_staff():
            form.add_field(t.column('site_authkey'))
        form.add_fields(
                t.column('site_x_authkey'),
            GDT_Divider().title('socialization'),
            t.column('site_irc'),
            t.column('site_discord'),
            t.column('site_telegram'),
            t.column('site_signal'),
            t.column('site_whatsapp'),
            GDT_Divider().title('options'),
            t.column('site_auto_update'),
            t.column('site_has_onsite_rank'),
            t.column('site_no_urlencode'),
            t.column('site_no_v1_scripts'),
            t.column('site_onsitename_case_s'),
            t.column('site_linear_challs'),
            t.column('site_has_no_email'),
        )

        super().gdo_create_form(form)
