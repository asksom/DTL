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
    """
    Evaluation function which determines if
    there is a point in splitting.
    Splitting is redundant if all are YES or all NO
    :param examples:
    :return: Boolean value, True if all values in example are the same
    """
    classification = examples[0].class_
    for i in examples:
        if i.class_ != classification: return False
    return True


def count_yes_and_no(examples):
    """
    Determines how many yeses and nos there are
    To be used to determine information gain in
    the actual non-random importance-implementation
    :param examples: examples
    :return: number of yes, number of no
    """
    yes = 0
    no = 0
    list_count = [x.class_ for x in examples]
    for x in list_count:
        if YES == x:
            yes += 1
        else:
            no += 1
    return yes, no


# attribute is an index
def remainder(attribute, examples):
    """
    calculates the remainder function value for the
    given attribute and its corresponding examples
    :param attribute: Index, to be accessed from the example class
    :param examples: examples to be evaluated.
    :return:
    """
    distinct_values = set()
    result = 0
    for ex in examples: distinct_values.add(ex.attributes[attribute])

    for val in distinct_values:
        pk = 0
        nk = 0
        for e in examples:
            if e.attribute[attribute] == val and e.class_ == YES:
                pk += 1
            elif e.attribute[attribute] == val and e.class_ == NO:
                nk += 1
        result += (pk + nk) / len(examples) * entropy(pk / (pk + nk))
    return result


# this needs to determine the expected information gain from each attribute
# maybe done on index? Idk. IMPORTANT: Page 704 in the book
def max_expected_value_importance(examples, attributes):
    """
    This method determines which attribute given the
    current examples is to be split on. It does this by
    taking the entropy of the example-set minus the remainder
    for each attribute, then evaluates which is the greater value.
    :param examples:
    :param attributes:
    :return:
    """

    # this needs not be too small, all actual values are at least 0
    max_gain = -1
    return_attribute = 0
    yes, no = count_yes_and_no(examples)
    for attribute in attributes:
        gain = entropy(yes / (yes + no)) - remainder(attribute, examples)
        if gain > max_gain:
            return_attribute = attribute
            max_gain = gain

    return return_attribute


def plurality_value(examples):
    """
    Takes in a list of Example objects and determines which is the most common value.
    :param examples: List of Example objects
    :return: The most common value. In this case that is either 1 or 2.
    """
    iterable_value_list = [example.class_ for example in examples]
    return max(set(iterable_value_list), key=iterable_value_list.count)


def decision_tree_learning(examples, attributes, parent_examples, importance_method):
    """
    Performs DTL on a given training set and node evaluation function

WIP

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


def test_plurality_value():
    test_list = parse_training_data("training.txt")
    obj_list = [Example(x[0:-1], x[-1]) for x in test_list]
    print(plurality_value(obj_list), " should be 1")
