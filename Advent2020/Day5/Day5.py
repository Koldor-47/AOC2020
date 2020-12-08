

def get_input_data(input_data):
    with open(input_data, 'r') as F:
        thedata = F.read().split("\n")
    return thedata

def data_to_number(row_data, letters):
    # letters needs to a list ie ["F", "B"]
    answer = "0b"
    for pos in row_data:
        if pos.upper() == letters[1]:
            answer += "1"
        elif pos.upper() == letters[0]:
            answer += "0"
        else:
            print("invalid")

    return int(answer, 2)


def get_seat_id(bin_data, codes):
    # Codes are all 4 toe of letters in 1 list ["F","B","L","R"]
    rows = codes[:2]
    cols = codes[2:]
    seat_id_list = []
    for ticket in bin_data:
        part2 = data_to_number(ticket[:-3], rows)
        part1 = data_to_number(ticket[-3:], cols)
        seat_id = (part2 * 8) + part1
        seat_id_list.append(seat_id)

    return seat_id_list

def find_my_seat(seat_ids):
    set_seat_id = set(seat_ids)
    full_range = set(range(min(seat_ids), max(seat_ids)))

    return full_range.difference(set_seat_id)

# Single Test
Seat_number = "BBFFBBFRLL"
answer = data_to_number(Seat_number[:-3], ["F", "B"])
print(answer)

#Answer Part 1
puzzle1 = get_seat_id(get_input_data("Day5Data.txt"), ["F","B","L","R"])

# Day 5 Answers
print(max(puzzle1))
print(find_my_seat(puzzle1))