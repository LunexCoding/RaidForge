import yaml
import random


CONFIGTYPES = set(['primary', 'sub'])


class BaseConfig:
    def __init__(self, filename=None):
        self._configType = None
        self._filename = filename
        self._data = None

        self._load()

    def _load(self):
        with open(self._filename, 'r') as config:
            self._data = yaml.full_load(config)

    def __enter__(self):
        return self._data, self._configType  # без надобности self, нет в планах обращаться к context

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
        self._data = {config: (data := None) for config in CONFIGTYPES}

    def definingConfig(self, configData):
        data, type = configData
        assert type in CONFIGTYPES, 'Unknown config type'
        self._data[type] = data

    def requestToGetArtifactParameters(self, request):
        return self._parseRequestToGetArtifactParameters(request)

    def _parseRequestToGetArtifactParameters(self, request=None):
        stat = request['stat']
        data = request['data']

        artifactType = request['artifactType']
        rank = data['rank']

        if stat == 'primary':
            return self._getPrimaryStat(artifactType, rank)

        elif stat == 'sub':

            primaryStatData = data['primaryStat']
            countSubStats = data['rarity']

            return self._getSubStat(countSubStats, primaryStatData, rank)

    def _getPrimaryStat(self, arfifactType, rank):
        primaryStatType = random.choice(list(self._data['primary'][arfifactType].keys()))
        primaryStatSubType = random.choice(list(self._data['primary'][arfifactType][primaryStatType].keys()))
        value = self._data['primary'][arfifactType][primaryStatType][primaryStatSubType][rank]

        return dict(statType=primaryStatType, statSubType=primaryStatSubType, value=value)

    def _getSubStat(self, countStats, primaryStatData, rank):

        listSubStats = []

        dictonary = {
            'Health': set(list(self._data['sub']['Health'].keys())),
            'Attack': set(list(self._data['sub']['Attack'].keys())),
            'Defense': set(list(self._data['sub']['Defense'].keys())),
            'Accuracy': set(list(self._data['sub']['Accuracy'].keys())),
            'Resistance': set(list(self._data['sub']['Resistance'].keys())),
            'Crit Chance': set(list(self._data['sub']['Crit Chance'].keys())),
            'Crit damage': set(list(self._data['sub']['Crit damage'].keys())),
            'Speed': set(list(self._data['sub']['Speed'].keys()))
        }

        dictonary[primaryStatData['statType']].discard(primaryStatData['statSubType'])
        if not dictonary[primaryStatData['statType']]:
            del dictonary[primaryStatData['statType']]

        for stat in range(countStats):

            statType = random.choice(list(dictonary.keys()))
            statSubType = random.choice(list(dictonary[statType]))
            dictonary[statType].discard(statSubType)
            if not dictonary[statType]:
                del dictonary[statType]

            value = self._data['sub'][statType][statSubType][rank]

            listSubStats.append(dict(statType=statType, statSubType=statSubType, value=value))

        return listSubStats


g_parserConfigs = ParserConfigData()
