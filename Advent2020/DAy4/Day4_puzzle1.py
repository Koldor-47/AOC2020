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


passport_data = Get_passport_data("Day4Data.txt")

find_keypars = r'\w+\:[A-Za-z0-9#]+'




def make_dict(string_data):
    new_data = []
    for passport in string_data:
        password_dict = {}
        keyPairs = re.findall(find_keypars, passport)
        for item in keyPairs:
            password_dict[item.split(":")[0]] = item.split(":")[1]
        if len(password_dict) > 6:
            new_data.append(password_dict)
    return new_data


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
            #print("not Valid")
            invalid_passports += 1

    print(f"The amount valid passports is: {valid_passports} ")
    return valid_passports_list

def complexValid(valid_Dict_data):
    valid_passports = 0
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passenger in valid_Dict_data:
        print(f" Passenger birth {passenger['byr']} and passport Date {passenger['iyr']}")
        valid_passport = False
        if int(passenger["byr"]) >= 1920 and int(passenger["byr"]) <= 2002:
            valid_passport = True
            print("hi")
        else:
            valid_passport = False
            continue

        if int(passenger["iyr"]) >= 2010 and int(passenger["byr"]) <= 2020:
            valid_passport = True
        else:
            valid_passport = False
            continue

        if int(passenger["eyr"]) >= 2020 and int(passenger["eyr"]) <= 2030:
            valid_passport = True
        else:
            valid_passport = False
            continue


        if valid_passport:
            valid_passports += 1

    return valid_passports



Answer1 = simpleVaild(make_dict(Get_passport_data("Day4Data.txt")))
testAnser = simpleVaild(make_dict(Get_passport_data("test_data.txt")))
test = simpleVaild(make_dict(Get_passport_data("Day4Data.txt")))


print(complexValid(testAnser))