# Logistics Data Preprocessing – Week 2

**Intern:** Harshada Kishor Mahajan  
**Role:** Logistics Data Analyst Intern  
**Task:** Week 2 – Data Collection, Cleaning, and Preprocessing for Logistics Analysis

## Overview
This project demonstrates a logistics data preprocessing pipeline for future analytics and delivery-delay prediction.

## Dataset
The included CSV is a simulated shipment-level dataset containing dates, distance, vehicle type, route, shipment weight, delivery time, and transportation cost.

## Preprocessing
1. Load data using Pandas
2. Remove duplicates
3. Convert date columns
4. Handle missing values
5. Standardize categories
6. Calculate delivery delay
7. Detect outliers using IQR
8. Normalize numerical features using Min-Max Scaling
9. Export processed data

## Technologies
Python, Pandas, Scikit-learn

## Files
- README.md – documentation
- logistics_preprocessing.py – preprocessing code
- cleaned_logistics_data.csv – dataset

## Run
Install dependencies:
`pip install pandas scikit-learn`

Then run:
`python logistics_preprocessing.py`

The dataset is simulated for educational/internship purposes and contains no confidential personal information.
