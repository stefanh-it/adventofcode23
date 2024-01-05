def raceBoats(time, target_dist):
    travel_distance = 0
    valid_game = 0
    time = int(time)
    for speed in range(time):
        speed += 1
        travel_distance = (time-speed) * speed
        # print(f"Speed: {speed}", f"Time: {time}", f"Distance: {travel_distance}")
        if travel_distance > int(target_dist):
            valid_game += 1
        # print(f"Valid Games: {valid_game}")
    return valid_game


def main(input):
    input = input.splitlines()
    time = ''.join(input[0].split()[1:])
    target_dist = ''.join(input[1].split()[1:])
    solution = raceBoats(time, target_dist)
    return solution, None


if __name__ == '__main__':
    main(input)
