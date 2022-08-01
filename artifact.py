import enum


artifactsTypes = {
    1: 'Weapon',
    2: 'Helmet',
    3: 'Shield',
    4: 'Gloves',
    5: 'Armor',
    6: 'Boots'
}


class RARITIES(enum.IntEnum):
    REGULAR = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


class Artifact:
    def __init__(self, type=None, set=None, rarity=None, rank=None, primaryStat=None, subStats=None):
        self._type = type
        self._set = set
        self._rarity = rarity
        self._rank = rank
        self._primaryStat = primaryStat
        self._subStats = subStats

    @property
    def type(self):
        return self._type

    @property
    def set(self):
        return self._set

    @property
    def rarity(self):
        return self._rarity

    @property
    def rank(self):
        return self._rank

    @property
    def primaryStat(self):
        return self._primaryStat

    @property
    def subStats(self):
        return self._subStats

    def _viewPrimaryStat(self):
        return f'''
        type: {self.primaryStat['statType']}
        subtype: {self.primaryStat['statSubType']}
        value: {self.primaryStat['value']}
    '''

    def _viewSubStats(self):
        for stat in self.subStats:
            yield f'''
        Type: {stat['statType']}
        Sub type: {stat['statSubType']}
        Value: {stat['value']}'''

    def __str__(self):
        result = f'''Artifact
    type: {self.type}
    set: {self.set}
    rarity: {RARITIES(self.rarity).name}
    rank: {self.rank}
    '''

        result += 'Primary stat: '
        result += self._viewPrimaryStat()

        result += 'Sub stats: '
        subStats = list(self._viewSubStats())
        if not subStats:
            result += 'None'
        for stat in subStats:
            result += stat + '\n'

        return result if result[-1] != '\n' else result[:-1]
