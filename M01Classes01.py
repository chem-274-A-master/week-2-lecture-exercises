"""
Constructor Exercise

Create a class to represent a chemical bond between atoms.

The constructor should take two arguments:

1. A list containing strings, where each string represents an atom involved in the bond.
2. A floating-point number representing the distance (bond length) between the atoms in the bond.

Store these values as instance attributes named 'atoms' and 'length', respectively.

See the __main__ function for example usage.
"""

if __name__ == "__main__":

  bond = Bond(["C", "H"], 1.09)

  # This will print 1.09
  print(bond.length)

  # This will print ["C", "H"]
  print(bond.atoms)