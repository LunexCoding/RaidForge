import yaml
import random


class StatsConfig:
  def __init__(self, filename=None):
    self._filename = filename
    self._data = None
    
    self._mainStatsConstants = {}
    self._subStatsConstants = {}

    self._load()
    self._parseConfig()

  def _load(self):
    with open(self._filename, 'r') as config:
        self._data = yaml.full_load(config)
        
  def _parseMainConfig(self):
    for header in self._data.items():
          self._mainStatsConstants[header[0]] = []
          for key, value in header[1].items():
              self._statsConstants[header[0]].append({key: value})

  def _parseSubConfig(self):
    for header in self._data.items():
          self._subStatsConstants[header[0]] = []
          for key, value in header[1].items():
              self._subStatsConstants[header[0]].append({key: value})

  def viewStats(self):
    for key, value in self._mainStatsConstants.items():
        print(f'{key}:')
        for allParams in value:
            for param, typesParam in allParams.items():
                print(f'    {param}:')
                for type, stats in typesParam.items():
                    print(f'        {type}: {stats}')
        print()  

  @property
  def statsConstants(self):
    return self._mainStatsConstants

  def _getStatRequestedType(self, artifactType, statType, rank):
    key, value = random.choice(list(self._mainStatsConstants[artifactType][0][statType].items()))
    value = value[rank]
    return key, value


g_statsConfig = StatsConfig('config.yaml')
g_statsConfig.viewStats()
artifactTypeStats = g_statsConfig._getStatRequestedType('Gloves', 'Health', 3)
print(artifactTypeStats)
