"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return [number, number +1, number +2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if rounds.__contains__(number):
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    return float(sum(hand) / len(hand))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    calculated_average = card_average(hand)
    middle_index = len(hand) // 2
    
    if (hand[0] + hand[-1]) / 2  == calculated_average:
        return True
    # elif middle indexvalue = calculated average 
    elif hand[middle_index] == calculated_average:
        return True
    else:
        return False





def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    #init total variables outside of loop scope
    even_total = []
    odd_total = []
    
    # itterate therough hand 
    for index, num in enumerate(hand):
        #if the index is even
        if index % 2 == 0:
            #add to even total
            even_total.append(num)
        else:
            odd_total.append(num)
    
    even_avg = sum(even_total) / len(even_total)
    odd_avg = sum(odd_total) / len(odd_total)
    return even_avg == odd_avg



def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] += 11
    
    return hand
