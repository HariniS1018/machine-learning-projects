#### **OVERALL SUMMARY:**

* All attributes have 777 entries, indicating **no missing values** for any of the numerical features.
* Also, Attribute `Grad.Rate` has maximum value of 118 typically says that there is obvious **data errors** since graduation rate cannot exceed 100%
----

**Identifying Presence Of Potential Outliers:**

From observation of statistical data, we Suspect the presence of outliers in the following attributes = **['Apps', 'Accept', 'Enroll', 'F.Undergrad', 'P.Undergrad', 'Outstate', 'Expend']**. So, Steps have taken and confirmed the **presence of Outliers** by observing the following results.
* Coefficient of Variation **(COV)** of every attribute in the above list is higher, **Mean > Median > Mode** for every attribute of the list and further Skewness Coefficient for every attribute further shows their values are higher than 0.5. So, these attributes have potential outliers and **right-Skewed**. Meaning a few large institutions receive a disproportionately high number.
* Visualizations prove that the `Expend` attribute also has potential outliers
* Visualizations (univariate analysis) on `Top10perc`, `Room.Board`, `Books`, `Personal`, `PhD`, `Terminal`, `S.F.Ratio`, and `perc.alumni` has shown potential outliers beyond statistical checks.
* This suggest that careful consideration of data transformation (e.g., log scaling) will be essential during preprocessing to manage their potential impact on ML model performance and to normalize feature distributions.
----

**Finding Relationship between Variables**

So, From the above correlation coefficient Heatmap, we can infer that,
* As attribute `Apps` increases `Accept` also increases => Which means, colleges receiving more applications tend to accept a greater number of students.
* Similarly,
    - `Accept` increases -> `Enroll` will also increase
    - `Apps`, or `Accept` or 'Enroll` increases -> `F.Undergrad` will also increase => No. of Full-time Undergraduates increases because they are enrolling more. larger institutions, characterized by higher application and acceptance volumes, generally have a greater number of full-time undergraduate students
    - `PhD` increases -> `Terminal` increases -> Faculties with Terminal degree are growing as lot of students studies PhD increases.
    - `S.F.Ration` decreases -> `Expend` increases -> As the student-to-faculty ratio decreases (meaning more faculty per student, or smaller class sizes), the instructional expenditure per student tends to increase.

Even with a strong correlation, correlation does not imply causation. Just because two variables move together doesn't mean one causes the other. There might be a third, unobserved factor, or the relationship might just be coincidental. Further analysis is needed to find the relationships.