import matplotlib.pyplot as plot
import pandas, os

MY_PATH = os.path.abspath(__file__)

# version = int(input("Which version you wanna try(You can see them in 'datasets' folder)?  "))
version = 1

DATASET_PATH = os.path.join(MY_PATH, "..", "..", "..", "datasets", f"v{version}", "health_monitoring.csv")
DATASET_PATH = os.path.abspath(DATASET_PATH)

dataset = pandas.read_csv(DATASET_PATH)

columns = dataset.select_dtypes(include=['number']).columns

non_numeric_columns = dataset.select_dtypes(exclude=['number']).columns
print("*** NON NUMERIC COLUMNS: ")
for col in non_numeric_columns:
    print(f"* {col}")


for col in columns:
    data = dataset[col].dropna()

    Q1, Q3 = data.quantile(0.25), data.quantile(0.75)
    IQR = Q3 - Q1

    lower, upper = (Q1 - (1.5 * IQR)), (Q3 + (1.5 * IQR))

    lower_outlier, upper_outlier = data[data < lower], data[data > upper]

    outliers = pandas.concat([lower_outlier, upper_outlier], axis=0) # تلفیق دو طرف داده های پرت

    print(f"** Number of outliers in {col} found: {len(outliers)}")


# باکس پلات
plot.figure(figsize=(5.5,6.8))
plot.boxplot([dataset[col] for col in columns])  # برای هر ستون یه باکس پلات
plot.title(f"BoxPlot")
plot.ylabel('Values')
plot.xticks(range(1, len(columns)+1), columns, rotation=90)
plot.grid(True)
plot.show()