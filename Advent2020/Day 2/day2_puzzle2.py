"""
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan
Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at
the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""

testList = ["1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc",
            "3-4 d: dddv"]

def GetData(DataFile):
    with open(DataFile, 'r') as TheFile:
        data_from_file = TheFile.read()
        data_from_file = data_from_file.split("\n")
        return data_from_file

def checkPassword(Passwords):
    valid_password_count = 0
    for Password in Passwords:
        amount_of_letters = Password.split(":")[0]
        TheWord = Password.split(":")[1].lstrip()
        theLetter = amount_of_letters[-1]
        letterAmount = amount_of_letters[:-2].split("-")
        firstPos = TheWord[int(letterAmount[0])-1]
        secondPos = TheWord[int(letterAmount[1])-1]

        if (firstPos == theLetter and secondPos != theLetter) or (firstPos != theLetter and secondPos == theLetter):
            valid_password_count += 1
    print(valid_password_count)

checkPassword(GetData("Day2Data.txt"))