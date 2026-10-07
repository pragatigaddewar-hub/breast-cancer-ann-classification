## Data Collection
import pandas as pd
df = pd.read_csv("data.csv")

## Data Understanding

print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)
df.info()

## Data Cleaning

# 1. Check Missing Values

print("Missing Value :" ,df.isnull().sum())

df = df.drop(columns=['Unnamed: 32'])

print(df.columns)

## Check Duplicate Values

print("Duplicate Values :" ,df.duplicated().sum())

num_cols = df.select_dtypes('number').columns
print(num_cols)

## Outliers

# 1.radius_mean
Q1 = df['radius_mean'].quantile(0.25)
Q3 = df['radius_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['radius_mean'] < lower_limit) | (df['radius_mean'] > upper_limit))
print("Outliers radius_mean :" ,outliers.sum())

# 2.texture_mean
Q1 = df['texture_mean'].quantile(0.25)
Q3 = df['texture_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['texture_mean'] < lower_limit) | (df['texture_mean'] > upper_limit))
print("Outliers texture_mean :" ,outliers.sum())

# 3.perimeter_mean
Q1 = df['perimeter_mean'].quantile(0.25)
Q3 = df['perimeter_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['perimeter_mean'] < lower_limit) | (df['perimeter_mean'] > upper_limit))
print("Outliers perimeter_mean :" ,outliers.sum())


# 4.area_mean
Q1 = df['area_mean'].quantile(0.25)
Q3 = df['area_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['area_mean'] < lower_limit) | (df['area_mean'] > upper_limit))
print("Outliers area_mean :" ,outliers.sum())


# 5.smoothness_mean
Q1 = df['smoothness_mean'].quantile(0.25)
Q3 = df['smoothness_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['smoothness_mean'] < lower_limit) | (df['smoothness_mean'] > upper_limit))
print("Outliers smoothness_mean :" ,outliers.sum())


# 6.compactness_mean
Q1 = df['compactness_mean'].quantile(0.25)
Q3 = df['compactness_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['compactness_mean'] < lower_limit) | (df['compactness_mean'] > upper_limit))
print("Outliers compactness_mean :" ,outliers.sum())


# 7.concavity_mean
Q1 = df['concavity_mean'].quantile(0.25)
Q3 = df['concavity_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concavity_mean'] < lower_limit) | (df['concavity_mean'] > upper_limit))
print("Outliers concavity_mean :" ,outliers.sum())


# 8.concave points_mean
Q1 = df['concave points_mean'].quantile(0.25)
Q3 = df['concave points_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concave points_mean'] < lower_limit) | (df['concave points_mean'] > upper_limit))
print("Outliers concave points_mean :" ,outliers.sum())


# 9.symmetry_mean
Q1 = df['symmetry_mean'].quantile(0.25)
Q3 = df['symmetry_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['symmetry_mean'] < lower_limit) | (df['symmetry_mean'] > upper_limit))
print("Outliers symmetry_mean :" ,outliers.sum())


# 10.fractal_dimension_mean
Q1 = df['fractal_dimension_mean'].quantile(0.25)
Q3 = df['fractal_dimension_mean'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['fractal_dimension_mean'] < lower_limit) | (df['fractal_dimension_mean'] > upper_limit))
print("Outliers fractal_dimension_mean :" ,outliers.sum())


# 11.radius_se
Q1 = df['radius_se'].quantile(0.25)
Q3 = df['radius_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['radius_se'] < lower_limit) | (df['radius_se'] > upper_limit))
print("Outliers radius_se :" ,outliers.sum())


# 12.texture_se
Q1 = df['texture_se'].quantile(0.25)
Q3 = df['texture_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['texture_se'] < lower_limit) | (df['texture_se'] > upper_limit))
print("Outliers texture_se :" ,outliers.sum())


# 13.perimeter_se
Q1 = df['perimeter_se'].quantile(0.25)
Q3 = df['perimeter_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['perimeter_se'] < lower_limit) | (df['perimeter_se'] > upper_limit))
print("Outliers perimeter_se :" ,outliers.sum())


# 14.area_se
Q1 = df['area_se'].quantile(0.25)
Q3 = df['area_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['area_se'] < lower_limit) | (df['area_se'] > upper_limit))
print("Outliers area_se :" ,outliers.sum())


# 15.smoothness_se
Q1 = df['smoothness_se'].quantile(0.25)
Q3 = df['smoothness_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['smoothness_se'] < lower_limit) | (df['smoothness_se'] > upper_limit))
print("Outliers smoothness_se :" ,outliers.sum())


# 16.compactness_se
Q1 = df['compactness_se'].quantile(0.25)
Q3 = df['compactness_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['compactness_se'] < lower_limit) | (df['compactness_se'] > upper_limit))
print("Outliers compactness_se:" ,outliers.sum())


# 17.concavity_se
Q1 = df['concavity_se'].quantile(0.25)
Q3 = df['concavity_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concavity_se'] < lower_limit) | (df['concavity_se'] > upper_limit))
print("Outliers concavity_se:" ,outliers.sum())


# 18.concave points_se
Q1 = df['concave points_se'].quantile(0.25)
Q3 = df['concave points_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concave points_se'] < lower_limit) | (df['concave points_se'] > upper_limit))
print("Outliers concave points_se:" ,outliers.sum())


# 19.symmetry_se
Q1 = df['symmetry_se'].quantile(0.25)
Q3 = df['symmetry_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['symmetry_se'] < lower_limit) | (df['symmetry_se'] > upper_limit))
print("Outliers symmetry_se:" ,outliers.sum())


# 20.fractal_dimension_se
Q1 = df['fractal_dimension_se'].quantile(0.25)
Q3 = df['fractal_dimension_se'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['fractal_dimension_se'] < lower_limit) | (df['fractal_dimension_se'] > upper_limit))
print("Outliers fractal_dimension_se:" ,outliers.sum())



# 21.radius_worst
Q1 = df['radius_worst'].quantile(0.25)
Q3 = df['radius_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['radius_worst'] < lower_limit) | (df['radius_worst'] > upper_limit))
print("Outliers radius_worst:" ,outliers.sum())


# 22.texture_worst
Q1 = df['texture_worst'].quantile(0.25)
Q3 = df['texture_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['texture_worst'] < lower_limit) | (df['texture_worst'] > upper_limit))
print("Outliers texture_worst:" ,outliers.sum())


# 23.perimeter_worst
Q1 = df['perimeter_worst'].quantile(0.25)
Q3 = df['perimeter_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['perimeter_worst'] < lower_limit) | (df['perimeter_worst'] > upper_limit))
print("Outliers perimeter_worst:" ,outliers.sum())


# 24.area_worst
Q1 = df['area_worst'].quantile(0.25)
Q3 = df['area_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['area_worst'] < lower_limit) | (df['area_worst'] > upper_limit))
print("Outliers area_worst:" ,outliers.sum())

# 25.smoothness_worst
Q1 = df['smoothness_worst'].quantile(0.25)
Q3 = df['smoothness_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['smoothness_worst'] < lower_limit) | (df['smoothness_worst'] > upper_limit))
print("Outliers smoothness_worst:" ,outliers.sum())

# 26.compactness_worst
Q1 = df['compactness_worst'].quantile(0.25)
Q3 = df['compactness_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['compactness_worst'] < lower_limit) | (df['compactness_worst'] > upper_limit))
print("Outliers compactness_worst:" ,outliers.sum())


# 27.concavity_worst
Q1 = df['concavity_worst'].quantile(0.25)
Q3 = df['concavity_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concavity_worst'] < lower_limit) | (df['concavity_worst'] > upper_limit))
print("Outliers concavity_worst:" ,outliers.sum())



# 28.concave points_worst
Q1 = df['concave points_worst'].quantile(0.25)
Q3 = df['concave points_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['concave points_worst'] < lower_limit) | (df['concave points_worst'] > upper_limit))
print("Outliers concave points_worst:" ,outliers.sum())


# 29.symmetry_worst
Q1 = df['symmetry_worst'].quantile(0.25)
Q3 = df['symmetry_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['symmetry_worst'] < lower_limit) | (df['symmetry_worst'] > upper_limit))
print("Outliers symmetry_worst:" ,outliers.sum())


# 30.fractal_dimension_worst
Q1 = df['fractal_dimension_worst'].quantile(0.25)
Q3 = df['fractal_dimension_worst'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = ((df['fractal_dimension_worst'] < lower_limit) | (df['fractal_dimension_worst'] > upper_limit))
print("Outliers fractal_dimension_worst:" ,outliers.sum())



## Check Incorrect/Invalid Values

# Numerical Columns

print("Radius Mean Min :" ,df['radius_mean'].min())
print("Radius Mean Max :" ,df['radius_mean'].max())

print("Texture Mean Min :" ,df['texture_mean'].min())
print("Texture Mean Max :" ,df['texture_mean'].max())

print("Perimeter Mean Min :" ,df['perimeter_mean'].min())
print("Perimeter Mean Max :" ,df['perimeter_mean'].max())

print("Area Mean Min :" ,df['area_mean'].min())
print("Area Mean Max :" ,df['area_mean'].max())

print("Smoothness Mean Min :" ,df['smoothness_mean'].min())
print("Smoothness Mean Max :" ,df['smoothness_mean'].max())

print("Compactness Mean Min :" ,df['compactness_mean'].min())
print("Compactness Mean Max :" ,df['compactness_mean'].max())

print("Concavity Mean Min :" ,df['concavity_mean'].min())
print("Concavity Mean Max :" ,df['concavity_mean'].max())

print("Concave Points Mean Min :" ,df['concave points_mean'].min())
print("Concave Points Mean Max :" ,df['concave points_mean'].max())

print("symmetry Mean Min :" ,df['symmetry_mean'].min())
print("symmetry Mean Max :" ,df['symmetry_mean'].max())

print("Fractal Dimension Mean Min :" ,df['fractal_dimension_mean'].min())
print("Fractal Dimension Mean Max :" ,df['fractal_dimension_mean'].max())

print("Radius Se Min :" ,df['radius_se'].min())
print("Radius Se Max :" ,df['radius_se'].max())

print("Texture Se Min :" ,df['texture_se'].min())
print("Texture Se Max :" ,df['texture_se'].max())

print("Perimeter Se Min :" ,df['perimeter_se'].min())
print("Perimeter Se Max :" ,df['perimeter_se'].max())

print("Area Se Min :" ,df['area_se'].min())
print("Area Se Max :" ,df['area_se'].max())

print("Smoothness Se Min :" ,df['smoothness_se'].min())
print("Smoothness Se Max :" ,df['smoothness_se'].max())

print("Compactness Se Min :" ,df['compactness_se'].min())
print("Compactness Se Max :" ,df['compactness_se'].max())

print("Concavity Se Min :" ,df['concavity_se'].min())
print("Concavity Se Max :" ,df['concavity_se'].max())

print("Concave Points Se Min :" ,df['concave points_se'].min())
print("Concave Points Se Max :" ,df['concave points_se'].max())

print("symmetry Se Min :" ,df['symmetry_se'].min())
print("symmetry Se Max :" ,df['symmetry_se'].max())

print("Fractal Dimension Se Min :" ,df['fractal_dimension_se'].min())
print("Fractal Dimension Se Max :" ,df['fractal_dimension_se'].max())

print("Radius Worst Min :" ,df['radius_worst'].min())
print("Radius Worst Max :" ,df['radius_worst'].max())

print("Texture Worst Min :" ,df['texture_worst'].min())
print("Texture Worst Max :" ,df['texture_worst'].max())

print("Perimeter Worst Min :" ,df['perimeter_worst'].min())
print("Perimeter Worst Max :" ,df['perimeter_worst'].max())

print("Area Worst Min :" ,df['area_worst'].min())
print("Area Worst Max :" ,df['area_worst'].max())

print("Smoothness Worst Min :" ,df['smoothness_worst'].min())
print("Smoothness Worst Max :" ,df['smoothness_worst'].max())

print("Compactness Worst Min :" ,df['compactness_worst'].min())
print("Compactness Worst Max :" ,df['compactness_worst'].max())

print("Concavity Worst Min :" ,df['concavity_worst'].min())
print("Concavity Worst Max :" ,df['concavity_worst'].max())

print("Concave Points Worst Min :" ,df['concave points_worst'].min())
print("Concave Points Worst Max :" ,df['concave points_worst'].max())

print("Symmetry Worst Min :" ,df['symmetry_worst'].min())
print("Symmetry Worst Max :" ,df['symmetry_worst'].max())

print("Fractal Dimension Worst Min :" ,df['fractal_dimension_worst'].min())
print("Fractal Dimension Worst Max :" ,df['fractal_dimension_worst'].max())


# Categorical (Target) Column
print("diagnosis")
print(df['diagnosis'].value_counts())


## EDA

# 1. Univariate Analysis
import matplotlib.pyplot as plt
# Numerical Columns

print("1.radius_mean")
plt.hist(df['radius_mean'])
plt.xlabel("Radius Mean")
plt.title("Distribution Of Radius Mean")
plt.show()


print("2.texture_mean")
plt.hist(df['texture_mean'])
plt.xlabel("Texture Mean")
plt.title("Distribution Of Texture Mean")
plt.show()


print("3.perimeter_mean")
plt.hist(df['perimeter_mean'])
plt.xlabel("Perimeter Mean")
plt.title("Distribution Of Perimeter Mean")
plt.show()


print("4.area_mean")
plt.hist(df['area_mean'])
plt.xlabel("Area Mean")
plt.title("Distribution Of Area Mean")
plt.show()


print("5.smoothness_mean")
plt.hist(df['smoothness_mean'])
plt.xlabel("Smoothness Mean")
plt.title("Distribution Of Smoothness Mean")
plt.show()


print("6.compactness_mean")
plt.hist(df['compactness_mean'])
plt.xlabel("Compactness Mean")
plt.title("Distribution Of Compactness Mean")
plt.show()


print("7.concavity_mean")
plt.hist(df['concavity_mean'])
plt.xlabel("Concavity Mean")
plt.title("Distribution Of Concavity Mean")
plt.show()



print("8.concave points_mean")
plt.hist(df['concave points_mean'])
plt.xlabel("Concave Points Mean")
plt.title("Distribution Of Concave Points Mean")
plt.show()


print("9.symmetry_mean")
plt.hist(df['symmetry_mean'])
plt.xlabel("Symmetry Mean")
plt.title("Distribution Of Symmetry Mean")
plt.show()


print("10.fractal_dimension_mean")
plt.hist(df['fractal_dimension_mean'])
plt.xlabel("Fractal Dimension Mean")
plt.title("Distribution Of Fractal Dimension Mean")
plt.show()


print("11.radius_se")
plt.hist(df['radius_se'])
plt.xlabel("Radius Se")
plt.title("Distribution Of Radius Se")
plt.show()


print("12.texture_se")
plt.hist(df['texture_se'])
plt.xlabel("Texture Se")
plt.title("Distribution Of Texture Se")
plt.show()

print("13.perimeter_se")
plt.hist(df['perimeter_se'])
plt.xlabel("Perimeter Se")
plt.title("Distribution Of Perimeter Se")
plt.show()


print("14.area_se")
plt.hist(df['area_se'])
plt.xlabel("Area Se")
plt.title("Distribution Of Area Se")
plt.show()


print("15.smoothness_se")
plt.hist(df['smoothness_se'])
plt.xlabel("Smoothness Se")
plt.title("Distribution Of Smoothness Se")
plt.show()


print("16.compactness_se")
plt.hist(df['compactness_se'])
plt.xlabel("Compactness Se")
plt.title("Distribution Of Compactness Se")
plt.show()


print("17.concavity_se")
plt.hist(df['concavity_se'])
plt.xlabel("Concavity Se")
plt.title("Distribution Of Concavity Se")
plt.show()


print("18.concave points_se")
plt.hist(df['concave points_se'])
plt.xlabel("Concave Points Se")
plt.title("Distribution Of Concave Points Se")
plt.show()


print("19.symmetry_se")
plt.hist(df['symmetry_se'])
plt.xlabel("Symmetry Se")
plt.title("Distribution Of Symmetry Se")
plt.show()



print("20.fractal_dimension_se")
plt.hist(df['fractal_dimension_se'])
plt.xlabel("Fractal Dimension Se")
plt.title("Distribution Of Fractal Dimension Se")
plt.show()



print("21.radius_worst")
plt.hist(df['radius_worst'])
plt.xlabel("Radius Worst")
plt.title("Distribution Of Radius Worst")
plt.show()


print("22.texture_worst")
plt.hist(df['texture_worst'])
plt.xlabel("Texture Worst")
plt.title("Distribution Of Texture Worst")
plt.show()



print("23.perimeter_worst")
plt.hist(df['perimeter_worst'])
plt.xlabel("Perimeter Worst")
plt.title("Distribution Of Perimeter Worst")
plt.show()


print("24.area_worst")
plt.hist(df['area_worst'])
plt.xlabel("Area Worst")
plt.title("Distribution Of Area Worst")
plt.show()


print("25.smoothness_worst")
plt.hist(df['smoothness_worst'])
plt.xlabel("Smoothness Worst")
plt.title("Distribution Of Smoothness Worst")
plt.show()


print("26.compactness_worst")
plt.hist(df['compactness_worst'])
plt.xlabel("Compactness Worst")
plt.title("Distribution Of Compactness Worst")
plt.show()


print("27.concavity_worst")
plt.hist(df['concavity_worst'])
plt.xlabel("Concavity Worst")
plt.title("Distribution Of Concavity Worst")
plt.show()


print("28.concave points_worst")
plt.hist(df['concave points_worst'])
plt.xlabel("Concave Points Worst")
plt.title("Distribution Of Concave Points Worst")
plt.show()



print("29.symmetry_worst")
plt.hist(df['symmetry_worst'])
plt.xlabel("Symmetry Worst")
plt.title("Distribution Of Symmetry Worst")
plt.show()


print("30.fractal_dimension_worst")
plt.hist(df['fractal_dimension_worst'])
plt.xlabel("Fractal Dimension Worst")
plt.title("Distribution Of Fractal Dimension Worst")
plt.show()


# Categorical (Target) Column
print("diagnosis")
plt.bar(df['diagnosis'].value_counts().index,df['diagnosis'].value_counts().values)
plt.xlabel("Diagnosis")
plt.title("Distribution Of Diagnosis")
plt.show()


# Bivariate Analysis
import seaborn as sns

print("Radius Mean VS Diagnosis")
sns.boxplot(data = df,x ='radius_mean',y = 'diagnosis')
plt.xlabel("Radius Mean")
plt.ylabel("Diagnosis")
plt.title("Radius Mean VS Diagnosis")
plt.show()


print("Texture Mean VS Diagnosis")
sns.boxplot(data = df,x ='texture_mean',y = 'diagnosis')
plt.xlabel("Texture Mean")
plt.ylabel("Diagnosis")
plt.title("Texture Mean VS Diagnosis")
plt.show()


print("Perimeter Mean VS Diagnosis")
sns.boxplot(data = df,x ='perimeter_mean',y = 'diagnosis')
plt.xlabel("Perimeter Mean")
plt.ylabel("Diagnosis")
plt.title("Perimeter Mean VS Diagnosis")
plt.show()


print("Area Mean VS Diagnosis")
sns.boxplot(data = df,x ='area_mean',y = 'diagnosis')
plt.xlabel("Area Mean")
plt.ylabel("Diagnosis")
plt.title("Area Mean VS Diagnosis")
plt.show()


print("Smoothness Mean VS Diagnosis")
sns.boxplot(data = df,x ='smoothness_mean',y = 'diagnosis')
plt.xlabel("Smoothness Mean")
plt.ylabel("Diagnosis")
plt.title("Smoothness Mean VS Diagnosis")
plt.show()


print("Compactness Mean VS Diagnosis")
sns.boxplot(data = df,x ='compactness_mean',y = 'diagnosis')
plt.xlabel("Compactness Mean")
plt.ylabel("Diagnosis")
plt.title("Compactness Mean VS Diagnosis")
plt.show()

print("Concavity Mean VS Diagnosis")
sns.boxplot(data = df,x ='concavity_mean',y = 'diagnosis')
plt.xlabel("Concavity Mean")
plt.ylabel("Diagnosis")
plt.title("Concavity Mean VS Diagnosis")
plt.show()


print("Concave Points Mean VS Diagnosis")
sns.boxplot(data = df,x ='concave points_mean',y = 'diagnosis')
plt.xlabel("Concave Points Mean")
plt.ylabel("Diagnosis")
plt.title("Concave Points Mean VS Diagnosis")
plt.show()

print("Symmetry Mean VS Diagnosis")
sns.boxplot(data = df,x ='symmetry_mean',y = 'diagnosis')
plt.xlabel("Symmetry Mean")
plt.ylabel("Diagnosis")
plt.title("Symmetry Mean VS Diagnosis")
plt.show()


print("Fractal Dimension Mean VS Diagnosis")
sns.boxplot(data = df,x ='fractal_dimension_mean',y = 'diagnosis')
plt.xlabel("Fractal Dimension Mean")
plt.ylabel("Diagnosis")
plt.title("Fractal Dimension Mean VS Diagnosis")
plt.show()

print("Radius Se VS Diagnosis")
sns.boxplot(data = df,x ='radius_se',y = 'diagnosis')
plt.xlabel("Radius Se")
plt.ylabel("Diagnosis")
plt.title("Radius Se VS Diagnosis")
plt.show()

print("Texture Se VS Diagnosis")
sns.boxplot(data = df,x ='texture_se',y = 'diagnosis')
plt.xlabel("Texture Se")
plt.ylabel("Diagnosis")
plt.title("Texture Se VS Diagnosis")
plt.show()


print("Perimeter Se VS Diagnosis")
sns.boxplot(data = df,x ='perimeter_se',y = 'diagnosis')
plt.xlabel("Perimeter Se")
plt.ylabel("Diagnosis")
plt.title("Perimeter Se VS Diagnosis")
plt.show()


print("Area Se VS Diagnosis")
sns.boxplot(data = df,x ='area_se',y = 'diagnosis')
plt.xlabel("Area Se")
plt.ylabel("Diagnosis")
plt.title("Area Se VS Diagnosis")
plt.show()


print("Smoothness Se VS Diagnosis")
sns.boxplot(data = df,x ='smoothness_se',y = 'diagnosis')
plt.xlabel("Smoothness Se")
plt.ylabel("Diagnosis")
plt.title("Smoothness Se VS Diagnosis")
plt.show()


print("Compactness Se VS Diagnosis")
sns.boxplot(data = df,x ='compactness_se',y = 'diagnosis')
plt.xlabel("Compactness Se")
plt.ylabel("Diagnosis")
plt.title("Compactness Se VS Diagnosis")
plt.show()


print("Concavity Se VS Diagnosis")
sns.boxplot(data = df,x ='concavity_se',y = 'diagnosis')
plt.xlabel("Concavity Se")
plt.ylabel("Diagnosis")
plt.title("Concavity Se VS Diagnosis")
plt.show()


print("Concave Points Se VS Diagnosis")
sns.boxplot(data = df,x ='concave points_se',y = 'diagnosis')
plt.xlabel("Concave Points Se")
plt.ylabel("Diagnosis")
plt.title("Concave Points Se VS Diagnosis")
plt.show()


print("Symmetry Se VS Diagnosis")
sns.boxplot(data = df,x ='symmetry_se',y = 'diagnosis')
plt.xlabel("Symmetry Se")
plt.ylabel("Diagnosis")
plt.title("Symmetry Se VS Diagnosis")
plt.show()


print("Fractal Dimension Se VS Diagnosis")
sns.boxplot(data = df,x ='fractal_dimension_se',y = 'diagnosis')
plt.xlabel("Fractal Dimension Se")
plt.ylabel("Diagnosis")
plt.title("Fractal Dimension Se VS Diagnosis")
plt.show()


print("Radius Worst  VS Diagnosis")
sns.boxplot(data = df,x ='radius_worst',y = 'diagnosis')
plt.xlabel("Radius Worst ")
plt.ylabel("Diagnosis")
plt.title("Radius Worst  VS Diagnosis")
plt.show()


print("Texture Worst  VS Diagnosis")
sns.boxplot(data = df,x ='texture_worst',y = 'diagnosis')
plt.xlabel("Texture Worst ")
plt.ylabel("Diagnosis")
plt.title("Texture Worst  VS Diagnosis")
plt.show()

print("Perimeter Worst  VS Diagnosis")
sns.boxplot(data = df,x ='perimeter_worst',y = 'diagnosis')
plt.xlabel("Perimeter Worst ")
plt.ylabel("Diagnosis")
plt.title("Perimeter Worst  VS Diagnosis")
plt.show()


print("Area Worst  VS Diagnosis")
sns.boxplot(data = df,x ='area_worst',y = 'diagnosis')
plt.xlabel("Area Worst ")
plt.ylabel("Diagnosis")
plt.title("Area Worst  VS Diagnosis")
plt.show()


print("Smoothness Worst  VS Diagnosis")
sns.boxplot(data = df,x ='smoothness_worst',y = 'diagnosis')
plt.xlabel("Smoothness Worst ")
plt.ylabel("Diagnosis")
plt.title("Smoothness Worst  VS Diagnosis")
plt.show()


print("Compactness Worst  VS Diagnosis")
sns.boxplot(data = df,x ='compactness_worst',y = 'diagnosis')
plt.xlabel("Compactness Worst ")
plt.ylabel("Diagnosis")
plt.title("Compactness Worst  VS Diagnosis")
plt.show()


print("Concavity Worst  VS Diagnosis")
sns.boxplot(data = df,x ='concavity_worst',y = 'diagnosis')
plt.xlabel("Concavity Worst ")
plt.ylabel("Diagnosis")
plt.title("Concavity Worst  VS Diagnosis")
plt.show()


print("Concave Points Worst  VS Diagnosis")
sns.boxplot(data = df,x ='concave points_worst',y = 'diagnosis')
plt.xlabel("Concave Points Worst ")
plt.ylabel("Diagnosis")
plt.title("Concave Points Worst  VS Diagnosis")
plt.show()

print("Symmetry Worst  VS Diagnosis")
sns.boxplot(data = df,x ='symmetry_worst',y = 'diagnosis')
plt.xlabel("Symmetry Worst ")
plt.ylabel("Diagnosis")
plt.title("Symmetry Worst  VS Diagnosis")
plt.show()


print("Fractal Dimension Worst  VS Diagnosis")
sns.boxplot(data = df,x ='fractal_dimension_worst',y = 'diagnosis')
plt.xlabel("Fractal Dimension Worst ")
plt.ylabel("Diagnosis")
plt.title("Fractal Dimension Worst  VS Diagnosis")
plt.show()


# Multivariate Analysis

num_cols = df.select_dtypes(include='number').columns
print("Correlation :",df[num_cols].corr())


sns.heatmap(df[num_cols].corr(),annot=True)
plt.show()


## Feature Selection

df = df.drop(columns='id')
print(df.columns)


## Data Processing
# 1. Encoding

one_hot = pd.get_dummies(df[['diagnosis']])
print(one_hot)

X = df.drop(columns='diagnosis')
y = one_hot

print(X.shape)
print(y.shape)

# 2. Train Test Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

## Feature Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled.shape)
print(X_test_scaled.shape)

## Model Building
# ANN
import tensorflow as tf
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

# Input Layer
model.add(Input(shape=(30,)))

# Hidden Layer
model.add(Dense(16,activation='relu'))

# Output Layer
model.add(Dense(2,activation='softmax'))

# Model Summary
model.summary()

## Model Compilation
model.compile(
    optimizer = 'adam' ,
    loss = 'categorical_crossentropy' ,
    metrics = ['accuracy']
)

## Model Training
history = model.fit(X_train_scaled,
                    y_train,
                    epochs=20,
                    validation_split= 0.2)

## Model Evaluation
test_loss , test_accuracy = model.evaluate(X_test_scaled,y_test)

print("Test Loss :" ,test_loss)
print("Test Accuracy :" ,test_accuracy)


## Prediction
y_pred = model.predict(X_test_scaled)

## Convert prediction into Class
y_pred_class = y_pred.argmax(axis=1)
print("Predicted Class :" ,y_pred_class)

## Convert Actual Values into Class

y_test_class = y_test.values.argmax(axis=1)
print("Actual Class :" ,y_test_class)


# Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test_class,y_pred_class)
print("Confusion Matrix :" ,cm)

# Classification Report
from sklearn.metrics import classification_report

cr = classification_report(y_test_class,y_pred_class)
print("Classification Report :" ,cr)

## Check Overfitting
print("Metrics :" ,history.history.keys())

print("Training Accuracy :" ,history.history['accuracy'][-1])
print("Validation Accuracy  :" ,history.history['val_accuracy'][-1])
print("Training Loss :" ,history.history['loss'][-1])
print("Validation Loss  :" ,history.history['val_loss'][-1])


## Final Model Result

print("Test Accuracy :" ,test_accuracy)

print("Final Model Result - Test Accuracy :" ,test_accuracy*100,"%")