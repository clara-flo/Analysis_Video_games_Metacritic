# -*- coding: utf-8 -*-
"""
Video Game Sales Analysis with Machine Learning

@author: Clara L. GARCIA

"""

#%% SETUP ENVIRONMENT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Configure display options
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
plt.style.use('seaborn')

#%% LOAD & INSPECT DATA
print("\n=== LOADING AND INSPECTING DATA ===")
df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# Initial data inspection
print("\nFirst 5 rows:")
print(df.head())
print("\nData types and missing values:")
print(df.info())
print("\nDescriptive statistics:")
print(df.describe())

#%% DATA CLEANING
print("\n=== CLEANING DATA ===")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Handle missing values
print("\nHandling missing values...")
df['year_of_release'] = pd.to_numeric(df['year_of_release'], errors='coerce')
df.dropna(subset=['year_of_release', 'genre', 'platform'], inplace=True)

# Fill missing scores
df['critic_score'] = df['critic_score'].fillna(df['critic_score'].mean())
df['user_score'] = df['user_score'].replace('tbd', np.nan)
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df['user_score'] = df['user_score'].fillna(df['user_score'].mean())

#%% FEATURE ENGINEERING
print("\n=== CREATING NEW FEATURES ===")

# Calculate total global sales
df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Create decade and age features
df['decade'] = (df['year_of_release'] // 10) * 10
current_year = 2017  # dataset limit
df['game_age'] = current_year - df['year_of_release']

# Create binary flags for reviews
df['has_critic_reviews'] = np.where(df['critic_score'].notna(), 1, 0)
df['has_user_reviews'] = np.where(df['user_score'].notna(), 1, 0)

#%% EXPLORATORY DATA ANALYSIS
print("\n=== EXPLORATORY ANALYSIS ===")

# 1. Dataset Overview
print("\n1. DATASET OVERVIEW")
num_games = df.shape[0]
year_min = int(df['year_of_release'].min())
year_max = int(df['year_of_release'].max())
print(f'Number of games: {num_games:,}')
print(f'Time period: {year_min}-{year_max} ({year_max-year_min} years)')

# Distribution analysis
print("\nGenre distribution:")
print(df['genre'].value_counts(normalize=True).mul(100).round(1))
print("\nTop platforms:")
print(df['platform'].value_counts().head(10))
print("\nTop publishers:")
print(df['publisher'].value_counts().head(10))

# 2. Sales Trends Over Time
print("\n2. SALES TRENDS OVER TIME")
plt.figure(figsize=(12, 6))
df.groupby('year_of_release')['total_sales'].sum().plot(title='Global Game Sales Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales (millions)')
plt.show()

# 3. Correlation Analysis
print("\n3. CORRELATION ANALYSIS")
corr_matrix = df[['total_sales', 'critic_score', 'user_score', 'year_of_release']].corr()
print("\nCorrelation matrix:")
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

#%% MACHINE LEARNING MODELING
print("\n=== BUILDING SALES PREDICTION MODEL ===")

# Feature selection
features = ['platform', 'genre', 'publisher', 'critic_score', 'user_score',
            'year_of_release', 'has_critic_reviews', 'has_user_reviews']
target = 'total_sales'

# Remove rows with missing target values
df_ml = df.dropna(subset=[target])

# Split data
X = df_ml[features]
y = df_ml[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
print("\nPreprocessing data...")
categorical_features = ['platform', 'genre', 'publisher']
numeric_features = ['critic_score', 'user_score', 'year_of_release',
                   'has_critic_reviews', 'has_user_reviews']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)])

# Build pipeline
print("\nBuilding Random Forest model...")
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"\nModel Performance:")
print(f"RMSE: {rmse:.2f}")
print(f"R-squared: {r2:.2f}")

# Feature Importance
print("\nCalculating feature importance...")
rf = model.named_steps['regressor']
feature_names = numeric_features + list(model.named_steps['preprocessor']
                         .named_transformers_['cat']
                         .get_feature_names_out(categorical_features))

importances = pd.Series(rf.feature_importances_, index=feature_names)
top_features = importances.sort_values(ascending=False).head(15)

# Sort and plot with a cleaner style
plt.figure(figsize=(10, 6))
top_features.sort_values().plot.barh(
    color='darkred', 
    edgecolor='black', 
    linewidth=1.2
)

# Titles and labels
plt.title('Top 15 Most Important Features for Sales Prediction', fontsize=16, weight='bold')
plt.xlabel('Importance Score', fontsize=15)
plt.ylabel('Feature', fontsize=15)

# Grid and style
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Remove frame lines except left & bottom
for spine in ['top', 'right']:
    plt.gca().spines[spine].set_visible(False)

plt.tight_layout()
plt.show()


print("\nAnalysis complete!")