from artifact import artifactsTypes, Artifact, RARITIES
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
# проверяем чтобы сумма вероятностей выпадения предметов была равна 1.
# Если где-то провтыкали - увидем ошибку сразу


class Forge:
    def __init__(self, nameSet=None):
        print('Forge call')
        self._nameSet = None

    def choiseSet(self, nameSet):
        self._nameSet = nameSet

    def createArtifact(self):
        rank = random.randint(1, 7)
        # rarity = random.choice(list(artifactsRaritys.values()))
        rarity = self._generateRarity()

        type = random.choice(list(artifactsTypes.values()))
        primaryStat = None
        substats = [self._getStat() for stat in range(rarity) if rarity != 0]
        print(rarity)
        print(substats)
        return Artifact(type, self._nameSet, rarity, rank, primaryStat, substats)

    def _getPrimaryStat(self):
        pass

    def _getStat(self):
        """
        Отправить запрос
        """
        return 'stat'

    def _generateRarity(self):
        # тут получаем рендомное число от 0 до 1. И проходимся по словарю с вероятностями. И проверяем отрезки
        #  с вероятностями. Например, если первым из словаря попадется RARITIES.RARE с вероятностью 0.15 то
        #  чтобы соответстновать этой вероятности value должно быть от 0 до 0.15. А если потом вторым например
        #  RARITIES.REGULAR, то value должно попасть уже в следующий отрезок от 0.15 до 0.55. Ну и так
        #  делим все на отрезки пока не дойдем до 1.
        value = random.random()

        currentRange = 0
        for rarity, chance in _RARITIES_RANDOM_RATES.items():
            if value <= currentRange and value <= currentRange + chance:
                return rarity
            currentRange += chance

        # сюда мы вообще никогда попасть не должны. По этому кинем ошибку
        raise Exception(
            "Abnormal behavior. Probably problems with _RARITIES_RANDOM_RATES")
        return RARITIES.REGULAR


g_forge = Forge()
g_forge.choiseSet('None')
print(g_forge.createArtifact())
