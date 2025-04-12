import pandas, os
import tkinter as tk
from tkinter import ttk

MY_PATH = os.path.abspath(__file__)

DATASET_PATH = os.path.join(MY_PATH, "..", "..", "..", "datasets", "v1", "health_monitoring.csv")
DATASET_PATH = os.path.abspath(DATASET_PATH)

dataset = pandas.read_csv(DATASET_PATH)

columns = dataset.select_dtypes(include=['number']).columns

for i in range(len(columns)):
    print(f"{i+1}. {columns[i]}")

column_index = int(input("Type the number of each one you wanna see the similarity matrix: "))
column_name = columns[column_index-1]
users = int(input("Type how many users you wanna try? "))
users+=1

# فاصله اقلیدسی
def calculate_similarity(user1, user2):
    return 1 / (1 + abs(float(user1) - float(user2)))


# ساخت ماتریس خالی
similarity_matrix = []
for i in range(users):
    similarity_matrix.append([0] * users)


for i in range(users):
    for j in range(i + 1, users):
        similarity = calculate_similarity(dataset.iloc[i][column_name], dataset.iloc[j][column_name])
        similarity_matrix[i][j] = ""          # بالا مثلثی
        similarity_matrix[j][i] = similarity  # پایین مثلثی


#################################################################################################################################


root = tk.Tk()
root.title(f"Similarity matrix of {column_name}")


frame = tk.Frame(root)
frame.pack(fill="both", expand=True)  # گرفتن کل صفحه

# اسکرول عمودی
v_scroll = tk.Scrollbar(frame, orient="vertical")

# اسکرول افقی
h_scroll = tk.Scrollbar(frame, orient="horizontal")

# ساخت جدول 
treeview = ttk.Treeview(frame, columns=[str(i) for i in range(users)], show="headings", height=users)

# افزودن اسکرول‌ها به جدول
treeview.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
v_scroll.config(command=treeview.yview)
h_scroll.config(command=treeview.xview)


for i in range(users):
    treeview.heading(i, text=str(i))  
    treeview.column(i, width=60, anchor="center")


users-=1

for i in range(users):
    row = [str(i + 1)]
    for j in range(users):
        num = similarity_matrix[i][j]
        if type(num) == str:
            row.append("")
        else:
            row.append(f"{num:.2f}")
    treeview.insert("", "end", values=row)

# اضافه کردن اسکرول به قاب
v_scroll.pack(side="right", fill="y")
h_scroll.pack(side="bottom", fill="x")

# پر کردن جدول تو پک
treeview.pack(fill="both", expand=True)


treeview.tag_configure('evenrow', background="#f0f0f0")
treeview.tag_configure('oddrow', background="#ffffff")

# تنظیم رنگ ها تو جدول
for row_index in range(users):
    if row_index % 2 == 0:
        tag = 'evenrow'
    else:
        tag = 'oddrow'
    treeview.item(treeview.get_children()[row_index], tags=tag)


root.update_idletasks()
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")  # پنجره اندازه ایی که باید تنظیم شه

root.mainloop()
