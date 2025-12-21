from gdo.base.Trans import t, sitename
from gdo.base.util.href import href
from gdo.core.GDT_UserName import GDT_UserName
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.mail.GDT_Email import GDT_Email
from gdo.mail.Mail import Mail
from gdo.ui.GDT_Link import GDT_Link
from gdo.wechall.GDT_Site import GDT_Site
from gdo.wechall.WC_RegAt import WC_RegAt
from gdo.wechall.WC_Site import WC_Site
from gdo.wechall.method.link_site_token import link_site_token


class link_site(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Site('site').linkable().not_null(),
            GDT_UserName('user').not_null(),
            GDT_Email('email').not_null().initial(self._env_user.get_mail()),
        )
        super().gdo_create_form(form)

    def get_site(self) -> WC_Site:
        return self.param_value('site')

    def form_submitted(self):
        site = self.get_site()
        name = self.param_val('user')
        mail = self.param_val('email')
        if mail.lower() == self._env_user.get_mail().lower():
            return self.link_site(site, name)
        self.send_mail(site, name, mail)
        return self.msg('msg_wc_link_mail_sent')

    def link_site(self, site: WC_Site, name: str) -> GDT_Site:
        return WC_RegAt.link(self._env_user, site, name)

    def send_mail(self, site: WC_Site, name: str, mail: str):
        mail = Mail.from_bot()
        mail.subject(t('mt_wechall_link_site'))
        mail.body(t('mbody_wc_link', (
            self._env_user.render_name(),
            site.render_name(),
            sitename(),
            GDT_Link().href(href('wechall', 'link_site_token', f"&token={link_site_token.token(self._env_user, site, name, mail)}")),
        )))
        mail.recipient(mail, self._env_user.render_name())
        mail.send()

