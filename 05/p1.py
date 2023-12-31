class DataMap:
    def __init__(self, map_input):
        self.rules = []
        for line in map_input.splitlines()[1:]:
            destination, source, range_length = map(int, line.split())
            self.rules.append((destination, source, range_length))

    def convertSeeds(self, seed_input):
        for destination, source, range_length in self.rules:
            if source <= seed_input < source + range_length:
                return destination + (seed_input - source)
        return seed_input
            #print(f" dest: {destination}, source: {source}, range: {range_length}")
            #print(self.rules)

    def evaluateMaps(seed, maps) -> (int, list):
        for datamap in maps:
            seed = datamap.convertSeeds(seed)
        return seed

def main(input):
    seeds, *map_inputs = input.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))
    #print(seeds, map_inputs)
    #print(DataMap(map_inputs))
    #print(DataMap(map_inputs[0]).rules)
    datamaps = []
    locations = []
    for map_input in map_inputs:
        datamap = DataMap(map_input)
        datamaps.append(datamap)
    for seed in seeds:
        locations.append(DataMap.evaluateMaps(seed, datamaps))
        #print(list(map(datamap.convertSeeds, seeds)))
        #locations = list(map(datamap.convertSeeds, seeds))

    return min(locations)

if __name__ == "__main__":
    main(input)
