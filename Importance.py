# These values are given in the task, and are used to make decisions.
import random
from math import log2

YES = 2
NO = 1


class TreeNode(object):
    """
    This is a node in the tree, to be used to handle logic when building the tree.
    Each node knows only which nodes are in its own subtree.
    """

    # initiates with a dictionary to contain subtrees
    def __init__(self, attribute):
        self.subtree = {}
        self.attribute = attribute

    # TODO
    def __repr__(self):
        pass

    def add_subtree(self, subtree, value):
        self.subtree[value] = subtree

class Example(object):
    """
    This is an example, attributes is a list of all attributes.
    """

    def __init__(self, attributes, class_):
        self.class_ = class_
        self.attributes = attributes


def random_importance():
    """
    Returns a number, where the largest is chosen
    :return: A number, where the largest is chosen.
    """
    ## Shell Function

    return random.randint(0, 10)


def eval_classification(examples):
    classification = examples[0].class_
    for i in examples:
        if i.class_!= classification:
            return False
    return True

def max_expected_value_importance():
    ## shell function

    return 0


def plurality_value(examples):
    """
    Takes in a list of Example objects and determines which is the most common value.
    :param examples: List of Example objects
    :return: The most common value.
    """
    iterable_value_list = [example.class_ for example in examples]
    return max(set(iterable_value_list), key=iterable_value_list.count)


def decision_tree_learning(examples, attributes, parent_examples, importance_method):
    """
    Performs DTL on a given training set and node evaluation function

    """

    tree = 0
    if len(examples) == 0:
        return plurality_value(parent_examples)

    elif examples.eval_classification() == 0:  # missing implementation
        return  # what is a classification? This is all based on pseudocode which is not well written

    elif attributes is None:
        return plurality_value(examples)
    else:
        # a = TreeNode(max())
        pass


def entropy(q):
    """
    Returns the impurity of the boolean variable q
    :param q:
    :return:
    """
    if q == 1 or q == 0:
        return 0
    return -q * log2(q) + (1 - q) * log2(1 - q)


def parse_training_data(file_name):
    """
    Method reads training data to be used and places it into a list containing string
    :param file_name: name of training data file to be read.
    :return:
    """
    with open(file_name, "r") as f:
        return_list = []
        data = f.readlines()
        # this is now a list containing strings on the following format:
        # "a, b, c, d, e, f, g, h" where all variables are integers.
        for string in data:
            temp_list = list(map(int, string.split("	")))
            return_list.append(temp_list)
    f.close()
    return return_list


def test_parse_training_data():
    """
    Validation method to check if parse_training_data works as expected.
    :param:
    :return:
    """
    print(parse_training_data("training.txt")[0:3])


test_parse_training_data()
