# 📊 Student Performance Data Analysis Project

## 📌 Project Overview

This project performs **data analysis and visualization** on a student performance dataset using Python.
The goal is to clean the dataset, analyze student behavior, identify performance patterns, and generate meaningful visual insights.

The project uses data science libraries to perform preprocessing, statistical analysis, and visualization.


## 🗂 Dataset Features

The dataset contains information about students:

* **StudentName** — Name of the student
* **Age** — Age of student
* **StudyHours** — Daily study hours
* **Attendance(%)** — Attendance percentage
* **Marks** — Marks obtained in exams


## ⚙️ Data Preprocessing Steps

The following preprocessing steps were performed:

1. Displayed first 19 rows of the dataset
2. Generated summary statistics
3. Checked dataset information and data types
4. Identified and removed missing values
5. Checked and counted duplicate records
6. Calculated average study hours and average marks
7. Identified student with highest marks
8. Identified student with lowest attendance
9. Saved cleaned dataset into a new CSV file


## 📈 Statistical Analysis

The project calculates:

* Average study hours of students
* Average marks scored
* Student with highest marks
* Student with lowest attendance
* Correlation between:

  * Study Hours and Marks
  * Attendance and Marks


## 📊 Data Visualizations

The following visualizations were created using Seaborn and Matplotlib:

1. **Bar Chart** — Study hours of students
2. **Histogram** — Distribution of marks
3. **Scatter Plot** — Study hours vs marks

These visualizations help in understanding performance patterns and student behavior.


## 🏆 Top Performers Analysis

The project identifies the **Top 5 students** with highest marks and displays:

* Student Name
* Marks
* Study Hours
* Attendance Percentage


## 🔍 Key Insights

1. Students who spend more time studying tend to score higher marks, showing a strong positive relationship between effort and performance. Consistent study habits greatly improve academic results.

2. Attendance has a positive impact on student performance, as students attending classes regularly generally achieve better marks. Classroom participation supports better understanding of subjects.

3. Most students score within the average marks range, while only a few students achieve extremely high or very low scores. This indicates a balanced academic performance across the dataset.

4. The highest-performing students usually maintain both high study hours and strong attendance. This shows that discipline and consistency are major factors behind academic success.

5. Only a small number of students fall into the low-performance category, suggesting effective teaching methods and good overall student engagement in studies.


## 💻 Technologies Used

* Python
* Pandas
* Seaborn
* Matplotlib
* Scikit-learn

---

## 📁 Output Files Generated

* **head.csv** → First 19 rows of dataset
* **summary.csv** → Statistical summary
* **cleandata.csv** → Cleaned dataset after preprocessing

---

## 🚀 Conclusion

This project demonstrates how data preprocessing, statistical analysis, and visualization techniques can be used to extract meaningful insights from student performance data. It helps in identifying academic patterns and factors that influence student success.

---

✍️ *Created as a Data Science practice project*
