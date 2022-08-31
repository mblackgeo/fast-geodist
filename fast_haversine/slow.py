import math


def slow_haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """A pure python implementation of Haversine distance

    This function is implemented following the ArcGIS documentation at
    https://bit.ly/3wKKYo1. It is provided here as a convenience to perform
    benchmarks against the Rust implementation.

    Parameters
    ----------
    lat1 : float
        First point latitude
    lng1 : float
        First point longitude
    lat2 : float
        Second point latitude
    lng2 : float
        Second point longitude

    Returns
    -------
    float
        Haversine distance in metres
    """
    R = 6371008.8  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lng2 - lng1)

    a = (
        math.sin(delta_phi / 2.0) ** 2
        + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
