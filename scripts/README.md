# **Utility Functions Documentation**

1. `load_environment_variables(parent_directory: str) - dict | None`

* Loads environment variables from a `.env` file located in the specified parent directory.
  - **Parameters** : `parent_directory (str)`: The directory containing the `.env` file.
  - **Returns** : `dict`: A dictionary of environment variables if successfully loaded; an empty dictionary otherwise.
  - **Logging** : Logs success or error messages during the loading process.

2. `connect_to_database(db_parameters: dict) -> psycopg2.extensions.Connection | None`

* Establishes a connection to a PostgreSQL database using the provided connection parameters.
  - **Parameters** : `db_parameters (dict)`: A dictionary of database connection parameters.
  - **Returns** : `Connection`: A psycopg2 connection object if successful; `None` otherwise.
  - **Logging** : Logs success or error messages during the connection process.

3. `load_data_from_db(conn: psycopg2.extensions.Connection, table_name: str) -> pd.DataFrame | None`

* Loads data from a specified table in a PostgreSQL database into a Pandas DataFrame.
  - **Parameters** :
    - `conn (Connection)`: A psycopg2 connection object.
    - `table_name (str)`: The name of the table to load data from.
  - **Returns** : `DataFrame`: A Pandas DataFrame containing the table data if successful; `None` otherwise.

  - **Logging** : Logs success or error messages during the data loading process.

4. `close_database_connection(conn: psycopg2.extensions.Connection) -> None`

* Closes the database connection.

  - **Parameters** : `conn (Connection)`: A psycopg2 connection object.
  - **Returns** : `None`.
  - **Logging** : Logs success or error messages during the connection closing process.

---

# **Data Processing Documentation**

## **Class Documentation: `MissingValueHandler`**

### **Overview**

- The `MissingValueHandler` class provides methods for inspecting, handling, and visualizing missing values in a Pandas DataFrame.

### **Class Initialization**

1. `__init__ (self, df: pd.DataFrame) -> None`
  * **Parameters** : `df (pd.DataFrame)`: The DataFrame to be inspected and handled.
  * **Logging** : Logs the creation of a `MissingValueHandler` instance.

### **Class Methods**

1. `missing_value_summary() -> pd.Series`
   * Returns the total number of missing values in each column.
   * **Logging** : Logs success or error during computation.
2. `missing_value_percentage() -> pd.Series`
   * Returns the percentage of missing values in each column.
   * **Logging** : Logs success or error during computation.
3. `missing_values_heatmap() -> None`
   * Displays a heatmap showing the distribution of missing values.
   * **Logging** : Logs success or error during visualization.
4. `describe_numeric_columns() -> pd.DataFrame`
   * Returns summary statistics for numeric columns.
   * **Logging** : Logs success or error during computation.
5. `value_counts_categorical(column_name: str) -> pd.Series`
   * Returns value counts for a specified categorical column.
   * **Parameters** : `column_name (str)`: The name of the column to compute value counts for.
   * **Logging** : Logs success or error during computation.
6. `correlation_matrix() -> pd.DataFrame`
   * Returns the correlation matrix of numerical columns.
   * **Logging** : Logs success or error during computation.
7. `inspect_outliers(columns: list = None) -> None`
   * Displays boxplots to inspect outliers in numeric columns.
   * **Parameters** :`columns (list)`: A list of column names to inspect; inspects all numeric columns if `None`.
   * **Logging** : Logs success or error during visualization.
