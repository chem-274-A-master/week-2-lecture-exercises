"""
Composition Exercise

Composition allows one object to contain and use instances of another class.

Using your Atom class from M01, create a class called Molecule.

The Molecule constructor should take a list of Atom objects and store it
as an instance attribute named `atoms`.

Add an instance method called `total_electrons` that returns the total
number of electrons across all atoms in the molecule.

Be sure to practice using type hints!

See the __main__ function for example usage.
"""

# Add your Atom class here.

# Write your Molecule class here.


if __name__ == "__main__":
    oxygen = Atom(protons=8, neutrons=8)
    hydrogen_1 = Atom(protons=1, neutrons=0)
    hydrogen_2 = Atom(protons=1, neutrons=0)

    water = Molecule([oxygen, hydrogen_1, hydrogen_2])

    # This will print 10
    print(water.total_electrons())

    # This will print 8
    print(water.atoms[0].protons)