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
            self.UP: self.UP,
            self.DOWN: self.DOWN,
            self.DEAD: self.DEAD,
            self.WANTED: self.WANTED,
            self.REFUSED: self.REFUSED,
            self.CONTACTED: self.CONTACTED,
            self.COMING_SOON: self.COMING_SOON,
        }
