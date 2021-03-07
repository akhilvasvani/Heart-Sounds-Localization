#!/usr/bin/env python
"""This script contains utility functions that are helpful
for the sound source localization script."""

import threading
import multiprocessing

from scripts.validations import ValidateList


class MultiProcessingWithReturnValue(object):
    def __init__(self, func, *args):
        """Define the function and function arguments to be multi-processed"""
        self.func = func
        self.args = args

    def run(self, *args):
        """Run the function, with its correct function arguments"""
        return self.func(args[0][0], *args[0][1])

    def pooled(self):
        """Multi-process the function"""

        with multiprocessing.Pool() as pool:
            *a, = pool.map(self.run, self.args)
        return a


class ThreadWithReturnValue(threading.Thread):
    """Created a Thread subclass. It is a workable do around,
       but it accesses "private" data structures that are specific
       to Thread implementation.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the thread object."""
        super().__init__(*args, **kwargs)
        self._return = None

    def run(self):
        """Runs the function if specified for the thread."""
        target = getattr(self, '_target')
        if target is not None:
            self._return = target(*getattr(self, '_args'), **getattr(self,
                                                                     '_kwargs'))

    def join(self, *args, **kwargs):
        """Returns the value of target function running in the thread."""
        super().join(*args, **kwargs)
        return self._return


# @ValidateList
# def convert_to_one_list(sample_list):
#     """Converts a list of a list into a single list.
#
#     Args:
#         sample_list: the input list to convert
#
#     Returns:
#         output_list: a single list
#     """
#
#     output_list = []
#     for item in sample_list:
#         if isinstance(item, list):
#
#             # Call this function on it and append its each value separately.
#             # If it has more lists in it this function will call itself again
#             for i in convert_to_one_list(item):
#                 output_list.append(i)
#         else:
#             output_list.append(item)
#     return output_list
#
#
# @ValidateList
# def check_list_of_lists_are_same_length(sample_list):
#     it = iter(sample_list)
#     the_len = len(next(it))
#     return False if not all(len(small_list) == the_len for small_list in it) else True
