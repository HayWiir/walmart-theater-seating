import pytest
from theater import *

def test_init():
    """
    Initializing theater class.
    """
    theater = Theater()

    assert(theater.available_seats == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20])
    assert(theater.reservations == [[], [], [], [], [], [], [], [], [], []])


def test_check_reservation():
    """
    Check available reservations
    """
    theater = Theater()

    theater.reservations = [[], [], [], [], [], [], [], [], [], []]
    assert(theater.available_ranges(5) == [[0,19]])

    theater.reservations = [[], [], [], [], [], [[7,16]], [], [], [], []]
    assert(theater.available_ranges(5) == [[0,6], [17,19]])

    theater.reservations = [[], [], [], [], [], [[7,10], [13,19]], [], [], [], []]
    assert(theater.available_ranges(5) == [[0,6], [11,12]])

    theater.reservations = [[], [], [], [], [], [[0,9], [13,14]], [], [], [], []]
    assert(theater.available_ranges(5) == [[10,12], [15,19]])

    theater.reservations = [[], [], [], [], [], [[5,9], [13,14]], [], [], [], []]
    assert(theater.available_ranges(5) == [[0,4], [10,12], [15,19]])

    theater.reservations = [[], [], [], [], [], [[0,19]], [], [], [], []]
    assert(theater.available_ranges(5) == [])



def test_add_reservation():
    """
    Test add_reservation function
    """
    theater = Theater()
    theater.reservations = [[], [], [], [[7,16]], [], [], [], [], [], []]

    theater.add_reservation(3, [18,19])
    theater.add_reservation(3, [1,3])
    theater.add_reservation(3, [4,6])

    # print(theater.reservation/s)

    assert(theater.reservations == [[], [], [], [[1,16], [18,19]], [], [], [], [], [], []])

    
# print(test_add_reservation())

def test_reserve():
    theater = Theater()
    
    assert(theater.reserve(5) == ['F1', 'F2', 'F3', 'F4', 'F5'])


def test_reserve_no_buffer():
    theater = Theater()

    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    #All rows are full (except 5 seats per row, buffer can't be used for more than 2 bookings)

    assert(theater.reserve(5) == ['F16', 'F17', 'F18', 'F19', 'F20'])

def test_reserve_separate():
    theater = Theater()

    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)
    theater.reserve(15)

    #All rows are full (except 1 seat per row, more than one reservations will be separate)
    assert(theater.reserve(9) == ['F19', 'F20', 'G19', 'G20', 'E19', 'E20', 'H19', 'H20', 'I19'])
    assert(theater.reserve(15) == ['F16', 'F17', 'F18', 'G16', 'G17', 'G18', 'E16', 'E17', 'E18', 'H16', 'H17', 'H18', 'I16', 'I17', 'I18'])

def test_reserve_excess():
    theater = Theater()

    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    theater.reserve(19)
    #All rows are full (except 1 seat per row, more than one reservations will be separate)
    assert(theater.reserve(20) == [])    