from itertools import chain
from typing import List, Tuple, Union

import numpy as np

from ._fast_geodist import haversine as _haversine
from ._fast_geodist import haversine_array

__all__ = ["haversine"]
__version__ = "0.4.0"


def haversine(
    *args: Union[
        np.ndarray,
        Tuple[Tuple[float, float], Tuple[float, float]],
        List[Tuple[Tuple[float, float], Tuple[float, float]]],
    ]
) -> Union[np.ndarray, List[float], float]:
    """Calculate the Haversine distance between pairs of latitudes and longitudes

    Parameters
    ----------
    args
        If input is a 2D numpy array with 4 columns containing lat/lon pairs, e.g.
        np.array([lat1, lon1, lat2, lon2], [...]). For each row the distance
        will be calculated.
        If the input is list a of tuples [((lat1, lon1), (lat2, long2))], the distance
        for each pair will be calculated.
        If the input is just a pair of tuples (lat1, lon1), (lat2, long2) the distance
        will be returned between the coordinates.

    Returns
    -------
    Union[np.ndarray, List[float], float]
        Haversine distance in metres, either a float or array/list of floats based on
        the input that was given.
    """
    if len(args) == 1:
        if isinstance(args[0], list):
            # must have an even number of coordinates (i.e. pairs)
            coords = args[0]
            if len(coords) % 2 != 0:
                raise ValueError(
                    f"An odd number of coordinate pairs was supplied : {len(coords)}"
                )

            # reshape and cast to a numpy array, return a list
            # TODO do this without going through numpy
            arr = np.array([list(chain(*c)) for c in coords])
            return list(haversine_array(arr))

        elif isinstance(args[0], np.ndarray):
            if args[0].ndim != 2 and args[0].shape[1] != 4:
                raise ValueError(
                    f"Input array must have shape [n, 4], got {args[0].shape}"
                )
            return haversine_array(args[0])

        else:
            raise NotImplementedError

    elif len(args) == 2:
        # should be a tuple of size 2 with 2 coordinate pairs
        if not isinstance(args, tuple):
            raise NotImplementedError(
                "Input must be a numpy array, tuple, or list of tuples"
            )

        if len(args) == 2:
            return _haversine(*args[0], *args[1])

    raise NotImplementedError(f"No implementation for {type(args)}")
