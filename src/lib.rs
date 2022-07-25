use itertools::izip;
use pyo3::prelude::*;

/// Mean radius of Earth in meters
/// This is the value recommended by the IUGG:
/// Moritz, H. (2000). Geodetic Reference System 1980. Journal of Geodesy, 74(1), 128–133. doi:10.1007/s001900050278
/// "Derived Geometric Constants: mean radius" (p133)
/// https://link.springer.com/article/10.1007%2Fs001900050278
/// https://sci-hub.se/https://doi.org/10.1007/s001900050278
/// https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
/// Source: https://github.com/georust/geo/blob/main/geo/src/lib.rs
const MEAN_EARTH_RADIUS: f64 = 6371008.8;

/// Calculate the Haversine (or Great Circle) distnace between two points
pub fn haversine_distance(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> f64 {
    // Following https://github.com/georust/geo/blob/main/geo/src/algorithm/haversine_distance.rs
    // Lat = Y, Lng = X
    let theta1 = lat1.to_radians();
    let theta2 = lat2.to_radians();

    let delta_theta = (lat2 - lat1).to_radians();
    let delta_lambda = (lng2 - lng1).to_radians();

    let a = (delta_theta / 2.0).sin().powi(2)
        + theta1.cos() * theta2.cos() * (delta_lambda / 2.0).sin().powi(2);

    let c = 2.0 * a.sqrt().asin();
    MEAN_EARTH_RADIUS * c
}

/// Python wrapper
#[pyfunction]
fn haversine(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> PyResult<f64> {
    Ok(haversine_distance(lat1, lng1, lat2, lng2))
}

#[pyfunction]
fn haversine_vec(
    lats1: Vec<f64>,
    lngs1: Vec<f64>,
    lats2: Vec<f64>,
    lngs2: Vec<f64>,
) -> PyResult<Vec<f64>> {
    let mut res = vec![0_f64; lats1.len()];
    for (lat1, lng1, lat2, lng2) in izip!(&lats1, &lngs1, &lats2, &lngs2) {
        res.push(haversine_distance(*lat1, *lng1, *lat2, *lng2))
    }
    Ok(res)
}

/// A Python module implemented in Rust.
#[pymodule]
fn fast_haversine(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(haversine, m)?)?;
    m.add_function(wrap_pyfunction!(haversine_vec, m)?)?;
    Ok(())
}
