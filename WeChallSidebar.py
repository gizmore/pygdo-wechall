from functools import lru_cache
from typing import TYPE_CHECKING

from gdo.ui.GDT_Bar import GDT_Bar
from gdo.ui.GDT_Divider import GDT_Divider
from gdo.ui.GDT_Link import GDT_Link
from gdo.wechall.WC_Site import WC_Site

if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page
    from gdo.wechall import module_wechall


class WeChallSidebar:
    @classmethod
    def init_sidebar(cls, page: 'GDT_Page', mod: 'module_wechall'):

        page._title_bar.add_fields(
            GDT_Link().href(mod.href('sites')).text('mt_wechall_sites'),
            GDT_Link().href(mod.href('ranking')).text('mt_wechall_ranking'),
        )

        page._left_bar.add_fields(
            GDT_Divider().title_raw(GDT_Link().href(mod.href('sites')).text('link_wc_sites', (WC_Site.num_sites(),)), False),
            cls.sites_bar(),
        )

    @classmethod
    @lru_cache(maxsize=None)
    def sites_bar(cls):
        sites_bar = GDT_Bar().vertical()
        for site in WC_Site.all_joined():
            sites_bar.add_field(GDT_Link().text_raw(site.render_name() + "&nbsp;" + site.render_icon(), False).href(site.get_url()))
        return sites_bar
