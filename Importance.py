# These values are given in the task, and are used to make decisions.
POSITIVE = 2
NEGATIVE = 1


class TreeNode(object):
    """
    This is a node in the tree, to be used to handle logic when building the tree.
    """
    #initiates with a dictionary to contain subtrees
    def __init__(self, attribute):
        self.subtree = {}
        self.attribute = attribute

    # TODO
    def __repr__(self):
        pass

    def add_subtree(self, subtree, value):
        self.subtree[value] = subtree


def random_importance():
    ## Shell Function

    return 0


def max_expected_value_importance():
    ## shell function

    return 0


def decision_tree_learning(training_set, target, attribute):
    """
    Performs DTL on a given training set and node evaluation function
    :param training_set:
    :param target:
    :param attribute:
    :return: Decision tree
    """

    tree = 0
    return tree


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
        # "a, b, c, d, e, f, g" where all variables are integers.
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
