"""
Tests for module 2 - inheritance
"""

import os
import sys
import pytest

# get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# add the parent directory to the path
sys.path.append(parent_dir)

# Test for the custom exception
def test_02_01_01():

    from M02Inheritance01 import InvalidDistanceError, is_bond

    with pytest.raises(InvalidDistanceError, match="Distance must be greater than or equal to zero."):
        is_bond(-0.5)

def test_02_01_02():

    from M02Inheritance01 import is_bond

    # This test checks that a valid distance does not raise an exception and returns the correct value.
    result = is_bond(0.5)
    assert result is True, "The function should return True for a distance within the bonding range."

def test_02_01_03():

    from M02Inheritance01 import is_bond

    # This test checks that a distance above max_distance does not raise an exception but returns False.
    result = is_bond(1.0)
    assert result is False, "The function should return False for a distance above the max bonding distance."

def test_02_02_01():

    from M02Inheritance02 import Ion

    # Create an Ion with a positive charge
    ion = Ion(protons=10, neutrons=10, charge=1)
    
    # With a positive charge, the number of electrons should be less than the number of protons
    assert ion.electrons == 9, "Ion with +1 charge should have one less electron than protons."

def test_02_02_02():

    from M02Inheritance02 import Ion

    # Create an Ion with a negative charge
    ion = Ion(protons=10, neutrons=10, charge=-1)
    
    # With a negative charge, the number of electrons should be more than the number of protons
    assert ion.electrons == 11, "Ion with -1 charge should have one more electron than protons."

def test_02_02_03():

    from M02Inheritance02 import Ion

    # Create an Ion with a neutral charge (should behave like an Atom)
    ion = Ion(protons=10, neutrons=10, charge=0)
    
    # With a neutral charge, the number of electrons should equal the number of protons
    assert ion.electrons == 10, "Ion with neutral charge should have electrons equal to protons."