"""
Test for module 1 week 2 - Python classes
"""

import os
import sys

# get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# add the parent directory to the path
sys.path.append(parent_dir)

def test_01_01():

    from M01Classes01 import Bond

    # Test case: Bond between O and H with a bond length of 0.96
    bond = Bond(["O", "H"], 0.96)
    
    # Assert atoms attribute is set correctly
    assert bond.atoms == ["O", "H"], "Atoms attribute is not set correctly."
    
    # Assert length attribute is set correctly
    assert bond.length == 0.96, "Length attribute is not set correctly."

def test_01_02():

    from M01Classes02 import Bond

    # Test case: Bond between N and H with a bond length of 1.02
    bond = Bond(["N", "H"], 1.02)
    
    # Assert initial length is correct
    assert bond.length == 1.02, "Initial bond length is incorrect."
    
    # Stretch the bond by 0.05
    bond.stretch(0.05)
    
    # Assert length attribute is updated correctly
    assert bond.length == 1.07, "Bond length after stretching is incorrect."
    
    # Stretch the bond by -0.02 (contracting)
    bond.stretch(-0.02)
    
    # Assert length attribute is updated correctly
    assert bond.length == 1.05, "Bond length after contracting is incorrect."

def test_01_03_01():

    from M01Classes03 import Bond

    # Test that the conversion factor is correct
    assert Bond.conversion_factor == 10.0, "Conversion factor should be class attribute set to conversion factor from nanometers to Ångström."

def test_01_03_02():

    from M01Classes03 import Bond

    # Create a bond with initial length 1.09 Ångström
    bond = Bond(["O", "H"], 1.09)
    
    # Stretch the bond by 0.02 Ångström
    bond.stretch(0.02)
    
    # Assert the length is updated correctly
    assert bond.length == 1.11

def test_01_03_03():

    from M01Classes03 import Bond

    # Create a bond with initial length 1.09 Ångström
    bond = Bond(["O", "H"], 1.09)
    
    # Stretch the bond by 0.02 nanometers (should be converted to 0.2 Ångström)
    bond.stretch(0.02, angstrom=False)
    
    # Assert the length is updated correctly
    assert bond.length == 1.29