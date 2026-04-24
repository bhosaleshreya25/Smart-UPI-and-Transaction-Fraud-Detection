import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import joblib
import os

print("=" * 60)
print("TRAINING ML MODELS")
print("=" * 60)

os.makedirs('data', exist_ok=True)

# Load dataset
df = pd.read_csv('data/upi_dataset.csv')
print(f"\nLoaded {len(df):,} records")

feature_cols = ['alpha_count', 'digit_count', 'special_count', 'total_length',
                'username_length', 'has_at', 'domain_valid', 'has_multiple_at',
                'suspicious_word', 'repeat_chars', 'is_impersonation',
                'digit_ratio', 'alpha_ratio', 'entropy_score',
                'starts_with_digit', 'report_count']

X = df[feature_cols].values
y = df['label'].values

print(f"Features: {len(feature_cols)}")
print(f"Fraud Rate: {(y.sum()/len(y))*100:.1f}%")

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42, stratify=y)

print(f"Training: {len(X_train):,} records")
print(f"Testing: {len(X_test):,} records")

# Models
models = {
    'XGBoost': xgb.XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42, eval_metric='logloss'),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42),
    'SVM': SVC(kernel='rbf', probability=True, random_state=42),
    'AdaBoost': AdaBoostClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42)
}

print("\n" + "=" * 60)
print("TRAINING RESULTS")
print("=" * 60)

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred) * 100
    prec = precision_score(y_test, y_pred) * 100
    rec = recall_score(y_test, y_pred) * 100
    f1 = f1_score(y_test, y_pred) * 100
    
    results[name] = {'accuracy': round(acc, 1), 'precision': round(prec, 1),
                     'recall': round(rec, 1), 'f1': round(f1, 1)}
    
    print(f"\n{name}:")
    print(f"  Accuracy: {acc:.1f}%")
    print(f"  Precision: {prec:.1f}%")
    print(f"  Recall: {rec:.1f}%")
    print(f"  F1-Score: {f1:.1f}%")

# Save models
joblib.dump(models, 'data/fraud_models.pkl')
joblib.dump(scaler, 'data/scaler.pkl')
print("\n✅ Models saved to data/")

best = max(results.items(), key=lambda x: x[1]['accuracy'])
print(f"\n🏆 BEST MODEL: {best[0]} with {best[1]['accuracy']}% accuracy")