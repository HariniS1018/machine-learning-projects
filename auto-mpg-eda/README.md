**This dataset is the *Auto MPG dataset* from the UCI Machine Learning Repository.** It contains technical specifications of cars manufactured in the 1970s–1980s and is commonly used for regression tasks, especially predicting fuel efficiency (miles per gallon, `mpg`).

---

### 📊 Dataset Overview
- **Target variable**:  
  - `mpg` → Miles per gallon (continuous, the fuel efficiency measure).
- **Features**:  
  - `cylinders` → Number of engine cylinders (discrete).  
  - `displacement` → Engine displacement in cubic inches (continuous).  
  - `horsepower` → Engine horsepower (continuous).  
  - `weight` → Vehicle weight in pounds (continuous).  
  - `acceleration` → Time to accelerate from 0–60 mph (continuous).  
  - `year` → Model year (discrete).  
  - `origin` → Country of origin (categorical: 1 = USA, 2 = Europe, 3 = Japan).  
  - `name` → Car model name (string, unique per instance).

---

### 📌 Key Facts
- **Number of samples**: 392 cars (after removing rows with missing values).  
- **Purpose**: Often used to build regression models predicting `mpg` from other car attributes.  
- **Source**: Originally published in the UCI Machine Learning Repository, widely used in ML tutorials and textbooks.  
- **Applications**:  
  - Regression (predicting mpg).  
  - Exploratory data analysis (relationships between weight, horsepower, and fuel efficiency).  
  - Feature engineering (categorical encoding of `origin`, text processing of `name`).

---