import matplotlib.pyplot as plot
import pandas, os

MY_PATH = os.path.abspath(__file__)

# version = int(input("Which version you wanna try(You can see them in 'datasets' folder)?  "))
version = 1
DATASET_PATH = os.path.join(MY_PATH, "..", "..", "..", "datasets", f"v{version}", "health_monitoring.csv")
DATASET_PATH = os.path.abspath(DATASET_PATH)

dataset = pandas.read_csv(DATASET_PATH)

columns = dataset.select_dtypes(include=['number']).columns # فقط داده های نامریک

output = "*** Only Numeric options: \n"
for i in range(len(columns)):
    output += f"{i+1}. {columns[i]}\n"


column_index = int(input(f"{output}Type the number of each one you wanna see the histogram: "))

column = columns[column_index-1]

data = dataset[column].dropna()   # حذف داده هایی که مقدار ندارن

Q1, Q3 = data.quantile(0.25), data.quantile(0.75)
IQR = Q3 - Q1

lower, upper = (Q1 - (1.5 * IQR)), (Q3 + (1.5 * IQR))

lower_outlier, upper_outlier = data[data < lower], data[data > upper]

outliers = pandas.concat([lower_outlier, upper_outlier], axis=0) # تلفیق دو طرف داده های پرت


# هیستوگرام
plot.hist(data, bins=50)
plot.title(f"Histogram of {column}")
plot.xlabel(column)
plot.ylabel('Frequency')

plot.show()