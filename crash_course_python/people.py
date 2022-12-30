subzero = {
    'name': 'Sub-Zero',
    'realm': 'Earthrealm',
    'alignment': 'Good',
    'faction': 'Lin Kuei',
    }

liukang = {
    'name': 'Liu Kang',
    'realm': 'Earthrealm',
    'alignment': 'Good',
    'faction': 'White Lotus Society'
    }

quanchi = {
    'name': 'Quan Chi',
    'realm': 'Netherealm',
    'alignment': 'Evil',
    'faction': 'Brotherhood of Shadow'
    }

people = [subzero, liukang, quanchi]

for person in people:
    print(f"{person['name']} is from {person['realm']} and fights for the\n"
          f"\t{person['alignment']} {person['faction']}.\n")


