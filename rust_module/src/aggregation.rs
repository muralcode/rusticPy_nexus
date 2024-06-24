use pyo3::prelude::*;

#[pyfunction]
pub fn aggregate(data: Vec<i32>) -> PyResult<i32> {
    // Example aggregation: sum of elements
    Ok(data.into_iter().sum())
}
