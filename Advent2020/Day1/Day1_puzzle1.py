
test_input = [1721,
              979,
              366,
              299,
              675,
              1456]

def GetData(DataFile):
    with open(DataFile, 'r') as Input_txt:
        inputTXT = Input_txt.read()
        input_list = inputTXT.split("\n")
        input_int_list = []
        for num in range(len(input_list)):
            input_int_list.append(int(input_list[num]))

    return input_int_list

def Answer(expense_report, total_expense):
    for i in expense_report:
        num = 2020 - i
        if num in expense_report:
            return i * num
            break


print(Answer(GetData("day1_input.txt"), 2020))
