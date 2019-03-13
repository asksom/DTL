import random
from math import log2

# These values are given in the task, and are used to make decisions.
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

    def __repr__(self):
        return self.class_,self.attributes


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
            if e.attributes[attribute] == val and e.class_ == YES:
                pk += 1
            elif e.attributes[attribute] == val and e.class_ == NO:
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


def decision_tree_learning(examples, attributes, parent_examples, importance_method=max_expected_value_importance):
    """
    Performs DTL on a given training set and node evaluation function
    :param examples: examples, a list of Example objects
    :param attributes: attributes, a list of length 0-6, which values of the same magnitude.
    :param parent_examples: The examples the previous iteration used.
    :param importance_method:
    :return:
    """
    if len(examples) == 0:
        return TreeNode(plurality_value(parent_examples))
    elif eval_classification(examples):
        return TreeNode(examples[0].class_)
    elif len(attributes) == 0:
        return TreeNode(plurality_value(examples))
    else:
        A = importance_method(examples, attributes)
        tree = TreeNode(A)
        new_attribute_list = list(filter(lambda a: a != A, attributes))
        # this is the new list of attributes to be carried over to the next iteration.
        # Hard code: values are only 1 or 2; ideally this would be done differently
        for vk in range(1, 3):
            exs = list(filter(lambda e: e.attributes[A] == vk, examples))
            subtree = decision_tree_learning(exs, new_attribute_list, examples)
            tree.add_subtree(subtree, vk)
        return tree


# This function is based completely on the pseudocode provided on page 703 of the course book.

def entropy(q):
    """
    Returns the impurity of the boolean variable q
    :param q:
    :return: Numeric value of entropy/impurity
    """
    if q == 1 or q == 0:
        return 0
    return -q * log2(q) + (1 - q) * log2(1 - q)


def parse_training_data(file_name="training.txt"):
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


def create_examples_from_data(list_of_examples):
    return [Example(x[:-1], x[-1]) for x in list_of_examples]


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


def main():
    examples = create_examples_from_data(parse_training_data())
    tree = decision_tree_learning(examples, [0, 1, 2, 3, 4, 5, 6], examples)
    #print(tree.subtree)


if __name__ == "__main__":
    main()
main()
