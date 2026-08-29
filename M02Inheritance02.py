"""
Inheritance Exercise

Consider the sample Atom class below. It assumes a neutral charge, i.e., the number of electrons is equal to the number of protons.

Create a class called Ion that inherits from Atom.
Add an extra argument called "charge" to the Ion constructor.
Use super() to call the constructor of the Atom class, and then modify the number of electrons according to the charge.
Use type hints for every parameter and return value.
"""


class Atom:
    def __init__(self, protons: int, neutrons: int) -> None:
        self.protons: int = protons
        self.electrons: int = protons
        self.neutrons: int = neutrons


# Write your Ion class here.


if __name__ == "__main__":
    my_ion = Ion(protons=10, neutrons=10, charge=1)
    print(f"My ion has {my_ion.electrons} electrons.")
