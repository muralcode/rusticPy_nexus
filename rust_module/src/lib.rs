use pyo3::prelude::*;

mod data_transform;
mod aggregation;
mod analysis;

#[pymodule]
fn rust_module(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(data_transform::transform, m)?)?;
    m.add_function(wrap_pyfunction!(aggregation::aggregate, m)?)?;
    m.add_function(wrap_pyfunction!(analysis::analyze, m)?)?;
    Ok(())
}
