----------------------
### Steps So Far Followed & Results Achieved:

**1. Data Cleaning**
* Found No missing Values, No duplicates, No inconsistent data.
* Stripped Trailing Spaces in Column names & Renamed Column name (`Turnover (₹ Cr)` to `Turnover (Cr Rs)`).
* Changed Data type of `Date` Attribute from Object to datetime64[ns].
* Saved the cleaned dataset.

-----

**2. Descriptive Statistical Analysis**
* Found Coefficient of Variation, Median & Mode, Skewness coefficient for numerical columns.
* Found potential outliers and right-skewed in `Shares Traded` & `Turnover` attributes.

-----

**3. Exploratory Data Analysis**
* Confirmed Presence of Outliers in `Shares Traded` & `Turnover` attributes using Histogram plots and boxplots.
* Positive Strong Correlation exists between Open & High, Open & Low, Open & Close, Shares Traded & Turnover.
* The data is Cyclical between any variable and the Date variable.

-----

**4. Data Preprocessing**
* Feature Engineering: `Daily Range = High - Low`, found to have outliers even though features `High` and `Low` doesn't possessed.
* Dropped some columns that causes multicollinearity.
* Applied Log Transformation and Capping to handle outliers but found ineffective, also underperforms than unprocessed data.
* Saved data that only pre-processed, `preprocessed_simple_data.csv` and also saved another dataset which is pre-processed and added engineered features, `preprocessed_engineered_data.csv`.

-----

**5. Feature Transformation**
* Tried Log Transformation, Yeo-Johnson Method and also Box-cox But none of these 3 worked better on `Shares Traded` & `Turnover` attributes.

-----

**6. Regression Model**
* Dropped `Date` column.
* Split the dataset with 80% for training while rest for testing.
* Scaled the dataset.
* Tried training model on different dataset,
    * only cleaned - `cleaned_nifty50.csv`
    * cleaned & preprocessed (Applied Log transformation on TurnOver attribute) - `preprocessed_simple_data.csv`
    * cleaned, Preprocessed, feature engineered, dropped columns - `preprocessed_engineered_data.csv`
    * Found linear regression model that trained on cleaned data outperforming others.
    * Found Log transformation isn't appropriate technique.
    * Found linear regression model outperforms random forest regressor.
    * Compared Predicted value & Actual values and also plotted using residual plot as well as scatter plot.

-----

**RESULT**:

Linear Regression Model:
* Root Mean Squared Error: 70.21451114333215
* Mean Squared Error: 4930.08
* R-squared: 99.0%

-----

**To load the model:**

`import joblib`

`loaded_linear_model = joblib.load('linear_regression_model.joblib')`

----------------------