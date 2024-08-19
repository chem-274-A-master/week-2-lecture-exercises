"""
Dunder method exercise

Add a `__str__` method to your Bond class. 
This version of the Bond class does not need to have a stretch method.

When print is called on an instance, it should print 'Bond with length BONDLENGTH between atoms ATOM1 and ATOM2.'
Replace 'BONDLENGTH', 'ATOM1', and 'ATOM2' with the appropriate instance attributes (length and atoms). 
Make sure to include the punctuation (a period at the end of the sentence).

"""

# Write your solution here.

if __name__ == "__main__":
  bond = Bond(["C", "H"], 1.09)

  # This will print 'Bond with length 1.09 between atoms C and H.'
  print(bond)
