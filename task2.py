import pandas as pd
from fpdf import FPDF

# Step 1: Read data from CSV file
df = pd.read_csv("data.csv")

# Step 2: Analyze the data
total_students = len(df)
average_age = df["Age"].mean()
average_marks = df["Marks"].mean()
topper = df.loc[df["Marks"].idxmax()]["Name"]
lowest = df.loc[df["Marks"].idxmin()]["Name"]

# Step 3: Create PDF using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(0, 10, f"Average Age: {average_age:.2f}", ln=True)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(0, 10, f"Top Scorer: {topper}", ln=True)
pdf.cell(0, 10, f"Lowest Scorer: {lowest}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Detailed Student List:", ln=True)

# Table Header
pdf.set_font("Arial", "B", 12)
pdf.cell(60, 10, "Name", 1)
pdf.cell(30, 10, "Age", 1)
pdf.cell(30, 10, "Marks", 1)
pdf.ln()

# Table Data
pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(60, 10, row["Name"], 1)
    pdf.cell(30, 10, str(row["Age"]), 1)
    pdf.cell(30, 10, str(row["Marks"]), 1)
    pdf.ln()

# Step 4: Save the PDF
pdf.output("student_report.pdf")

print("✅ Report generated as student_report.pdf")
