import matplotlib.pyplot as plot
import pandas, matplotlib, os

MY_PATH = os.path.abspath(__file__)

version = int(input("Which version you wanna try(You can see them in 'datasets' folder)?  "))

# "../../datasets/v1/health_monitoring.csv"
DATASET_PATH = os.path.join(MY_PATH, "..", "..", "..", "datasets", f"v{version}", "health_monitoring.csv")
DATASET_PATH = os.path.abspath(DATASET_PATH)

dataset = pandas.read_csv(DATASET_PATH)

columns = dataset.columns

output = ""
for i in range(len(columns)):
    output += f"{i+1}. {columns[i]}\n"

column_index = int(input(f"{output}*** Type the number of each one you wanna see the outliers: "))

column = columns[column_index-1]

data = dataset[column].dropna()   # حذف داده هایی که مقدار ندارن

Q1, Q3 = data.quantile(0.25), data.quantile(0.75)
IQR = Q3 - Q1

lower, upper = (Q1 - (1.5 * IQR)), (Q3 + (1.5 * IQR))

lower_outlier, upper_outlier = data[data < lower], data[data > upper]

outliers = pandas.concat([lower_outlier, upper_outlier], axis=0) # تلفیق دو طرف داده های پرت

print(f"Number of outliers found: {len(outliers)}")


# باکس پلات
plot.boxplot(data)
plot.title(f"BoxPlot of {column}")
plot.ylabel(column)
plot.grid(True)
plot.show()