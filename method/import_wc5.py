from functools import lru_cache

from gdo.base.Database import Database
from gdo.base.Util import gdo_print
from gdo.core.GDO_Server import GDO_Server
from gdo.core.GDO_User import GDO_User
from gdo.core.GDO_UserSetting import GDO_UserSetting
from gdo.core.GDT_Bool import GDT_Bool
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.wechall.WC_RegAt import WC_RegAt
from gdo.wechall.WC_RegAtHistory import WC_RegAtHistory
from gdo.wechall.WC_Site import WC_Site


class SiteOptions:
    AUTO_UPDATE = 0x01
    HIDE_BY_DEFAULT = 0x02
    HAS_LOGO = 0x04
    ONSITE_RANK = 0x08
    NO_URLENCODE = 0x10
    NO_V1_SCRIPTS = 0x20
    LINK_CASE_S = 0x40
    LINEAR = 0x80
    NO_EMAIL = 0x100

class ImportUtil:
    @staticmethod
    def date_convert_from_gwf3(ts: str) -> str|None:
        ts = ts.strip()
        if not ts or set(ts) == {'0'}:
            return None
        parts = {
            'Y': ts[0:4],
            'm': ts[4:6] if len(ts) >= 6 else '01',
            'd': ts[6:8] if len(ts) >= 8 else '01',
            'H': ts[8:10] if len(ts) >= 10 else '00',
            'i': ts[10:12] if len(ts) >= 12 else '00',
            's': ts[12:14] if len(ts) >= 14 else '00',
            'n': ts[14:20] if len(ts) >= 20 else '000000',
        }
        return (
            f"{parts['Y']}-{parts['m']}-{parts['d']} "
            f"{parts['H']}:{parts['i']}:{parts['s']}."
            f"{parts['n']}"
        )

    @classmethod
    @lru_cache(maxsize=None)
    def userid(cls, user_id: str) -> str|None:
        return GDO_UserSetting.select('uset_user').where(f'uset_key="wc1_id" AND uset_val="{user_id}"').exec().fetch_val()

