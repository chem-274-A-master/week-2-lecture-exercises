"""
In Python, one common use of inheritance is to create custom exceptions that are more descriptive for specific situations. In this exercise, you will create a custom exception class called `InvalidDistanceError`. Your custom exception should inherit from Python's built-in `Exception` class.

After defining your custom exception, modify the given `is_bond` function below to raise your `InvalidDistanceError` when the `distance` parameter is negative. The exception should carry a message stating that "Distance must be greater than or equal to zero."

"""

# write your custom exception here

def is_bond(distance: float, max_distance: float=0.95):
    """
    Returns check if bond based on distance criterion
    
    Parameters
    ----------
    distance: float
        The distance between two atoms.
    
    max_distance: float, Optional, default=0.95
        The maximum distance for two atoms to be considered bonded.
    
    Returns
    -------
    bool
    Whether atoms are bonded.
    """

    # Finish this function and use your custom exception.


if __name__ == "__main__":
    # This will raise an exception
    is_bond(-1)
  