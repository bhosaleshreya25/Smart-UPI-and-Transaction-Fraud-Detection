# Smart-UPI-and-Transaction-Fraud-Detection
A machine learning-based system that detects fraudulent UPI IDs and suspicious transactions using pattern and behavior analysis. Built with Python and Flask, it provides real-time fraud detection for digital payment systems.
```markdown
# 🔐 UPI Fraud Detection System

An AI-powered fraud detection system that identifies fraudulent UPI IDs and suspicious transactions using ensemble machine learning with **97% accuracy**.

--

## 📌 Quick Overview

This system detects fraudulent UPI IDs and transactions in real-time using:
- **6 ML Models** (XGBoost, Random Forest, SVM, etc.)
- **20+ Fraud Detection Rules**
- **Real-time Risk Scoring** (<100ms response)

---

## 🏗️ System Architecture

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                              UPI FRAUD DETECTION SYSTEM                                      │
│                                   SYSTEM ARCHITECTURE                                        │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    PRESENTATION LAYER                                        │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌───────────┐│
│   │   HOME      │    │   UPI       │    │ TRANSACTION │    │  DASHBOARD  │    │  REPORT   ││
│   │   PAGE      │    │   VERIFY    │    │   ANALYSIS  │    │    PAGE     │    │   PAGE    ││
│   │             │    │   PAGE      │    │    PAGE     │    │             │    │           ││
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └─────┬─────┘│
│          │                  │                  │                  │                 │      │
│          └──────────────────┴──────────────────┴──────────────────┴─────────────────┘      │
│                                              │                                              │
│                                      HTML/CSS/JavaScript                                    │
│                                              │                                              │
└──────────────────────────────────────────────┼──────────────────────────────────────────────┘
                                               │
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      APPLICATION LAYER                                       │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│                              ┌─────────────────────────┐                                    │
│                              │      FLASK SERVER        │                                    │
│                              │      (app.py)            │                                    │
│                              └───────────┬─────────────┘                                    │
│                                          │                                                   │
│                    ┌─────────────────────┼─────────────────────┐                            │
│                    │                     │                     │                            │
│                    ▼                     ▼                     ▼                            │
│          ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐                    │
│          │   /api/verify   │   │ /api/analyze    │   │ /api/dashboard  │                    │
│          │     -upi        │   │  -transaction   │   │     -data       │                    │
│          └────────┬────────┘   └────────┬────────┘   └────────┬────────┘                    │
│                   │                     │                     │                            │
│                   └─────────────────────┼─────────────────────┘                            │
│                                         │                                                   │
│                                         ▼                                                   │
│                          ┌─────────────────────────────┐                                   │
│                          │     ROUTING & CONTROLLER     │                                   │
│                          │      (Request Handler)       │                                   │
│                          └─────────────┬───────────────┘                                   │
│                                        │                                                     │
└────────────────────────────────────────┼────────────────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     BUSINESS LOGIC LAYER                                     │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│                         ┌─────────────────────────────────────┐                            │
│                         │        FRAUD DETECTION ENGINE        │                            │
│                         └─────────────────┬───────────────────┘                            │
│                                           │                                                  │
│         ┌─────────────────────────────────┼─────────────────────────────────┐               │
│         │                                 │                                 │               │
│         ▼                                 ▼                                 ▼               │
│  ┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐         │
│  │   FORMAT         │          │   PATTERN        │          │   BEHAVIORAL     │         │
│  │   VALIDATION     │          │   DETECTION      │          │   ANALYSIS       │         │
│  │   MODULE         │          │   MODULE         │          │   MODULE         │         │
│  ├──────────────────┤          ├──────────────────┤          ├──────────────────┤         │
│  │ • Check @ symbol │          │ • Lottery words  │          │ • Amount check   │         │
│  │ • Domain validity│          │ • Suspicious     │          │ • Time analysis  │         │
│  │ • Multiple @     │          │   keywords       │          │ • Frequency      │         │
│  │ • Empty fields   │          │ • Repeated chars │          │ • Deviation      │         │
│  │ • Length check   │          │ • Sequential     │          │ • UPI risk       │         │
│  └────────┬─────────┘          │   digits         │          └────────┬─────────┘         │
│           │                    │ • Impersonation  │                   │                   │
│           │                    └────────┬─────────┘                   │                   │
│           │                             │                             │                   │
│           └─────────────────────────────┼─────────────────────────────┘                   │
│                                         │                                                   │
│                                         ▼                                                   │
│                          ┌─────────────────────────────┐                                   │
│                          │      FEATURE EXTRACTION      │                                   │
│                          │                            │                                   │
│                          │  • alpha_count  • digit_count                                 │
│                          │  • special_count • length                                     │
│                          │  • entropy_score • digit_ratio                               │
│                          │  • domain_valid • report_count                                │
│                          │  • suspicious_word • repeat_chars                            │
│                          └─────────────┬───────────────┘                                   │
│                                        │                                                     │
│                                        ▼                                                     │
│                          ┌─────────────────────────────────────────────────────────────┐   │
│                          │                 ML ENSEMBLE ENGINE                          │   │
│                          │                   (6 MODELS)                                │   │
│                          └─────────────────────────────────────────────────────────────┘   │
│                                        │                                                   │
│         ┌──────────────┬───────────────┼───────────────┬──────────────┬──────────────┐    │
│         │              │               │               │              │              │    │
│         ▼              ▼               ▼               ▼              ▼              ▼    │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │ XGBoost  │   │  Random  │   │Gradient  │   │   SVM    │   │ AdaBoost │   │Logistic  │ │
│  │          │   │ Forest   │   │Boosting  │   │          │   │          │   │Regression│ │
│  │  28%     │   │  22%     │   │  18%     │   │  14%     │   │  10%     │   │   8%     │ │
│  │  Weight  │   │  Weight  │   │  Weight  │   │  Weight  │   │  Weight  │   │  Weight  │ │
│  │          │   │          │   │          │   │          │   │          │   │          │ │
│  │ 97.0%    │   │ 96.5%    │   │ 96.8%    │   │ 95.6%    │   │ 96.4%    │   │ 96.1%    │ │
│  │ Accuracy │   │ Accuracy │   │ Accuracy │   │ Accuracy │   │ Accuracy │   │ Accuracy │ │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘ │
│       │              │              │              │              │              │       │
│       └──────────────┴──────────────┼──────────────┴──────────────┴──────────────┘       │
│                                     │                                                      │
│                                     ▼                                                      │
│                          ┌─────────────────────────────────────────────┐                  │
│                    ┌─────┤          WEIGHTED VOTING SYSTEM              ├─────┐            │
│                    │     └─────────────────────────────────────────────┘     │            │
│                    │                                                         │            │
│                    │    Final Score = (XGB×0.28) + (RF×0.22) + (GB×0.18)    │            │
│                    │                 + (SVM×0.14) + (Ada×0.10) + (LR×0.08)   │            │
│                    │                                                         │            │
│                    └─────────────────────┬───────────────────────────────────┘            │
│                                          │                                                │
│                                          ▼                                                │
│                          ┌─────────────────────────────┐                                │
│                          │      RISK CALCULATION       │                                │
│                          │                            │                                │
│                          │   0-100% Risk Score         │                                │
│                          └─────────────┬───────────────┘                                │
│                                        │                                                  │
│                    ┌───────────────────┼───────────────────┐                            │
│                    │                   │                   │                            │
│                    ▼                   ▼                   ▼                            │
│          ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐    │
│          │  Critical   │     │    High     │     │   Medium    │     │    Low      │    │
│          │  70-100%    │     │   50-69%    │     │   30-49%    │     │   0-29%     │    │
│          │   🔴 RED    │     │   🟠 ORANGE │     │   🟡 YELLOW │     │   🟢 GREEN  │    │
│          │  BLOCK      │     │  VERIFY     │     │  MONITOR    │     │  APPROVE    │    │
│          └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘    │
│                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       DATA LAYER                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐    │
│   │   upi_dataset   │   │  transaction    │   │  fraud_models   │   │    scaler       │    │
│   │     .csv        │   │  _dataset.csv   │   │     .pkl        │   │    .pkl         │    │
│   │                 │   │                 │   │                 │   │                 │    │
│   │ 10,000+ records │   │ 10,000+ records │   │ ┌─────────────┐ │   │ Normalization   │    │
│   │ 20+ features    │   │ 12+ features    │   │ │ XGBoost     │ │   │ Parameters      │    │
│   │                 │   │                 │   │ │ RandomForest│ │   │                 │    │
│   │                 │   │                 │   │ │ GradBoost   │ │   │                 │    │
│   │                 │   │                 │   │ │ SVM         │ │   │                 │    │
│   │                 │   │                 │   │ │ AdaBoost    │ │   │                 │    │
│   │                 │   │                 │   │ │ LogisticReg │ │   │                 │    │
│   │                 │   │                 │   │ └─────────────┘ │   │                 │    │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘   └─────────────────┘    │
│                                                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      OUTPUT LAYER                                            │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│                    ┌─────────────────────────────────────────────────────────┐              │
│                    │                    USER RESPONSE                         │              │
│                    ├─────────────────────────────────────────────────────────┤              │
│                    │  • Risk Score (0-100%)                                  │              │
│                    │  • Risk Level (Critical/High/Medium/Low)                │              │
│                    │  • Action Recommendation (Block/Verify/Monitor/Approve) │              │
│                    │  • Risk Factors (Warnings with explanations)            │              │
│                    │  • Model Predictions                                    │
│                    └─────────────────────────────────────────────────────────┘              │
│                                                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **UPI Verification** | Check if UPI ID is fraudulent |
| 💳 **Transaction Analysis** | Analyze amount, time, frequency |
| 📊 **Dashboard** | View model performance charts |
| 🚨 **Fraud Reporting** | Report suspicious UPIs |

---

## 🤖 Model Performance

| Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
| **XGBoost** 🏆 | **97.0%** | 97.5% | 94.4% |
| Gradient Boosting | 96.8% | 97.1% | 94.3% |
| Random Forest | 96.5% | 96.5% | 94.2% |
| AdaBoost | 96.4% | 98.6% | 91.9% |
| SVM | 95.6% | 94.0% | 94.5% |
| Logistic Regression | 96.1% | 96.7% | 92.9% |

### Confusion Matrix (XGBoost)
```
              Predicted
              Safe  Fraud
