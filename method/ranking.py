from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Query import Query
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Bool import GDT_Bool
from gdo.country.GDT_Country import GDT_Country
from gdo.date.Time import Time
from gdo.table.MethodQueryTable import MethodQueryTable
from gdo.ui.GDT_Rank import GDT_Rank
from gdo.ui.GDT_Score import GDT_Score
from gdo.user.GDT_ProfileLink import GDT_ProfileLink
from gdo.wechall.GDT_SiteProgressIcons import GDT_SiteProgressIcons
from gdo.wechall.WC_RegAt import WC_RegAt


class ranking(MethodQueryTable):

    def gdo_cached(cls) -> int:
        return Time.ONE_MINUTE * 15

    def gdo_searched(self) -> bool:
        return False

    def gdo_filtered(self) -> bool:
        return False

    def gdo_ordered(self) -> bool:
        return False

    def gdo_paginate_size(self) -> int:
        return 100

    def gdo_table(self) -> GDO:
        return GDO_User.table()

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Bool('alltime').initial('0'),
        ]

    def gdo_table_query(self) -> Query:
        query = WC_RegAt.table().select()
        query.select('SUM(regat_score) score')
        query.join_object('regat_user')
        query.join_object('regat_site')
        GDO_User.join_setting(query, 'country_ethnics', 'country', 'regat_user_t')
        query.order('score DESC')
        query.group('regat_user')
        query.where("user_server = 2 AND user_type in ('member') ")
        if not self.param_value('alltime'): query.where("site_status = 'up'")
        query.fetch_as(GDO_User.table())
        return query

    def gdo_table_headers(self) -> list[GDT]:
        return [
            GDT_Rank('rank'),
            GDT_Country('country'),
            GDT_Score('score'),
            GDT_ProfileLink('link').with_avatar(),
            GDT_SiteProgressIcons('progress').joined(),
        ]

    def render_country(self, country, user) -> str:
        return country.render_html()

    # def render_link(self, link, user) -> str:
    #     return link.render_cell()
