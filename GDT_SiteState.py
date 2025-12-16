from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum


class GDT_SiteState(GDT_Enum):

    UP = 'up'
    DOWN = 'down'
    DEAD = 'dead'
    WANTED = 'wanted'
    REFUSED = 'refused'
    CONTACTED = 'contacted'
    COMING_SOON = 'coming_soon'

    def gdo_choices(self) -> dict:
        return {
            self.UP: t('wcss_up'),
            self.DOWN: t('wcss_down'),
            self.DEAD: t('wcss_dead'),
            self.WANTED: t('wcss_wanted'),
            self.REFUSED: t('wcss_refused'),
            self.CONTACTED: t('wcss_contacted'),
            self.COMING_SOON: t('wcss_coming_soon'),
        }

    def render_txt(self) -> str:
        return t(f"wcss_{self.get_val()}")