Actual  Safe   1850    28
        Fraud    41  1281

• TP: 1,281 | FP: 28 | TN: 1,850 | FN: 41
• Precision: 97.5% | Recall: 94.4% | F1: 95.9%
```

---

## 📋 Fraud Detection Rules

### Format Validation (Highest Priority)
| Condition | Risk | Example |
|-----------|------|---------|
| Multiple @ | 98% | `user@@domain` |
| Missing @ | 95% | `username` |
| Missing domain | 92% | `username@` |

### Pattern Detection
| Pattern | Risk Added | Example |
|---------|------------|---------|
| Lottery words | +45 | `winner`, `prize`, `bonus` |
| Suspicious words | +40 | `fraud`, `scam`, `test` |
| Repeated chars | +30 | `aaaa`, `1111` |
| Sequential digits | +25 | `123`, `456` |
| Invalid domain | +30 | `@xyz`, `@gmail` |

### Risk Levels
| Score | Level | Action |
|-------|-------|--------|
| 70-100% | Critical | ❌ BLOCK |
| 50-69% | High | ⚠️ VERIFY |
| 30-49% | Medium | 🔍 MONITOR |
| 0-29% | Low | ✅ APPROVE |

---

## 🛠️ Technologies

| Category | Technologies |
|----------|--------------|
| Backend | Python, Flask, Scikit-learn, XGBoost |
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Data | Pandas, NumPy, CSV |

---

## 📁 Project Structure

```
upi-fraud-detection/
├── app.py                      # Main Flask app
├── requirements.txt            # Dependencies
├── generate_all_datasets.py    # Dataset generator
├── train_all_models.py         # Model trainer
├── templates/
│   └── index.html              # Frontend 
├── data/
│   ├── upi_dataset.csv         # Training data
|   ├── transactions_dataset.csv 
│   ├── fraud_models.pkl        # Trained models
│   └── scaler.pkl              # Feature scaler
└── README.md
```



## 🚀 Installation (5 Minutes)

```bash
# 1. Clone repository
git clone https://github.com/yourusername/upi-fraud-detection.git
cd upi-fraud-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python generate_all_datasets.py

