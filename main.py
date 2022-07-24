from arsenal import g_arsenal
from forge import g_forge
from config import g_parserConfigs, MainStatsConfig, SubStatsConfig


def main():
    set = 'Speed'

    g_forge.choiseSet(set)

    for i in range(10):
        art = g_forge.generateArtifact()
        g_arsenal.addInArsenal(art)

    g_arsenal.load()


if __name__ == '__main__':
    with (
        MainStatsConfig('configs/primary.yaml') as mainConfig,
        SubStatsConfig('configs/sub.yaml') as subConfig
    ):
        g_parserConfigs.definingConfig(mainConfig)
        g_parserConfigs.definingConfig(subConfig)

    main()
