use _fast_geodist::haversine_distance_array;
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use ndarray::Array;
use ndarray_rand::rand_distr::Uniform;
use ndarray_rand::RandomExt;

pub fn criterion_benchmark(c: &mut Criterion) {
    let arr = Array::random((1_000_000, 4), Uniform::new(-90.0, 90.0));

    c.bench_function("array", |b| {
        b.iter(|| haversine_distance_array(black_box(&arr.view())))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
