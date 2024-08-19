"""
Method Exercise

In the previous exercise, you wrote a class called Bond where the constructor took two arguments: 
a list containing strings and a floating-point number representing the distance between the atoms. 
These arguments are stored as attributes named 'atoms' and 'length', respectively.

Building on this class, add an instance method called "stretch". 
This method should take a float as its input parameter, representing a change in distance. 
In this method, update the 'length' attribute by adding the input parameter to its current value.

See the __main__ function for example usage.
"""

# Write your class here

if __name__ == "__main__":

  bond = Bond(["C", "H"], 1.09)

  # This will print 1.09
  print(bond.length)

  # Stretch the bond by 0.02
  bond.stretch(0.02)

  # This will print 1.11
  print(bond.length)