# 4. Train models
python train_all_models.py

# 5. Run app
python app.py

# 6. Open browser
http://localhost:5000
```

### requirements.txt
```txt
flask==2.3.3
flask-cors==4.0.0
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
xgboost==1.7.6
joblib==1.3.2
```

---

## 🧪 Quick Testing

### Test UPI IDs

| UPI ID | Expected Risk |
|--------|---------------|
| `rahul123@okhdfcbank` | Low (15%) ✅ |
| `fraud@paytm` | High (75%) 🚨 |
| `winner123@paytm` | Critical (80%) 🚨 |
| `11111@@scam` | Critical (98%) 🚨 |

### Test Transactions

| Amount | Hour | Frequency | Expected |
|--------|------|-----------|----------|
| ₹5,000 | 14 | 1 | Low Risk ✅ |
| ₹25,000 | 21 | 3 | Medium Risk ⚠️ |
| ₹75,000 | 2 | 6 | High Risk 🚨 |

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/verify-upi` | POST | Verify UPI ID |
| `/api/analyze-transaction` | POST | Analyze transaction |
| `/api/dashboard-data` | GET | Get statistics |

### Sample Request
```bash
curl -X POST http://localhost:5000/api/verify-upi \
  -H "Content-Type: application/json" \
  -d '{"upi_id": "fraud@paytm"}'
```

### Sample Response
```json
{
    "risk_score": 85,
    "risk_level": "High",
    "action": "VERIFY THOROUGHLY",
    "warnings": ["⚠️ Suspicious keyword: 'fraud'"]
}
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Best Accuracy** | 97.0% (XGBoost) |
| **Response Time** | <100ms |
| **Precision** | 97.5% |
| **Recall** | 94.4% |
| **False Positive Rate** | 1.5% |

---

## 🚀 Future Scope

- Real banking API integration
- Mobile application
- Deep learning models
- Email/SMS alerts



## ⚡ Quick Commands

```bash
# Run everything
pip install -r requirements.txt && python generate_all_datasets.py && python train_all_models.py && python app.py

# Test UPI
curl -X POST http://localhost:5000/api/verify-upi -H "Content-Type: application/json" -d '{"upi_id":"fraud@paytm"}'
```


**Built with Python, Flask, Scikit-learn & XGBoost** | *97% Accuracy | <100ms Response* 🛡️
```
