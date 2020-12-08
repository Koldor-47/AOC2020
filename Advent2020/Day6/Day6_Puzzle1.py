"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration
forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions
for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For
each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the
same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the
plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's
answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

"""


def get_data(dataFile):
    with open(dataFile, 'r') as F:
        question_data = F.read().split("\n\n")
    return question_data


def Answered_questions(input_data):
    total_answers = 0
    new_data = []
    for q, x in enumerate(input_data):
        new_data.append(x.replace("\n", ""))
    for v in new_data:
        letter_dict = {}
        for a in v:
            if a not in letter_dict:
                letter_dict[a] = 0
            else:
                letter_dict[a] += 1

        total_answers += len(letter_dict)
    return total_answers





def test_answer(input_data):
    answers = input_data.split("\n")
    letter_count = {}
    letter_equal_count = 0
    length_of_list = len(answers)

    for answer in answers:
        for letter in list(answer):
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    for count in letter_count.values():
        if count == length_of_list:
            letter_equal_count += 1

    return letter_equal_count


def total_letter_counter(input_data):
    total_letter_count = 0
    for letter in input_data:
        total_letter_count += test_answer(letter)
    return total_letter_count

test_question_sheet2 = "a\na\na\na"
test_question_sheet = 'lznroxbqymvfijpwkec\ngljkpwyvsbmroziefnqxc\nbmkiewyxjfzqrocnlpv\nibewnmlkzfcrjyvxopq' \
                      '\nfkmxpbvjiwlrzocqyne '


data = get_data("Day5Data.txt")


print(f"Q1: {Answered_questions(data)} Q2: {total_letter_counter(data)}")