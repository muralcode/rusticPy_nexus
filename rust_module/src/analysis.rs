use pyo3::prelude::*;

#[pyfunction]
pub fn analyze(data: Vec<i32>) -> PyResult<f64> {
    // Example analysis: calculate mean
    let sum: i32 = data.iter().sum();
    let count = data.len();
    Ok(sum as f64 / count as f64)
}
