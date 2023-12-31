"""Part Two."""
## https://www.youtube.com/watch?v=b8ka6eZ4Vbk&t=1044 ## Source + Tutorial

class SeedRange:
    """Represents a range of seeds."""

    def __init__(self, starting, ending):
        self.starting = starting
        self.ending = ending

    def __repr__(self):
        return f"({self.starting}, {self.ending})"

    def intersection(self, other):
        """Return the intersection of two seed ranges."""
        temp_range = SeedRange(max(self.starting, other.starting), min(self.ending, other.ending))
        return temp_range if temp_range.starting < temp_range.ending else None

    def subtractRanges(self, other):
        intersection = self.intersection(other)
        if intersection == None: 
            return [SeedRange(self.starting, self.ending)]
        elif (intersection.starting, intersection.ending) == (self.starting, self.ending):
            return []
        elif intersection.starting == self.starting
            return [SeedRange(intersection.ending, self.ending)]
        elif intersection.ending == self.ending
            return [SeedRange(self.starting, intersection.starting)]
        else:
            return [SeedRange(self.starting, intersection.starting), SeedRange(intersection.ending, self.ending)]

    def add(self, offset)
        return SeedRange(self.starting + offset, self.ending + offset)

class DataMap:
    """Represents a data map."""

    def __init__(self, map_input):
        self.rules = []
        self.seed_ranges = []
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

    # def getSeedRange(seed_ranges):
    #     seed_start = []
    #     seed_end = []
    #     for i, seed in enumerate(seed_ranges):
    #         if i % 2 == 0:
    #             seed_start.append(seed)
    #         if i % 2 != 0:
    #             seed_end.append(seed_start[-1] + int(seed))
    #     zipped_seed_ranges = zip(seed_start, seed_end)
    #     seed_ranges_list = []
    #     for sr in zipped_seed_ranges:
    #         # print(sr)
    #         ranges = range(sr[0], sr[1], 1)
    #         seed_ranges_list += list(map(int, ranges))
    #     return seed_ranges_list

def main(input):
    seeds, *map_inputs = input.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))
    # seed_start = []
    # seed_end = []
    # seed_ranges = ()
    # for i, seed in enumerate(seeds):
    #     if i % 2 == 0:
    #         seed_start.append(seed)
    #     if i % 2 != 0:
    #         seed_end.append(seed_start[-1] + int(seed)-1)
    # seed_ranges = list(zip(seed_start, seed_end))
    # print(seed_ranges)
    #print(seeds, map_inputs)
    #print(DataMap(map_inputs))
    #print(DataMap(map_inputs[0]).rules)
    datamaps = []
    locations = []
    for map_input in map_inputs:
        datamap = DataMap(map_input)
        datamaps.append(datamap)
    # seed_ranges = DataMap.getSeedRange(seeds)
    # print(seed_ranges)
    for seed in seeds:
        locations.append(DataMap.evaluateMaps(seed, datamaps))
        #print(list(map(datamap.convertSeeds, seeds)))
        #locations = list(map(datamap.convertSeeds, seeds))
    
    #locations = [1, 2]
    return min(locations)

if __name__ == "__main__":
    main(input)
