#[cfg(test)]
mod tests {
    use super::super::data_transform;
    use super::super::aggregation;
    use super::super::analysis;

    #[test]
    fn test_transform() {
        let data = vec![1, 2, 3, 4];
        let result = data_transform::transform(data);
        assert_eq!(result, vec![2, 4, 6, 8]);
    }

    #[test]
    fn test_aggregate() {
        let data = vec![1, 2, 3, 4];
        let result = aggregation::aggregate(data);
        assert_eq!(result, 10);
    }

    #[test]
    fn test_analyze() {
        let data = vec![1, 2, 3, 4];
        let result = analysis::analyze(data);
        assert_eq!(result, 2.5);
    }
}
