from gdo.vote.GDO_VoteTable import GDO_VoteTable
from gdo.wechall.WC_Site import WC_Site
from gdo.vote.WithVotes import WithVotes
from gdo.base.GDO import GDO

class WC_SiteVote(GDO_VoteTable):

    def gdo_votes_table(self) -> 'GDO_VoteTable':
        raise self

    def gdo_vote_object_table(self) -> 'GDO|WithVotes':
        return WC_Site.table()

    def gdo_min_vote_score(self) -> int:
        return 1

    def gdo_max_vote_score(self) -> int:
        return 10

