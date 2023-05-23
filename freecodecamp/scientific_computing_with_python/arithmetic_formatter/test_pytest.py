from arithmetic_arranger import arithmetic_arranger


def test_valid_input():
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    expected_output = "   32      3801      45      123\n" \
                      "+ 698    -    2    + 43    +  49\n" \
                      "-----    ------    ----    -----"
    assert arithmetic_arranger(problems) == expected_output


def test_invalid_operator():
    # Test with invalid operator
    problems = ["32 x 698"]
    expected_output = "Error: Operator must be '+' or '-'."
    assert arithmetic_arranger(problems) == expected_output


def test_non_digit_input():
    # Test with non-digit input
    problems = ["32a + 698"]
    expected_output = "Error: Numbers must only contain digits."
    assert arithmetic_arranger(problems) == expected_output


def test_too_many_problems():
    # Test with too many problems
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 1", "2 + 2"]
    expected_output = "Error: Too many problems."
    assert arithmetic_arranger(problems) == expected_output


def test_number_longer_than_four_digits():
    # Test with numbers longer than four digits
    problems = ["12345 + 698"]
    expected_output = "Error: Numbers cannot be more than four digits."
    assert arithmetic_arranger(problems) == expected_output


def test_display_results():
    # Test with valid input and display_results=True
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    expected_output = "   32      3801      45      123\n" \
                      "+ 698    -    2    + 43    +  49\n" \
                      "-----    ------    ----    -----\n" \
                      "  730      3799      88      172"
    assert arithmetic_arranger(problems, display_results=True) == expected_output


def test_space_between_problems():
    # Test with valid input and space_between_problems=2
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    expected_output = "   32    3801    45    123\n" \
                      "+ 698  -    2  + 43  +  49\n" \
                      "-----  ------  ----  -----"
    assert arithmetic_arranger(problems, space_between_problems=2) == expected_output


def test_digit_limit():
    # Test with valid input and digit_limit=4
    problems = ["32 + 698", "34801 - 2", "45 + 43", "123 + 49"]
    expected_output = "Error: Numbers cannot be more than four digits."
    assert arithmetic_arranger(problems, digit_limit=4) == expected_output

