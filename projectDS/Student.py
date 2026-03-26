import pandas
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pandas.read_csv('student.csv')

head = df.head(19)
head.to_csv('head.csv',index=False)

summry = df.describe()
summry.to_csv('summary.csv',index=False)

info = df.info()

print(df.isnull().sum())
df = df.dropna()

print("sum of duplicate value",df.duplicated().sum())
print("the average study hours of students",round(df["StudyHours"].mean()))

print("the average marks score",round(df["Marks"].mean()))

m = df['Marks'].idxmax()
print("highest marks student: ",df.loc[m,['StudentName','Marks']])

a = df['Attendance(%)'].idxmin()
print("lowest attendance student: ",df.loc[a,['StudentName','Attendance(%)']])

val = ["Age", "StudyHours", "Attendance(%)", "Marks"]

# scaler = StandardScaler()
# df[val] = scaler.fit_transform(df[val])
df.to_csv('cleandata.csv',index=False)

corr = df["StudyHours"].corr(df["Marks"])
print("Correlation:", corr)

corr = df["Attendance(%)"].corr(df["Marks"])
print("Correlation:", corr)

cleancsv = pandas.read_csv('cleandata.csv')

sb.barplot(x=cleancsv.index, y="StudyHours", data=cleancsv)
plt.title("Study Hours of Students")
plt.xlabel("Student Index")
plt.show()

sb.histplot(cleancsv["Marks"])
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
 
sb.scatterplot(x="StudyHours", y="Marks", data=cleancsv)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

top5 = cleancsv.sort_values(by="Marks", ascending=False).head(5)
print("Top 5 Students with Highest Marks:\n")
print(top5[["StudentName", "Marks", "StudyHours", "Attendance(%)"]])