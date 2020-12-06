"""
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over
from a past vacation. They offer you a second one if you can find three numbers in your expense report
that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

def GetData(DataFile):
    with open(DataFile, 'r') as Input_txt:
        inputTXT = Input_txt.read()
        input_list = inputTXT.split("\n")
        input_int_list = []
        for num in range(len(input_list)):
            input_int_list.append(int(input_list[num]))

    return input_int_list

def Get_three_number(Data, total):
    value1 = None
    value2 = None
    Value3 = None

    for count, value in enumerate(Data):
        for second_count, second_value in enumerate(Data):
            if value + second_value < total:
                value1 = Data[count]
                value2 = Data[second_count]
                two_totals = value1 + value2
                if (total - two_totals) in Data:
                    return((total - two_totals) * value1 * value2)



print(Get_three_number(GetData("day1_input.txt"), 2020))