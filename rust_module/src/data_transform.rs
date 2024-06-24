use pyo3::prelude::*;

#[pyfunction]
pub fn transform(data: Vec<i32>) -> PyResult<Vec<i32>> {
    // Example transformation: multiply each element by 2
    Ok(data.into_iter().map(|x| x * 2).collect())
}
