import pandas as pd
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Load data into memory
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'cleaned_data.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    df = pd.DataFrame() # Fallback

@app.route('/')
def index():
    if df.empty:
        return "Dataset not found. Please run the ETL pipeline first."
    
    departments = df['Department'].unique().tolist() if 'Department' in df.columns else []
    genders = df['Gender'].unique().tolist() if 'Gender' in df.columns else []
    experiences = df['Experience_Group'].dropna().unique().tolist() if 'Experience_Group' in df.columns else []
    
    return render_template('index.html', departments=departments, genders=genders, experiences=experiences)

@app.route('/api/data')
def get_data():
    if df.empty:
        return jsonify({"error": "No data available"})
        
    filtered_df = df.copy()
    
    # Apply filters
    dept = request.args.get('department')
    gender = request.args.get('gender')
    exp = request.args.get('experience')
    
    if dept and dept != 'All':
        filtered_df = filtered_df[filtered_df['Department'] == dept]
    if gender and gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == gender]
    if exp and exp != 'All':
        filtered_df = filtered_df[filtered_df['Experience_Group'] == exp]
        
    # Calculate KPIs
    total_employees = len(filtered_df)
    avg_salary = int(filtered_df['Salary'].mean()) if not filtered_df.empty else 0
    avg_bonus = int(filtered_df['Bonus'].mean()) if not filtered_df.empty else 0
    
    # Pay gap calculation within filtered view
    g_salary = filtered_df.groupby('Gender')['Salary'].mean()
    pay_gap = 0
    if 'Male' in g_salary and 'Female' in g_salary and g_salary['Male'] > 0:
        pay_gap = round(((g_salary['Male'] - g_salary['Female']) / g_salary['Male']) * 100, 2)
        
    kpis = {
        "total_employees": f"{total_employees:,}",
        "avg_salary": f"₹{avg_salary:,}",
        "avg_bonus": f"₹{avg_bonus:,}",
        "pay_gap": f"{pay_gap}%"
    }
    
    # Chart Data: Salary by Department
    dept_salary = filtered_df.groupby('Department')['Salary'].mean().round(0).to_dict()
    chart1 = {
        "labels": list(dept_salary.keys()),
        "data": list(dept_salary.values())
    }
    
    # Chart Data: Gender Distribution
    gender_dist = filtered_df['Gender'].value_counts().to_dict()
    chart2 = {
        "labels": list(gender_dist.keys()),
        "data": list(gender_dist.values())
    }
    
    return jsonify({
        "kpis": kpis,
        "chart1": chart1,
        "chart2": chart2
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
