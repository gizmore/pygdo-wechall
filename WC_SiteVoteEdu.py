from gdo.vote.GDO_VoteTable import GDO_VoteTable
from gdo.vote.WithVotes import WithVotes
from gdo.base.GDO import GDO

class WC_SiteVoteEdu(GDO_VoteTable):

    def gdo_vote_object_table(self) -> 'GDO|WithVotes':
        from gdo.wechall.WC_Site import WC_Site
        return WC_Site.table()

    def gdo_min_vote_score(self) -> int:
        return 4

    def gdo_max_vote_score(self) -> int:
        return 7
