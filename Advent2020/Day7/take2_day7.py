import re


class coloured_bag:
    def __init__(self, holding_bag, contained_bags):
        self.bag = holding_bag
        self.Contained_bags = contained_bags


def read_data(inputFile):
    with open(inputFile, 'r') as F:
        list_data = F.read().split("\n")
    return list_data


test_data = read_data("day7Data.txt")

def organise_bags(bag_list):
    re_txt = r'\w+ \w+ bag'
    list_of_bags = []
    for bag in bag_list:
        temp_bag = re.findall(re_txt, bag)
        the_Bag = temp_bag[0].strip(" bag")
        contains_bag_list = []

        for C_bag in temp_bag[1:]:
            if "no other bag" in temp_bag[1:]:
                continue
            else:
                contains_bag_list.append(C_bag.strip(" bag"))

        colouredBag = coloured_bag(the_Bag, contains_bag_list)
        list_of_bags.append(colouredBag)
    return list_of_bags



bag_list2 = organise_bags(test_data)

for bag in bag_list2:
    print(f"{bag.bag} contains {bag.Contained_bags}")