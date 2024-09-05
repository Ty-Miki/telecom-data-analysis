# **Overview**

The test suite ensures that each utility function and class method behaves as expected, with appropriate logging and error handling.

### **Utility Functions Tests**

1. **Test `load_environment_variables()`**
   * Verifies that environment variables are correctly loaded from a `.env` file, and appropriate logging is performed.
2. **Test `connect_to_database()`**
   * Ensures a database connection is established or fails gracefully with correct logging.
3. **Test `load_data_from_db()`**
   * Checks if data is loaded into a DataFrame from a specified table, with proper handling of errors.
4. **Test `close_database_connection()`**
   * Confirms that the database connection is closed successfully, with error logging on failure.

### **Class Tests: `MissingValueHandler`**

1. **Test `missing_value_summary()`**
   * Validates that the method returns accurate counts of missing values per column.
2. **Test `missing_value_percentage()`**
   * Ensures the method returns the correct percentage of missing values per column.
3. **Test `missing_values_heatmap()`**
   * Verifies that a heatmap of missing values is displayed without errors.
4. **Test `describe_numeric_columns()`**
   * Confirms that the method returns summary statistics for numeric columns.
5. **Test `value_counts_categorical()`**
   * Checks that value counts for a specified categorical column are accurate.
6. **Test `correlation_matrix()`**
   * Ensures the method returns an accurate correlation matrix of numerical columns.
7. **Test `inspect_outliers()`**
   * Verifies that boxplots for outliers are displayed for specified or all numeric columns.
