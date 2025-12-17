from gdo.base.Cache import gdo_cached
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Trans import t
from gdo.base.util.href import href
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Editor import GDT_Editor
from gdo.core.GDT_Float import GDT_Float
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_Secret import GDT_Secret
from gdo.core.GDT_Select import GDT_Select
from gdo.core.GDT_String import GDT_String
from gdo.core.GDT_UInt import GDT_UInt
from gdo.country.GDT_Country import GDT_Country
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Date import GDT_Date
from gdo.date.GDT_Edited import GDT_Edited
from gdo.forum.GDT_Board import GDT_Board
from gdo.forum.GDT_Thread import GDT_Thread
from gdo.language.GDT_Language import GDT_Language
from gdo.message.GDT_Message import GDT_Message
from gdo.net.GDT_Url import GDT_Url
from gdo.ui.GDT_Color import GDT_Color
from gdo.ui.GDT_Image import GDT_Image
from gdo.ui.GDT_Score import GDT_Score
from gdo.vote.GDT_VoteCount import GDT_VoteCount
from gdo.vote.GDT_VoteResult import GDT_VoteResult
from gdo.wechall.GDT_SiteState import GDT_SiteState
from gdo.wechall.WCException import WCException
from gdo.wechall.WC_SiteVoteDiff import WC_SiteVoteDiff
from gdo.wechall.WC_SiteVoteFun import WC_SiteVoteFun


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.wechall.WC_RegAt import WC_RegAt


class WC_Site(GDO):

    @classmethod
    @gdo_cached(cache_key='wc_site_count')
    def num_sites(cls) -> int:
        return cls.table().count_where(cls.where_joined())

    @classmethod
    @gdo_cached(cache_key='wc_sites_joined')
    def all_joined(cls) -> list[WC_Site]:
        return cls.table().select().where(cls.where_joined()).exec().fetch_all()

    @classmethod
    def where_joined(cls):
        return "site_status IN ('up', 'down', 'coming_soon')"

    def gdo_real_class(cls, vals: dict[str,str]) -> type[GDO]:
        from gdo.wechall.site.MAPPING import MAPPING
        return MAPPING.MAPPING.get(vals['site_class_name'], WC_Site)

    def gdo_table_name(cls) -> str:
        return 'wc_site'

    def gdo_columns(self) -> list[GDT]:
        from gdo.wechall.site.MAPPING import MAPPING
        return [
            GDT_AutoInc('site_id'),
            GDT_SiteState('site_status').initial(GDT_SiteState.COMING_SOON).not_null().label('status'),

            GDT_String('site_name').maxlen(48).not_null().label('name'),
            GDT_Name('site_short_name').maxlen(12).not_null().label('short_name'),
            GDT_Select('site_class_name').maxlen(16).not_null().choices(MAPPING.MAPPING).label('class_name'),
            GDT_Message('site_description').maxlen(16384).label('description'),

            GDT_Image('site_logo').label('logo').width(32).height(32),
            GDT_Color('site_fg_color').label('fg_color'),
            GDT_Color('site_bg_color').label('bg_color'),

            GDT_Country('site_country').label('country'),
            GDT_Language('site_language').label('language'),

            GDT_Date('site_join_date').label('join_date'),
            GDT_Date('site_launch_date').label('launch_date'),

            GDT_Secret('site_authkey').ascii().case_s().maxlen(32),
            GDT_Secret('site_x_authkey').ascii().case_s().maxlen(32),

            GDT_String('site_irc').label('irc'),
            GDT_String('site_discord').label('discord'),
            GDT_String('site_telegram').label('telegram'),
            GDT_String('site_signal').label('signal'),
            GDT_String('site_whatsapp').label('whatsapp'),

            GDT_Board('site_board').label('board'),
            GDT_Thread('site_thread').label('thread'),

            GDT_Url('site_url').reachable().label('url'),
            GDT_String('site_url_mail'),
            GDT_String('site_url_score'),
            GDT_String('site_url_profile'),

            GDT_Score('site_score').label('score'),
            GDT_Score('site_base_score').initial('10000').label('base_score'),
            GDT_UInt('site_pow_arg').not_null().initial('100'),
            GDT_Float('site_avg'),

            GDT_UInt('site_max_score').label('max_score'),
            GDT_UInt('site_chall_count').label('chall_count'),
            GDT_UInt('site_user_count').label('user_count'),

            GDT_VoteCount('site_vote_dif').table(WC_SiteVoteDiff.table()).label('num_votes_dif'),
            GDT_VoteCount('site_vote_edu').table(WC_SiteVoteDiff.table()).label('num_votes_edu'),
            GDT_VoteCount('site_vote_fun').table(WC_SiteVoteFun.table()).label('num_votes_fun'),

            GDT_VoteResult('site_dif').table(WC_SiteVoteDiff.table()).label('difficulty'),
            GDT_VoteResult('site_edu').table(WC_SiteVoteDiff.table()).label('education'),
            GDT_VoteResult('site_fun').table(WC_SiteVoteFun.table()).label('fun'),

            GDT_UInt('site_visit_in').not_null().initial('0'),
            GDT_UInt('site_visit_out').not_null().initial('0'),

            GDT_Edited('site_edited'),
            GDT_Editor('site_editor'),

            GDT_Created('site_created'),
            GDT_Creator('site_creator'),

            GDT_Bool('site_auto_update').not_null().initial('0'),
            GDT_Bool('site_hide_default').not_null().initial('0'),
            GDT_Bool('site_has_onsite_rank').not_null().initial('0'),
            GDT_Bool('site_no_urlencode').not_null().initial('0'),
            GDT_Bool('site_no_v1_scripts').not_null().initial('0'),
            GDT_Bool('site_onsitename_case_s').not_null().initial('0'),
            GDT_Bool('site_linear_challs').not_null().initial('0'),
            GDT_Bool('site_has_no_email').not_null().initial('0'),
        ]

    def __str__(self):
        return self.render_name()

    def __repr__(self):
        return self.render_name()

    def get_url(self) -> str:
        return self.gdo_val('site_url')

    ###########
    # Scoring #
    ###########

    def update_scores(self, regat: 'WC_RegAt') -> bool:
        raise WCException(t('err_not_implemented'))

    ##########
    # Render #
    ##########
    def render_name(self):
        return self.gdo_val('site_name')

    def render_icon(self):
        icon = GDT_Image.column(self, 'site_logo')
        file = icon.get_file() or ModuleLoader.instance().get_module('wechall').cfg_default_logo()
        if file: file = file[0].get_id()
        return icon.href(href('wechall', 'site_logo', f'&site={self.get_id()}&file={file}')).render_html()
