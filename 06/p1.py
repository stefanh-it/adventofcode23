def raceBoats(times, target_dists):
    travel_distance = 0
    valid_games = 1
    for i, time in enumerate(times):
        valid_game = 0
        time = int(time)
        for speed in range(time):
            speed += 1
            travel_distance = (time-speed) * speed
            print(f"Speed: {speed}", f"Time: {time}", f"Distance: {travel_distance}")
            if travel_distance > int(target_dists[i]):
                valid_game += 1
            print(f"Valid Games: {valid_game}")
        valid_games *= valid_game
    return valid_games
    


def main(input):
    input = input.splitlines()
    times = input[0].split()[1:]
    target_dists = input[1].split()[1:]
    print(f"Times: {times}, Dists: {target_dists}")
    solution = raceBoats(times, target_dists)
    return solution, None

if __name__ == '__main__':
    main(input)
