from forge import g_forge

g_forge.choiseSet(input('name set -> '))
artifact = g_forge.createArtifact()
print(artifact.artifactRarity)