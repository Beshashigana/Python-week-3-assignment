import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

try:
    iris = load_iris()
    df = pd.dataframe(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nDataset info:")
    print

    print("\nMissing Values:")
    print(df.isnull().sum())

except FileNotFoundError as e:
    print(f"Error: {e}")

print("\nBasic Statistics:")
(df.describe())

grouped_data = df.groupby('species').mean()
print("\nMean by Species")
print(grouped_data)

print("\nObservations:")
print("1. Setosa species has the smallest average measurements in terms i fsepal and petal size.")
print("2. Versicolor and Virginica species show larger petal and sepal sizes.")

# Task 3: Data Visualization

# 1. Line Chart: Trend over time (Example: Count of species over some time)
# Here, we will simulate it by showing the distribution of species
species_count = df['species'].value_counts()

plt.figure(figsize=(10,6))
species_count.plot(kind='line', marker='o')
plt.title('Species Count Trend (Simulated Time-Series)')
plt.xlabel('Species')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# 2. Bar Chart: Average Petal Length by Species
plt.figure(figsize=(10,6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=0)
plt.show()

# 3. Histogram: Petal Length Distribution
plt.figure(figsize=(10,6))
df['petal length (cm)'].hist(bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(10,6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species', palette='Set1')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()


