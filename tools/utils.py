#!/usr/bin/env python
"""This script contains utility functions that are helpful
for the sound source localization script."""

import multiprocessing


class MultiProcessingWithReturnValue:
    """MultiProcessingWithReturnValue receives a function and its corresponding
       arguments, as in input, and runs the function on multiple cores.
       Each output is saved into a list and returned.

       Attributes:
           func: the function to run
           args: the function's arguments
    """
    def __init__(self, func, *args):
        """Initializes MultiProcessingWithReturnValue with func and *args."""
        self.func = func
        self.args = args

    def run(self, *args):
        """Run the function, with its correct function arguments."""
        return self.func(args[0][0], *args[0][1])

    def pooled(self):
        """Multi-process the function"""

        with multiprocessing.Pool() as pool:
            *sample_output, = pool.map(self.run, self.args)
        return sample_output


def set_microphone_locations():
    """Returns microphone locations list. The x dimension,
       y dimension, and z dimension serve as optional input
       arguments. Note: For the default case, the microphone
       locations are under a new coordinate system in relation
       to the center of the room
       (whose center = [(0.34925/2),(0.219964/2),(0.2413/2)] is the origin)

      Returns:
          List of lists which contains the microphone coordinates
    """

    # Microphone x,y,z locations
    x_locations = [-0.102235, -0.052197, -0.027304]
    y_locations = [-0.109982]
    z_locations = [0.056388, 0.001524, -0.053340, -0.108204]

    return [[x, y, z] for x in x_locations for y in y_locations
            for z in z_locations]
