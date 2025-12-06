from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_Secret import GDT_Secret
from gdo.core.GDT_String import GDT_String
from gdo.core.GDT_UInt import GDT_UInt
from gdo.country.GDT_Country import GDT_Country
from gdo.date.GDT_Date import GDT_Date
from gdo.language.GDT_Language import GDT_Language
from gdo.net.GDT_Url import GDT_Url
from gdo.ui.GDT_Image import GDT_Image
from gdo.ui.GDT_Score import GDT_Score
from gdo.wechall.GDT_SiteState import GDT_SiteState


class WC_Site(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('site_id'),
            GDT_SiteState('site_status').initial(GDT_SiteState.COMING_SOON).not_null(),

            GDT_String('site_name').maxlen(48).not_null(),
            GDT_Name('site_classname').maxlen(12).not_null(),
            GDT_Image('site_logo'),

            GDT_Country('site_country'),
            GDT_Language('site_language'),

            GDT_Date('site_joindate'),
            GDT_Date('site_launchdate'),

            GDT_Secret('site_authkey').ascii().case_s().maxlen(32),
            GDT_Secret('site_xauthkey').ascii().case_s().maxlen(32),

            GDT_String('site_irc'),
            GDT_String('site_discord'),
            GDT_String('site_telegram'),
            GDT_String('site_signal'),
            GDT_String('site_whatsapp'),

            GDT_Url('site_url').reachable(),
            GDT_String('site_url_mail'),
            GDT_String('site_url_score'),
            GDT_String('site_url_profile'),

            GDT_Score('site_score'),
            GDT_Score('site_basescore').initial('10000'),
            GDT_Score('site_avg'),

            GDT_UInt('site_maxscore'),
            GDT_UInt('site_challcount'),
            GDT_UInt('site_usercount'),
            GDT_UInt('site_linkcount'),

            # Votes
        # 'site_dif' = > array(GDO::DECIMAL, 3.0, array(5, 4)),
        # 'site_fun' = > array(GDO::DECIMAL, 3.0, array(5, 4)),
        # // 'site_vote_dif' = > array(GDO::OBJECT, GDO::NOT_NULL, array('GWF_VoteScore', 'site_vote_dif')),  # votes
        # // 'site_vote_fun' = > array(GDO::OBJECT, GDO::NOT_NULL, array('GWF_VoteScore', 'site_vote_fun')),  # votes
        # 'site_vote_dif' = > array(GDO::UINT, 0),  # GDO::NOT_NULL, array('GWF_VoteScore', 'site_vote_dif')), # votes
        # 'site_vote_fun' = > array(GDO::UINT, 0),  # OBJECT, GDO::NOT_NULL, array('GWF_VoteScore', 'site_vote_fun')), # votes

        # 'site_visit_in' = > array(GDO::UINT, 0),  # How many visitors go that site
        # 'site_visit_out' = > array(GDO::UINT, 0),  # How many visitors come from that site
        # 'site_options' = > array(GDO::UINT | GDO::INDEX, 0),

        # 'site_boardid' = > array(GDO::UINT, 0),  # Linked Forumboard
        # 'site_threadid' = > array(GDO::UINT, 0),  # Linked Mainthread

        # 'site_tags' = > array(GDO::TEXT | GDO::UTF8 | GDO::CASE_I),  # Exploit,Crypto,
        # 'site_tagbits' = > array(GDO::UINT | GDO::INDEX, 0),  # 0x01a204b (Tags as bits)

        # 'site_color' = > array(GDO::CHAR | GDO::ASCII | GDO::CASE_S, GDO::NULL, 6),
        #
        # 'site_spc' = > array(GDO::UINT, 25),
        # 'site_powarg' = > array(GDO::UINT, 100),
        #
        # 'site_descr_lid' = > array(GDO::UINT, 1),

        ]
