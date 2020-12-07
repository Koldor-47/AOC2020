"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While
these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually
valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the
same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required
fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of
key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid -
it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not,
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file,
how many passports are valid?

"""
import re


def Get_passport_data(Data_file):
    with open(Data_file, "r") as DFile:
        data = DFile.read()
        data = data.split("\n\n")
        return data


def make_dict(string_Data):
    passport_data_list = []
    for passport in string_Data:
        passport = repr(passport.replace("\n", ' '))
        passport = passport.replace("'", "")
        passport = passport.split()
        d = dict(v.split(":") for v in passport)
        if len(d) == 8:
            passport_data_list.append(d)
        elif len(d) == 7 and 'cid' not in d:
            passport_data_list.append(d)

    return passport_data_list


def simpleVaild(Dict_data):
    valid_passports = 0
    invalid_passports = 0
    valid_passports_list = []
    for person in Dict_data:
        if len(person) == 8:
            valid_passports_list.append(person)
            valid_passports += 1
        elif len(person) == 7 and "cid" not in person:
            valid_passports_list.append(person)
            valid_passports += 1
        else:
            # print("not Valid")
            invalid_passports += 1

    print(f"The amount valid passports is: {valid_passports} ")
    return valid_passports_list


def complexValid(valid_Dict_data):
    valid_passports = []
    passport_hair_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for passenger in valid_Dict_data:
        valid_passport = 0
        # Checking for correct BirthDate
        if 1920 <= int(passenger["byr"]) <= 2002:
            valid_passport += 1
        else:
            continue
        # Checking the correct Issue Date
        if 2010 <= int(passenger["iyr"]) <= 2020:
            valid_passport += 1
        else:
            continue
        # Checking the Correct Expiration Date
        if 2020 <= int(passenger["eyr"]) <= 2030:
            valid_passport += 1
        else:
            continue
        # Looking For the right height

        if passenger["hgt"][-2:] == "cm":
            if 150 <= int(passenger["hgt"][:-2]) <= 193:
                valid_passport += 1
            else:
                continue
        elif passenger["hgt"][-2:] == "in":
            if 59 <= int(passenger["hgt"][:-2]) <= 76:
                valid_passport += 1
            else:
                continue
        else:
            continue
        # Checking For correct eye Colour
        if passenger["ecl"] in passport_hair_colour:
            valid_passport += 1
        else:
            continue
        # Checking For Correct hair Colour
        if re.fullmatch(r'#[0-9a-f]{6}', passenger["hcl"]):
            valid_passport += 1
        else:
            continue
        # checking for correct Pass ID
        if re.fullmatch(r'[0-9]{9}', passenger["pid"]):
            valid_passport += 1
        else:
            continue
        if valid_passport >= 7:
            valid_passports.append(passenger)

    return valid_passports


Answer1 = simpleVaild(make_dict(Get_passport_data("Day4Data.txt")))
test = simpleVaild(make_dict(Get_passport_data("test_data2.txt")))
second = complexValid(make_dict(Get_passport_data("Day4Data.txt")))

print(len(second))
