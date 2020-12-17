"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab
some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible
for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every
vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would
be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny
    gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny
    gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure
you get all of it.)

"""

import re
import os

print(os.getcwd())


def get_luggage_data(luggage_data):
    with open(luggage_data, "r") as F:
        luggage_list = F.read().split("\n")
    return luggage_list


def gold_bag_holder(luggage_data):
    gold_bag_count = 0
    gold_bag_name = "shiny gold bag"
    gold_bag_holder_bag = []
    for rule in luggage_data:
        raw_bag_list = re.findall(r"\w+ \w+ bag", rule)
        secondary_bags = raw_bag_list[1:]
        for secondary_bag in secondary_bags:
            if secondary_bag == gold_bag_name:
                gold_bag_holder_bag.append(raw_bag_list[0])
    return gold_bag_holder_bag


def test1(gold_carrying_bags, luggage_data):
    bag_list = []
    for bag in luggage_data:
        raw_bag_list = re.findall(r"\w+ \w+ bag", bag)
        for G_bag in gold_carrying_bags:
            if G_bag in raw_bag_list[1:]:
                bag_list.append(raw_bag_list[:1])
                break
    return bag_list


from_luggage_machine = get_luggage_data("day7Data.txt")

gold_carrying_bags = gold_bag_holder(from_luggage_machine)
bag_list_temp = test1(gold_carrying_bags, from_luggage_machine)

bag_list = [item for b_list in bag_list_temp for item in b_list]

print(test1(bag_list, from_luggage_machine))


print(len(test1(gold_carrying_bags, from_luggage_machine)) + len(gold_carrying_bags))
test_string = "light red bags contain 1 bright white bag, 2 muted yellow bags."

# I think im meant ot becount the amount of different bag that carry gold bags ...... 27 isn't the right asnwer