import re
import collections


class coloured_bag:
    def __init__(self, holding_bag, contained_bags):
        self.bag = holding_bag
        self.Contained_bags = contained_bags


def read_data(inputFile):
    with open(inputFile, "r") as F:
        list_data = F.read().split("\n")
    return list_data


test_data = read_data("test_data.txt")


def organise_bags(bag_list):
    re_txt = r"\w+ \w+ bag"
    list_of_bags = []
    for bag in bag_list:
        temp_bag = re.findall(re_txt, bag)
        the_Bag = temp_bag[0].split()[:2]
        the_Bag = " ".join(the_Bag)
        contains_bag_list = []

        for C_bag in temp_bag[1:]:
            if "no other bag" in temp_bag[1:]:
                continue
            else:
                contains_bag_list.append(" ".join(C_bag.split()[:2]))

        colouredBag = coloured_bag(the_Bag, contains_bag_list)
        list_of_bags.append(colouredBag)
    return list_of_bags


def backwards_bags(bag_list):
    p_bag_regex = re.compile(r"^(\w+ \w+) bags contain (.+)$")
    c_bags_regex = re.compile(r"(\d+) (\w+ \w+)")
    backwards_bags = collections.defaultdict(list)
    for bag in bag_list:
        bag_line = p_bag_regex.match(bag)
        P_bag = bag_line[1]
        C_bag = bag_line[2]

        for n, child in c_bags_regex.findall(C_bag):
            print(f" n = {n}, can child = {child}")
            backwards_bags[child].append(P_bag)

    return backwards_bags


def get_bag_of_bags(bag_list, start_bag):
    b_lists = []
    for bag in bag_list:
        if start_bag in bag.Contained_bags:
            b_lists.append(bag.bag)

    print(b_lists)


bag_list2 = backwards_bags(test_data)

print(bag_list2)
