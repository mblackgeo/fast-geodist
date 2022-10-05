use ndarray::parallel::prelude::{IndexedParallelIterator, IntoParallelIterator, ParallelIterator};
use ndarray::{Array1, Array2, ArrayView2, Axis};
use numpy::{IntoPyArray, PyArray1, PyReadonlyArray2};
use pyo3::prelude::{pyfunction, pymodule, wrap_pyfunction, PyModule, PyResult, Python};

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

pub fn haversine_distance_array(x: &ArrayView2<f64>) -> Array1<f64> {
    let mut distances = Vec::with_capacity(x.shape()[0]);
    x.axis_iter(Axis(0))
        .into_par_iter()
        .map(|row| haversine_distance(row[0], row[1], row[2], row[3]))
        .collect_into_vec(&mut distances);

    Array1::from(distances)
}

pub fn haversine_combinations(arr1: &ArrayView2<f64>, arr2: &ArrayView2<f64>) -> Array2<f64> {
    // TODO panic if arr1 and arr2 aren't the same shape
    let out = Array2::zeros((arr1.shape()[0], arr2.shape()[0]));

    // TODO implement
    out
}

/// Python wrappers
#[pyfunction]
fn haversine(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> PyResult<f64> {
    Ok(haversine_distance(lat1, lng1, lat2, lng2))
}

#[pyfunction]
fn haversine_array<'py>(py: Python<'py>, x: PyReadonlyArray2<f64>) -> &'py PyArray1<f64> {
    let res = haversine_distance_array(&x.as_array());
    res.into_pyarray(py)
}

/// Python module
#[pymodule]
fn _fast_geodist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(haversine, m)?)?;
    m.add_function(wrap_pyfunction!(haversine_array, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use approx::assert_relative_eq;
    use ndarray::array;

    #[test]
    fn test_haversine_1() {
        let res = haversine_distance(0.0, 0.0, 1.0, 0.0);
        let expect = 111195.0802335329_f64;
        assert_relative_eq!(res, expect, epsilon = 1.0e-6)
    }

    #[test]
    fn test_haversine_2() {
        let res = haversine_distance(42.3521, -72.1235, 70.612, 72.1260);
        let expect = 7130580.307935911_f64;
        assert_relative_eq!(res, expect, epsilon = 1.0e-6)
    }

    #[test]
    fn test_haversine_array() {
        let arr = array![[42.3521, -72.1235, 70.612, 72.1260], [0.0, 0.0, 1.0, 0.0]];

        let res = haversine_distance_array(&arr.view());
        let expect = [7130580.307935911, 111195.0802335329];

        assert_relative_eq!(res[0], expect[0], epsilon = 1.0e-6);
        assert_relative_eq!(res[1], expect[1], epsilon = 1.0e-6);
    }

    #[test]
    fn test_haversine_comb() {
        let arr1 = array![[45.7597, 4.8422], [51.509865, -0.118092]];
        let arr2 = array![[48.8567, 2.3508], [40.7033962, -74.2351462]];

        let res = haversine_combinations(&arr1.view(), &arr2.view());
        let expect = array![[392217.25956, 343374.55271], [6163436.38211, 5586484.47423]];

        for i in 0..expect.shape()[0] {
            for j in 0..expect.shape()[1] {
                assert_relative_eq!(res[(i, j)], expect[(i, j)], epsilon = 1.0e-6);
            }
        }
    }
}
