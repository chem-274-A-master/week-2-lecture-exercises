"""Tests for module 3 - composition."""


def test_03_01_01():
    from M03Composition01 import Atom

    atom = Atom(protons=8, neutrons=10)

    assert atom.protons == 8, "The Atom protons attribute is not set correctly."
    assert atom.neutrons == 10, "The Atom neutrons attribute is not set correctly."
    assert atom.electrons == 8, "A neutral Atom should have one electron per proton."


def test_03_01_02():
    from M03Composition01 import Atom, Molecule

    atoms = [Atom(protons=6, neutrons=6), Atom(protons=8, neutrons=8)]
    molecule = Molecule(atoms)

    assert molecule.atoms == atoms, (
        "The Molecule atoms attribute should contain the supplied Atom objects."
    )


def test_03_01_03():
    from M03Composition01 import Atom, Molecule

    carbon = Atom(protons=6, neutrons=6)
    oxygen_1 = Atom(protons=8, neutrons=8)
    oxygen_2 = Atom(protons=8, neutrons=8)
    molecule = Molecule([carbon, oxygen_1, oxygen_2])

    assert molecule.total_electrons() == 22, (
        "A carbon dioxide molecule should have 22 total electrons."
    )

    # Ensure the method totals electrons rather than another Atom attribute.
    carbon.electrons = 5
    assert molecule.total_electrons() == 21, (
        "total_electrons should sum the electrons attribute of every Atom."
    )
