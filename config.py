import yaml
import random


class BaseConfig:
    def __init__(self, filename=None):
        self._configType = None
        self._filename = filename
        self._data = None

        self._load()

    def _load(self):
        with open(self._filename, 'r') as config:
            self._data = yaml.full_load(config)

    def _parseData(self):
        pass

    def __enter__(self):
        return self.data, self.type  # без надобности self, нет в планах обращаться к context

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._data = None
        return True

    @property
    def data(self):
        return self._data

    @property
    def type(self):
        return self._configType


class MainStatsConfig(BaseConfig):
    def __init__(self, filename=None):
        super().__init__(filename)
        self._configType = 'primary'


class SubStatsConfig(BaseConfig):
    def __init__(self, filename=None):
        super().__init__(filename)
        self._configType = 'sub'


class ParserConfigData:
    def __init__(self):
        self._data = {
            'primary': None,
            'sub': None
        }

    def definingConfig(self, dataConfig):
        data, type = dataConfig
        assert type in self._data, 'Unknown config type'
        self._data[type] = data

    def requestToGetArtifactParameters(self, request):
        return self._parseRequestToGetArtifactParameters(request)

    def _parseRequestToGetArtifactParameters(self, request=None):
        '''
        Request pattern:

            Primary:
            {
                'artifactType': ... ,
                'stat': ... ,
                'data': {
                    'rank': ... ,
                    ...
                }
            }

            Subs:
            {
            'artifactType': ... ,
            'stat': ... ,
            'data': {
                'rank': ... ,
                'rarity': ... ,
                ...
                'primaryStat': {
                    'statType': ... ,
                    'statSubType': ...
                }
            }
        }
        '''

        stat = request.get('stat')
        data = request.get('data')

        assert stat == 'primary' or stat == 'sub', 'Unknown stat type'

        artifactType = request.get('artifactType')
        rank = data.get('rank')
        countSubStats = data.get('rarity')

        if stat == 'primary':
            return self._getPrimaryStat(artifactType, rank)

        elif stat == 'sub':

            primaryStatData = data['primaryStat']

            return self._getSubStat(countSubStats, primaryStatData, rank)

    def _getPrimaryStat(self, arfifactType, rank):
        primaryStatType = random.choice(list(self._data['primary'][arfifactType].keys()))
        primaryStatSubType = random.choice(list(self._data['primary'][arfifactType][primaryStatType].keys()))

        return (primaryStatType, primaryStatSubType, self._data['primary'][arfifactType][primaryStatType][primaryStatSubType][rank])

    def _getSubStat(self, countSubStats, primaryStatData, rank):

        subStatType = random.choice(list(self._data['sub'].keys()))
        subStatSubType = random.choice(list(self._data['sub'][subStatType].keys()))

        if [subStatType, subStatSubType] == [primaryStatData['statType'], primaryStatData['statSubType']]:
            print(f"{subStatType}, {subStatSubType} and {primaryStatData['statType']}, {primaryStatData['statSubType']}")
            print("Repeat")
            return self._getSubStat(countSubStats, primaryStatData, rank)

        return [(subStatType, subStatSubType), (primaryStatData['statType'], primaryStatData['statSubType'])]


parserConfigs = ParserConfigData()

with (
    MainStatsConfig('config.yaml') as mainConfig,
    SubStatsConfig('subconfig.yaml') as subConfig
):

    parserConfigs.definingConfig(mainConfig)
    parserConfigs.definingConfig(subConfig)

request = {
            'artifactType': 'Gloves',
            'stat': 'sub',
            'data': {
                'rank': 4,
                'rarity': 3,
                'primaryStat': {
                    'statType': 'Attack',
                    'statSubType': 'Flat'
                }
            }
        }

print(parserConfigs.requestToGetArtifactParameters(request))


# Кусок старого кода, должен переместиться в новый класс
def viewStats(self):
    for artifactType, allMainStatsByArtifactType in self._mainStatsConstants.items():
        print(f'{artifactType}:')

        for fullDataByMainStatType in allMainStatsByArtifactType:
            for mainStatType, fullDataByMainStatSubType in fullDataByMainStatType.items():
                print(f'    {mainStatType}:')
                for mainStatSubType, dataMainStatSubTypeByRank in fullDataByMainStatSubType.items():
                    print(f'        {mainStatSubType}: {dataMainStatSubTypeByRank}')
        print()

