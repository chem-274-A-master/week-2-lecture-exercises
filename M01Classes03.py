"""
Class and Instance Attributes Exercise

Using your Bond class definition from the previous exercises, 
add a class attribute called `conversion_factor` that holds the conversion factor to convert nanometers to Ångström (you will need to figure out what the conversion factor is).

Modify your `stretch` instance method to take an optional argument named "angstrom". The default value for this optional argument should be True.

If False is passed for this argument, 
the method should assume that the user is inputting the length in units of nanometers. 
Use the class attribute `conversion_factor` to convert the input argument to Ångström before updating the bond length.

See the __main__ function for example usage.

"""

# Write your class here

if __name__ == "__main__":
    # This will print the conversion factor for nanometers to angstrom
    print(Bond.conversion_factor)
    
    bond = Bond(["C", "H"], 1.09)
    
    # This will also print the conversion factor for nanomters to angstrom
    print(bond.conversion_factor)
    
    # This will print 1.09
    print(bond.length)
    # Stretch the bond by 0.02 nm
    bond.stretch(0.02, angstrom=False)
    
    # This will print 1.29
    print(bond.length)

    # Convert it back.
    bond.stretch(-0.2)
    
    # This will print the original bond length
    print(bond.length)