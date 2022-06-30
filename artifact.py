import enum # спец модуль для "перечислений"

artifactsTypes = {
  1: 'Weapon',
  2: 'Helmet',
  3: 'Shield',
  4: 'Gloves',
  5: 'Armor',
  6: 'Boots'
}


artifactsRaritys = {
  'Regular': 0,
  'Uncommon': 1,
  'Rare': 2,
  'Epic': 3,
  'legengary': 4
}
# ох да, словари поди не в тему. Если 1 сласс Artifact, от класса artifactsTypes: WEAPON = 1 я не знаю что делать с ним тогда
# не понял)))
# 
class RARITIES(enum.IntEnum): # перечисление будет цифровое, вот я не знал как рандомный атрибут тянуть
  REGULAR = 0
  UNCOMMON = 1
  RARE = 2
  EPIC = 3
  LEGENDARY = 4
# лучше так, а не словари
  
  
class Artifact:
  def __init__(self, type=None, set=None, rarity=None, rank=None, primaryStat=None, substats=None):
    self._type = type
    self._set = set
    self._rarity = rarity
    self._rank = rank
    self._primaryStat = primaryStat
    self._substats = substats

  def _getType(self):
   assert False
    
  @property 
  def artifactType(self):
    return self._type

  @property
  def artifactSet(self):
    return self._set

  @property
  def artifactRarity(self):
    return self._rarity

  @property
  def artifactRank(self):
    return self._rank

  @property
  def artifactPrimaryStat(self):
    return self._primaryStat

  @property
  def artifactSubstats(self):
    return self._substats


