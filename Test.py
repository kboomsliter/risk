import risk
import data

players = {'Izzy': risk.Player('Izzy'), 
        'Chris': risk.Player('Chris'), 
        'Kerry': risk.Player('Kerry')}
troopColors = risk.PlayerColors()

print("Players: " + str(list(players.keys())))

# players first die roll would determine order
# order would allow players to pick colors

troopColors.assign('blue', players['Chris'])
troopColors.assign('red', players['Kerry'])
troopColors.assign('yellow', players['Izzy'])

for k, v in players.items():
    print("Player " + k + " is assigned troop color " + v.color)

for contName, contMap in data.landmap.items():
    print "Continent: " + contName
    for terrName, terrMap in contMap.items():
        print "   Territory: " + terrName
        for adjacency in terrMap:
            print "       Adjacent to: " + adjacency

for contName, contProp in data.continentProperties.items():
    print "Continent: " + contName
    for name, value in contProp.items():
        print "    " + name + ": " + str(value)
