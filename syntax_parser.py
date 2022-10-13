import json
import numpy as np
from collections import defaultdict


class RuleWriter(object):
    """
    This class is for writing rules in a format 
    the judging software can read
    Usage might look like this:

    rule_writer = RuleWriter()
    for lhs, rhs, prob in out_rules:
        rule_writer.add_rule(lhs, rhs, prob)
    rule_writer.write_rules()

    """
    def __init__(self):
        self.rules = []

    def add_rule(self, lhs, rhs, prob):
        """Add a rule to the list of rules
        Does some checking to make sure you are using the correct format.

        Args:
            lhs (str): The left hand side of the rule as a string
            rhs (Iterable(str)): The right hand side of the rule. 
                Accepts an iterable (such as a list or tuple) of strings.
            prob (float): The conditional probability of the rule.
        """
        assert isinstance(lhs, str)
        assert isinstance(rhs, list) or isinstance(rhs, tuple)
        assert not isinstance(rhs, str)
        nrhs = []
        for cl in rhs:
            assert isinstance(cl, str)
            nrhs.append(cl)
        assert isinstance(prob, float)

        self.rules.append((lhs, nrhs, prob))

        
    def write_rules(self, filename="q1.json"):
        """Write the rules to an output file.

        Args:
            filename (str, optional): Where to output the rules. Defaults to "q1.json".
        """
        json.dump(self.rules, open(filename, "w"))


# load the parsed sentences
psents = json.load(open("parsed_sents_list.json", "r"))
# psents = [['A', ['B', ['C', 'blue']], ['B', 'cat']]] # test case

# print a few parsed sentences
# NOTE: you can remove this if you like
# for sent in psents[:10]:
#     print(sent)

#
# final = []
# def flatten(lst,count):
#     count=count+1
#     for t in range(len(lst)-1):
#         a = []
#         a.append(lst[0])
#         if count<=3:
#             if len(lst[t + 1]) > 1:
#                 final.extend(flatten(lst[t + 1],count))
#                 if len(lst[t + 1][0]) == 1:
#                     a.append(lst[t + 1][0])
#             if len(lst[t + 1]) == 1:
#                 a.append(lst[t + 1])
#         else:
#             a.append(lst[t + 1])
#
#
#         final.append(a)
#     return final
#
# count=0
# print(flatten(psents[0],count))
final=[]
ffinal = []

def faltte(lst):

    for i in range(len(lst) - 1):
        if isinstance(lst[i + 1],list):
            ffinal.append([lst[0], lst[i + 1][0]])
            faltte(lst[i + 1])
        else:
            ffinal.append([lst[0], lst[i + 1]])
    return ffinal

def calp(final):
    have=[]
    for i in final:
        if i not in have:
            count = 0
            p = 1
            for j in final:
                if i[0] == j[0] and i[1] == j[1]:
                    count = count + 1
                elif i[0] == j[0]:
                    p = p + 1
            a = []
            for t in range(count):
                a.append(i[1])

            if i not in have:
                have.append(i)
                rule_writer.add_rule(i[0], a, 1 / p)

rule_writer=RuleWriter()
count=0
for i in psents:
    calp(faltte(i))
    count=count+1
rule_writer.write_rules()

















# TODO: estimate the conditional probabilities of the rules in the grammar

# TODO: write the rules to the correct output file using the write_rules method

