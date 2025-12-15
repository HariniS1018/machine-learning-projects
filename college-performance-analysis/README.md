### Project Title: College Performance Analysis & Graduation Rate Prediction

**Overview:**
This project involves a comprehensive data analysis and machine learning pipeline applied to the `College.csv` dataset, which contains various attributes for 777 US universities and colleges. The primary goal is to gain insights into factors influencing college characteristics and to build a predictive model for `Grad.Rate` (Graduation Rate), a key indicator of institutional success.

**Key Features Explored:**
* `Private`: Public/private indicator
* `Apps`: Number of applications received
* `Accept`: Number of applicants accepted
* `Enroll`: Number of new students enrolled
* `Outstate`: Out-of-state tuition
* `Expend`: Instructional expenditure per student
* `S.F.Ratio`: Student/faculty ratio
* And many more...

**Methodology:**

1.  **Data Loading & Initial Assessment:** Loaded the dataset using Pandas, performed initial data inspection, renamed columns, and handled indexing. Checked for missing values and obtained descriptive statistics.
2.  **Exploratory Data Analysis (EDA): (WIP)**
    * Conducted univariate analysis using histograms and boxplots to understand the distribution of numerical variables and identify outliers.
    * Performed bivariate analysis using correlation heatmaps and scatter plots to visualize relationships between numerical features.
    * Utilized count plots, box plots, and violin plots to compare numerical attributes across categorical groups (e.g., `Private` vs. `Public` colleges).
    * Identified key trends, distributions, and potential data quality issues.
3.  **Data Preprocessing & Feature Engineering: (WIP)**
    * Addressed identified outliers through appropriate transformations or handling strategies.
    * Engineered new features (e.g., `AcceptanceRate`, `EnrollmentRate`) to potentially improve model performance and derive new insights.
    * Encoded the categorical `Private` variable for machine learning compatibility.
    * Split the dataset into training and testing sets and applied feature scaling (StandardScaler) to numerical features.
4.  **Machine Learning Model Development: (WIP)**
    * Selected and trained several regression models, including [e.g., Linear Regression, Random Forest Regressor, Gradient Boosting Regressor].
    * Evaluated model performance using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared.
    * [Optional: Performed hyperparameter tuning using GridSearchCV/RandomizedSearchCV to optimize model performance.]
    * [Optional: Analyzed feature importance to understand which variables contribute most to graduation rate prediction.]

**Tools & Technologies:**
* Python
* Pandas (for data manipulation)
* NumPy (for numerical operations)
* Matplotlib (for basic plotting)
* Seaborn (for advanced statistical visualizations)
* Scikit-learn (for machine learning models and preprocessing)

---
**Insights Gained from Exploratory Data Analysis (EDA)**
Through comprehensive data exploration, I uncovered several key characteristics and relationships within the `College.csv` dataset:

* **Data Quality Identified:**
    * Confirmed the dataset has **no missing values** across all attributes, indicating good initial data integrity.
    * Identified a **data error in 'Grad.Rate'** where one institution reported a graduation rate of 118%, which will require specific handling during preprocessing (e.g., capping at 100%).

* **Presence of Outliers & Skewness:**
    * Statistical analysis (Coefficient of Variation, Mean vs. Median vs. Mode, Skewness Coefficient) and visualizations (histograms, boxplots) confirmed the **presence of significant right-skewed outliers** in key attributes like `Apps`, `Accept`, `Enroll`, `F.Undergrad`, `P.Undergrad`, `Outstate`, and `Expend`.
    * This suggests a substantial number of institutions fall within a typical range, while a few are exceptionally large or expensive, receiving disproportionately high applications/enrollments or having very high expenditures. This finding is crucial for selecting appropriate models or considering data transformations.

* **Key Variable Relationships Discovered:**
    * **Strong Positive Correlations:** A clear positive correlation exists between:
        * `Apps` (Applications) and `Accept` (Acceptances): Colleges receiving more applications also tend to accept more students.
        * `Accept` and `Enroll` (Enrollment): More accepted students typically lead to higher enrollment.
        * `Apps`/`Accept`/`Enroll` and `F.Undergrad` (Full-time Undergraduates): Larger institutions, characterized by higher application/acceptance/enrollment volumes, generally have more full-time undergraduate students.
        * `PhD` (Percent of faculty with Ph.D.s) and `Terminal` (Percent of faculty with terminal degrees): An increase in faculty with PhDs correlates with a rise in faculty holding terminal degrees overall.
    * **Inverse Relationship:** A notable inverse relationship was observed between `S.F.Ratio` (Student/Faculty Ratio) and `Expend` (Instructional Expenditure per student). This suggests that as the student-to-faculty ratio decreases (implying smaller class sizes or more faculty per student), the instructional expenditure per student tends to increase.

* **Important Caveat:** While strong correlations were identified, it's essential to remember that **correlation does not imply causation**. Further analysis is necessary to understand the underlying drivers and complex relationships between these variables.
---

**How to Run:**
1.  Clone this repository: `git clone https://github.com/HariniS1018/College-Performance-Analysis-and-Graduation-Rate-Prediction.git`
2.  Navigate to the project directory: `cd College-Performance-Analysis-and-Graduation-Rate-Prediction`
3.  Install dependencies: `pip install -r requirements.txt`
4.  Open the Jupyter Notebook: `data_exploration.ipynb`

**Future Enhancements:**
* Explore advanced feature engineering techniques.
* Experiment with more sophisticated machine learning models or ensemble methods.
* Deploy the model as a simple web application.
* Perform clustering analysis to identify distinct groups of colleges.

---