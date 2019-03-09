def random_importance():
    ## Shell Function

    return 0


def max_expected_value_importance():
    ## shell function

    return 0


def decision_tree_learning():
    return


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
            temp_list = string.split("	")
            for i in range(len(temp_list)):
                temp_list[i] = int(temp_list[i])
            return_list.append(temp_list)
    f.close()
    return return_list


def test_parse_training_data():
    """
    Validation method to check if parse_training_data works as expected.
    :param file_name:
    :return:
    """
    print(parse_training_data("training.txt")[0])


test_parse_training_data()
