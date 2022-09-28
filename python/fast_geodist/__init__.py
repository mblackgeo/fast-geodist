from typing import Tuple, Union

import numpy as np

from ._fast_geodist import haversine as _haversine
from ._fast_geodist import haversine_array

__all__ = ["haversine"]
__version__ = "0.3.0"


def haversine(
    input: Union[np.ndarray, Tuple[float, float, float, float]]
) -> Union[np.ndarray, float]:
    """Calculate the Havesine distance between pairs of latitudes and longitudes

    Parameters
    ----------
    input : Union[np.ndarray, Tuple[float, ...]
        Either a 2D numpy array with 4 columns containing lat/lon pairs, e.g.
        np.array([lat1, lon1, lat2, lon2], [...]). For each row the distance
        will be calculated. Or if the input is a Tuple of 4 floats given as
        (lat1, lon1, lat2, lon2) the distance will be calculated.

    Returns
    -------
    Union[np.ndarray, float]
        Haversine distance in metres, either a float or array of floats based on
        the input that was given.
    """
    if isinstance(input, np.ndarray):
        if input.ndim != 2 and input.shape[1] != 4:
            raise ValueError(f"Input array must have shape [n, 4], got {input.shape}")
        return haversine_array(input)

    if not isinstance(input, tuple):
        raise NotImplementedError("Input must be a numpy array or tuple of floats")

    if len(input) != 4:
        raise ValueError(f"Input tuple must have exactly 4 elements, got {len(input)}")

    return _haversine(*input)
