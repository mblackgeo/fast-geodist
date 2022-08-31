use approx::assert_relative_eq;
use fast_haversine::{haversine_distance, haversine_distance_array};
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

    let res = haversine_distance_array(&arr);
    let expect = [7130580.307935911, 111195.0802335329];

    assert_relative_eq!(res[0], expect[0], epsilon = 1.0e-6);
    assert_relative_eq!(res[1], expect[1], epsilon = 1.0e-6);
}