class import_wc5(MethodForm):

    USER_MAPPING: dict[str, tuple[dict[str, str], GDO_User]] = {}

    def gdo_transactional(self) -> bool:
        return False

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Bool('sites').initial('1'),
            GDT_Bool('users').initial('1'),
            GDT_Bool('regat').initial('1'),
            GDT_Bool('user_history').initial('1'),
            GDT_Bool('site_history').initial('1'),
        )
        super().gdo_create_form(form)

    async def form_submitted(self):
        db = Database('localhost', 'wechall', 'wechall', 'wechall')
        if self.param_value('sites'): await self.import_sites(db)
        if self.param_value('users'): await self.import_users(db)
        if self.param_value('regat'): await self.import_regat(db)
        if self.param_value('user_history'): await self.import_regat_history(db)
        if self.param_value('site_history'): await self.import_site_history(db)
        return self.render_page()

    async def import_sites(self, db: Database):
        result = db.select("SELECT * FROM wc4_wc_site LEFT JOIN wc4_country ON wc4_country.country_id = site_country LEFT JOIN wc4_language ON wc4_language.lang_id = site_language")
        while row := result.fetch_assoc():
            opts = int(row['site_options'])
            WC_Site.blank({
                'site_id': row['site_id'],
                'site_status': row['site_status'],
                'site_name': row['site_name'],
                'site_class_name': row['site_classname'],
                'site_short_name': row['site_classname'],
                'site_fg_color': 'ff'+(row['site_color'] if row['site_color'] else '000000'),

                'site_country': row['country_tld'].upper(),
                'site_language': row['lang_iso'].lower(),

                'site_join_date': ImportUtil.date_convert_from_gwf3(row['site_joindate']),
                'site_launch_date': ImportUtil.date_convert_from_gwf3(row['site_launchdate']),

                'site_authkey': str(row['site_authkey']),
                'site_x_authkey': str(row['site_xauthkey']),

                'site_irc': (row['site_irc']),
                'site_discord': (row['site_discord']),
                'site_telegram': (row['site_telegram']),
                'site_signal': (row['site_signal']),
                'site_whatsapp': (row['site_whatsapp']),

                'site_board': None,
                'site_thread': None,

                'site_url': row['site_url'],
                'site_url_mail': row['site_url_mail'],
                'site_url_score': row['site_url_score'],
                'site_url_profile': row['site_url_profile'],

                'site_score': row['site_score'],
                'site_base_score': row['site_basescore'],
                'site_pow_arg': row['site_powarg'],
                'site_avg': row['site_avg'],

                'site_max_score': None if int(row['site_maxscore']) <= 0 else row['site_maxscore'],
                'site_chall_count': None if int(row['site_challcount']) <= 0 else row['site_challcount'],
                'site_user_count': None if int(row['site_usercount']) <= 0 else row['site_usercount'],

                'site_auto_update': '1' if opts & SiteOptions.AUTO_UPDATE else '0',
                'site_hide_default': '1' if opts & SiteOptions.HIDE_BY_DEFAULT else '0',
                'site_has_onsite_rank': '1' if opts & SiteOptions.ONSITE_RANK else '0',
                'site_no_urldecode': '1' if opts & SiteOptions.NO_URLENCODE else '0',
                'site_no_v1_scripts': '1' if opts & SiteOptions.NO_V1_SCRIPTS else '0',
                'site_onsitename_case_s': '1' if opts & SiteOptions.LINK_CASE_S else '0',
                'site_linear_challs': '1' if opts & SiteOptions.LINEAR else '0',
                'site_has_no_email': '1' if opts & SiteOptions.NO_EMAIL else '0',
            }).soft_replace()

    async def import_users(self, db: Database):
        result = db.select("SELECT * FROM wc4_user")
        web = GDO_Server.get_by_connector('web')
        count = 0
        while row := result.fetch_assoc():
            new_user = await web.get_or_create_user(row['user_name'])
            self.USER_MAPPING[row['user_id']] = (row, new_user)
            new_user.save_setting('wc1_id', row['user_id'])
            count += 1
            if count % 1000 == 0:
                gdo_print("Importing users: " + str(count))

    async def import_regat(self, db: Database):
        result = db.select("SELECT * FROM wc4_wc_regat")
        columns = WC_RegAt.table().columns_only('regat_site', 'regat_user', 'regat_onsite_name', 'regat_onsite_score', 'regat_onsite_solved', 'regat_onsite_rank', 'regat_first_link', 'regat_last_link')
        data = []
        while row := result.fetch_assoc():
            data.append([
                row['regat_sid'],
                ImportUtil.userid(row['regat_uid']),
                row['regat_onsitename'],
                row['regat_onsitescore'],
                row['regat_challsolved'],
                row['regat_onsiterank'],
                ImportUtil.date_convert_from_gwf3(row['regat_linkdate']),
                ImportUtil.date_convert_from_gwf3(row['regat_lastdate']),
            ])
        WC_RegAt.table().bulk_insert(columns, data)

    async def import_regat_history(self, db: Database):
        result = db.select("SELECT * FROM wc4_wc_user_history2")
        columns = WC_RegAtHistory.table().columns_only('rh_site', 'rh_user', 'rh_type', 'rh_score', 'rh_percent', 'rh_gain_score', 'rh_gain_percent', 'rh_onsite_score', 'rh_onsite_solved', 'rh_onsite_rank', 'rh_created')
        data = []
        while row := result.fetch_assoc():
            data.append([
                row['userhist_sid'],
                ImportUtil.userid(row['userhist_uid']),
                row['userhist_type'],
                row['userhist_totalscore'],
                str(float(row['userhist_percent']) / 100.0),
                row['userhist_gain_score'],
                str(float(row['userhist_gain_perc']) / 100.0),
                row['userhist_onsitescore'],
                None,
                row['userhist_onsiterank'],
                ImportUtil.date_convert_from_gwf3(row['userhist_date']),
            ])
        WC_RegAtHistory.table().bulk_insert(columns, data)

    async def import_site_history(self, db: Database):
        result = db.select("SELECT * FROM wc4_wc_site_history")
        columns = WC_RegAt.table().columns_only('regat_site', 'regat_user', 'regat_onsite_name', 'regat_onsite_score', 'regat_onsite_solved', 'regat_onsite_rank', 'regat_first_link', 'regat_last_link')
        data = []
        while row := result.fetch_assoc():
            data.append([
                row['regat_sid'],
                ImportUtil.userid(row['regat_uid']),
                row['regat_onsitename'],
                row['regat_onsitescore'],
                row['regat_challsolved'],
                row['regat_onsiterank'],
                ImportUtil.date_convert_from_gwf3(row['regat_linkdate']),
                ImportUtil.date_convert_from_gwf3(row['regat_lastdate']),
            ])
        WC_RegAt.table().bulk_insert(columns, data)

