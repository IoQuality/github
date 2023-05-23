import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **args):
        """
        Initializes a Hat object with a variable number of balls.

        The balls are represented as a list of strings, where each string is the color of a ball.

        :param args: A variable number of keyword arguments
                     key (str) is the color of the ball
                     value (int) is the number of balls of that color

        The drawn_balls list is initialized for the draw method.

        Using the key-value pair (color=num_of_balls) from the input, the *color* of the ball is extracted and
        added to the list as many times as many balls of that color (num_of_balls) were passed to the class.
        The *extend method* allows adding multiple values to the list at once.
        """
        self.drawn_balls = []
        self.contents = []
        try:
            self.contents.extend([color for color, num_of_balls in args.items() for _ in range(num_of_balls)])
        except TypeError:
            print(f"Error: invalid key or value entered {args.items() = }. Nothing will be added to the hat.")

    def __str__(self):
        return f"Hat(contents={self.contents})"

    def __repr__(self):
        return f"Hat(contents={self.contents})"

    def draw(self, num_balls_drawn: int) -> list[str]:
        """
        Picks balls at random from the hat and removes them (if possible).

        :param num_balls_drawn: The number of balls to draw from the hat.
                                When *num_balls_drawn* is greater than or equal to the total number of balls in the hat,
                                the method removes all the balls from the hat.

        :return drawn_balls: A list of strings representing the colors of the drawn balls.
                                        (required by the unit test 2)

        The *random.sample* method is used to pick random number (num_balls_drawn) of balls from the contents pool.
        The contents of the hat are updated by removing the balls matching drawn_balls.
        """
        if num_balls_drawn >= len(self.contents):
            self.drawn_balls = self.contents
            self.contents = []
        else:
            self.drawn_balls = random.sample(self.contents, num_balls_drawn)
            for ball in self.drawn_balls:
                self.contents.remove(ball)
        return self.drawn_balls


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    """
    Conducts a series of experiments (num_experiments) to determine the probability of drawing a specific set of balls
    from the hat.
    :param hat: an instance of the class Hat. Each hat contains at least one colored ball
    :param num_balls_drawn: how many balls will be drawn from the hat
    :param num_experiments: how many times will the experiment be run
    :param expected_balls: An expected dictionary of drawn balls for the experiment
    :return: probability - number of successful experiments divided by the number of experiments performed

    First data validation occurs. Num_of_balls must be an int as well as num_balls_drawn and num_experiment which are
    reset to 0 if incorrect data has been assigned.
    The *copied_hat* is a copy of hat and will be used for the experiments, the original *hat* will be used to reset
    the *copied_hat* before each experiment

    The successful_experiment variable is reset before each experiment. The *subset_of_dictionary* function returns
    True for a successful match. Each match adds 1 to the successful_experiment variable.
    
    The *Counter* object is a subclass of dict class implemented in C that allows you to count the occurrences of
    elements in a list, which allows to efficiently compute *drawn_balls* *Counter object* (a dictionary) from the
    *copied_hat.drawn_balls* list.
    """

    for num_of_balls in expected_balls.keys():
        if not isinstance(expected_balls[num_of_balls], int):
            print(TypeError(f"Error: invalid value entered: expected_balls={expected_balls}.\n"
                            f"Setting the ball value to 0."))
            expected_balls[num_of_balls] = 0
    try:
        num_balls_drawn = int(num_balls_drawn)
        num_experiments = int(num_experiments)
    except ValueError:
        print(TypeError(f"Error: invalid value entered:\n"
                        f"{type(num_balls_drawn) = }\n"
                        f"{type(num_experiments) = }\n"
                        f"Setting num_balls_drawn and num_experiments to 0."))
        num_balls_drawn = 0
        num_experiments = 0

    successful_experiment = 0
    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        copied_hat.draw(num_balls_drawn)
        drawn_balls = convert_list_to_dict(copied_hat.drawn_balls)
        successful_experiment += subset_of_dictionary(drawn_balls, expected_balls)

    if num_experiments == 0:
        print(ZeroDivisionError(f"No experiments have been run"))
        return 0
    else:
        return successful_experiment / num_experiments


def subset_of_dictionary(big_dictionary: dict, small_dictionary: dict) -> bool:
    """
    This function checks if the *small_dictionary* is contained within the *big_dictionary*.

    :param big_dictionary: the big dictionary
    :param small_dictionary: a smaller dictionary which is a potential subset of the bigger dictionary
    :return bool: True if the keys and their matching values inside the *big_dictionary* were equal or greater than the
                  keys and their matching values in *small_dictionary*.
    """
    return all(key in big_dictionary and small_dictionary[key] <= big_dictionary[key] for key in small_dictionary)


def convert_list_to_dict(change_from: list[str]) -> dict:
    """
    Function converts a lit of strings to a collections.Counter dictionary
    :param change_from: data to change
    :return: dictionary

    TODO: expand to more conversions
    """
    if isinstance(change_from, list) is True:
        return Counter(change_from)
    else:
        return {}
