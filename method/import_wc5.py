from gdo.base.Database import Database
from gdo.core.GDO_User import GDO_User
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm


class import_wc5(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    async def form_submitted(self):
        db = Database('localhost', 'wechall', 'wechall', 'wechall')
        result = db.select("SELECT * FROM wc4_user")
        while row := result.fetch_assoc():
            pass
            # GDO_User.blank({}).insert()
        return self.render_page()
