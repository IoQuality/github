def arithmetic_arranger(problems: list[str],
                        display_results: bool = False,
                        space_between_problems: int = 4,
                        minimal_distance: int = 2,
                        digit_limit: int = 4) -> str:
    """
    Formats a list of arithmetic problems vertically and returns the formatted string.

    :param problems: A list of strings representing arithmetic problems.
                     Each problem should contain two numbers and an operator separated by spaces.
                     The operator must be '+' or '-'.
    :param display_results: A boolean value indicating whether to display the results of the arithmetic problems.
                            Default is False.
    :param space_between_problems: An integer value representing the number of spaces between each problem.
                                    Default is 4.
    :param minimal_distance: An integer value representing the minimum distance between the operator and the longest
                             number length for each problem. Default is 2.
    :param digit_limit: An integer value representing the maximum number of digits allowed for each number in the
                        problems. Default is 4.

    :return: A string representing the formatted arithmetic problems.
            If an error occurs, an error message is returned instead.
    """

    if len(problems) < 1:
        return "Error: No problems to solve."

    if len(problems) > 5:
        return "Error: Too many problems."

    # splitting problems into three lists
    try:
        addends_1, operators, addends_2 = zip(*(problem.split() for problem in problems))
    except ValueError:
        raise ValueError("The program accepts no more than two numbers and one operator sign per problem ")

    # checking operators
    supported_operations = ("-", "+")
    if any(operator not in supported_operations for operator in operators):
        return "Error: Operator must be '+' or '-'."

    # testing all addends' types
    try:
        addends_1 = list(map(int, addends_1))
        addends_2 = list(map(int, addends_2))
    except ValueError:
        return "Error: Numbers must only contain digits."

    # calculating results for the supported operations
    results = [addend_1 + addend_2 if operator == "+" else addend_1 - addend_2
               for addend_1, operator, addend_2 in zip(addends_1, operators, addends_2)]

    # finding maximum addend length for each problem, minimal_distance accounts for the operator symbol and a single
    # white space between the operator and the longest number length for each problem
    max_lengths = [len(str(max(addend_1, addend_2)))+minimal_distance for addend_1, addend_2 in zip(addends_1, addends_2)]
    if any(max_length > minimal_distance + digit_limit for max_length in max_lengths):
        return "Error: Numbers cannot be more than four digits."

    # padding addends_1
    new_addends_1 = [f"{addend_1:{max_length}d}" for addend_1, max_length in zip(addends_1, max_lengths)]
    # adding operator and padding to addends_2
    new_addends_2 = [f"{operator} {addend_2:{max_length - minimal_distance}d}"
                     for operator, addend_2, max_length in zip(operators, addends_2, max_lengths)]
    # padding results
    new_results = [f"{result:{max_length}d}" for result, max_length in zip(results, max_lengths)]

    # creating lines with fixed spacing between the problems
    space_between_problems = " " * space_between_problems
    line_1 = space_between_problems.join(f"{addend_1}" for addend_1 in new_addends_1)
    line_2 = space_between_problems.join(f"{addend_2}" for addend_2 in new_addends_2)
    line_3 = space_between_problems.join(f"{'-' * max_length}" for max_length in max_lengths)
    line_4 = space_between_problems.join(f"{result}" for result in new_results)

    # constructing the final string for the output
    final_line = [line_1, line_2, line_3]
    if display_results:
        final_line.append(line_4)
    return "\n".join(final_line)
