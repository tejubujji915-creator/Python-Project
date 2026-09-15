# ============================================================
# AGRICULTURE CROP PRODUCTION AND PREDICTION
# ============================================================

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# 1. AGRICULTURAL DATASET
# ============================================================

data = {
    "Area": [10, 15, 20, 25, 30,
             35, 40, 45, 50, 55,
             60, 65, 70, 75, 80],

    "Rainfall": [500, 550, 600, 650, 700,
                 750, 800, 850, 900, 950,
                 1000, 1050, 1100, 1150, 1200],

    "Fertilizer": [100, 120, 150, 170, 200,
                   220, 250, 270, 300, 320,
                   350, 370, 400, 420, 450],

    "Pesticide": [20, 25, 30, 35, 40,
                  45, 50, 55, 60, 65,
                  70, 75, 80, 85, 90],

    "Production": [25, 35, 48, 60, 75,
                   90, 105, 120, 135, 150,
                   165, 180, 195, 210, 225]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# ============================================================
# 2. DATA ANALYSIS
# ============================================================

print("\nAGRICULTURE DATASET")
print(df)

print("\nDATASET INFORMATION")
df.info()   # fixed: removed print()

print("\nSTATISTICAL ANALYSIS")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

# ============================================================
# 3. DATA PREPROCESSING
# ============================================================

df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))

# ============================================================
# 4. FEATURE SELECTION
# ============================================================

X = df[["Area", "Rainfall", "Fertilizer", "Pesticide"]]
y = df["Production"]

# ============================================================
# 5. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================================================
# 6. MACHINE LEARNING MODEL
# ============================================================

model = LinearRegression()
model.fit(X_train, y_train)

# ============================================================
# 7. MODEL PERFORMANCE
# ============================================================

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMODEL PERFORMANCE")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# ============================================================
# 8. CROP PRODUCTION PREDICTION FUNCTION
# ============================================================

def predict_production():
    try:
        # Validate inputs
        if not all([area_entry.get(), rainfall_entry.get(),
                    fertilizer_entry.get(), pesticide_entry.get()]):
            messagebox.showerror("Input Error", "All fields must be filled!")
            return

        area = float(area_entry.get())
        rainfall = float(rainfall_entry.get())
        fertilizer = float(fertilizer_entry.get())
        pesticide = float(pesticide_entry.get())

        input_data = pd.DataFrame(
            [[area, rainfall, fertilizer, pesticide]],
            columns=["Area", "Rainfall", "Fertilizer", "Pesticide"]
        )

        prediction = model.predict(input_data)

        result_label.config(
            text=f"Predicted Crop Production:\n{round(prediction[0], 2)} Tons"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")

# ============================================================
# 9. CLEAR FUNCTION
# ============================================================

def clear_data():
    area_entry.delete(0, tk.END)
    rainfall_entry.delete(0, tk.END)
    fertilizer_entry.delete(0, tk.END)
    pesticide_entry.delete(0, tk.END)
    result_label.config(text="")

# ============================================================
# 10. TKINTER GUI INTERFACE
# ============================================================

root = tk.Tk()
root.title("Agriculture Crop Production and Prediction")
root.geometry("600x600")
root.resizable(False, False)

# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="🌾 AGRICULTURE CROP PRODUCTION\nAND PREDICTION 🌾",
    font=("Arial", 18, "bold"),
    pady=20
)
title.pack()

# ============================================================
# AREA
# ============================================================

tk.Label(root, text="Enter Agricultural Area (Hectares)", font=("Arial", 12)).pack()
area_entry = tk.Entry(root, font=("Arial", 12), width=30)
area_entry.pack(pady=5)

# ============================================================
# RAINFALL
# ============================================================

tk.Label(root, text="Enter Rainfall (mm)", font=("Arial", 12)).pack()
rainfall_entry = tk.Entry(root, font=("Arial", 12), width=30)
rainfall_entry.pack(pady=5)

# ============================================================
# FERTILIZER
# ============================================================

tk.Label(root, text="Enter Fertilizer Used (kg)", font=("Arial", 12)).pack()
fertilizer_entry = tk.Entry(root, font=("Arial", 12), width=30)
fertilizer_entry.pack(pady=5)

# ============================================================
# PESTICIDE
# ============================================================

tk.Label(root, text="Enter Pesticide Used (kg)", font=("Arial", 12)).pack()
pesticide_entry = tk.Entry(root, font=("Arial", 12), width=30)
pesticide_entry.pack(pady=5)

# ============================================================
# PREDICT BUTTON
# ============================================================

predict_button = tk.Button(
    root,
    text="PREDICT CROP PRODUCTION",
    font=("Arial", 12, "bold"),
    command=predict_production,
    width=28,
    height=2
)
predict_button.pack(pady=20)

# ============================================================
# CLEAR BUTTON
# ============================================================

clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 11),
    command=clear_data,
    width=15
)
clear_button.pack()

# ============================================================
# RESULT LABEL
# ============================================================

result_label = tk.Label(root, text="", font=("Arial", 15, "bold"), pady=30)
result_label.pack()

# ============================================================
# RUN APPLICATION
# ============================================================

# Bind Enter key to prediction
root.bind('<Return>', lambda event: predict_production())

root.mainloop()
