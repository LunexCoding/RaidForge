from artifact import Artifact, artifactsTypes, RARITIES
from config import g_parserConfigs
import random


_RARITIES_LIST_FOR_RANDOM = set([
    RARITIES.REGULAR, RARITIES.UNCOMMON, RARITIES.RARE, RARITIES.EPIC,
    RARITIES.LEGENDARY
])

_RARITIES_COUNT_SUBSTATS = {
    RARITIES.REGULAR: 0,
    RARITIES.UNCOMMON: 1,
    RARITIES.RARE: 2,
    RARITIES.EPIC: 3,
    RARITIES.LEGENDARY: 4,
}

_RARITIES_RANDOM_RATES = {
    RARITIES.REGULAR: 0.4,
    RARITIES.UNCOMMON: 0.3,
    RARITIES.RARE: 0.15,
    RARITIES.EPIC: 0.1,
    RARITIES.LEGENDARY: 0.05,
}
assert sum(
    _RARITIES_RANDOM_RATES.values()
) == 1


class Forge:
    def __init__(self):
        self._nameSet = None
        self._artifactType = None
        self._artifactRank = None
        self._artifactRarity = None
        self._artifactPrimaryStat = None
        self._artifactSubStats = None

    def choiseSet(self, nameSet):
        self._nameSet = nameSet

    def generateArtifact(self):
        self._artifactType = self._generateArtifactType()
        self._artifactRank = self._generateArtifactRank()
        self._artifactRarity = self._generateRarity()
        self._artifactPrimaryStat = self._generateArtifactPrimaryStat()
        self._artifactSubStats = self._generateArtifactSubStats()
        return Artifact(self._artifactType, self._nameSet, self._artifactRarity, self._artifactRank, self._artifactPrimaryStat, self._artifactSubStats)

    def _generateArtifactType(self):
        return random.choice(list(artifactsTypes.values()))

    def _generateRarity(self):
        value = random.random()

        currentRange = 0
        for rarity, chance in _RARITIES_RANDOM_RATES.items():
            if currentRange <= value and value <= currentRange + chance:
                return rarity
            currentRange += chance

        raise Exception("Abnormal behavior. Probably problems with _RARITIES_RANDOM_RATES")
        return RARITIES.REGULAR

    def _generateArtifactRank(self):
        return random.randint(1, 6)

    def _generateArtifactPrimaryStat(self):
        request = {
            'artifactType': self._artifactType,
            'stat': 'primary',
            'data': {
                'rank': self._artifactRank,
            }
        }
        return g_parserConfigs.requestToGetArtifactParameters(request)

    def _generateArtifactSubStats(self):
        request = {
            'artifactType': self._artifactType,
            'stat': 'sub',
            'data': {
                'rank': self._artifactRank,
                'rarity': _RARITIES_COUNT_SUBSTATS[self._artifactRarity],
                'primaryStat': {
                    'statType': self._artifactPrimaryStat['statType'],
                    'statSubType': self._artifactPrimaryStat['statSubType'],
                }
            }
        }
        return g_parserConfigs.requestToGetArtifactParameters(request)


g_forge = Forge()
