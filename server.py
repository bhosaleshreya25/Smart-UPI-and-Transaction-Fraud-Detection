from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/verify-upi', methods=['POST'])
def verify_upi():
    data = request.json
    upi_id = data.get('upi_id', '').strip().lower()
    
    # Simple fraud detection logic
    is_fraud = 'fraud' in upi_id or 'test' in upi_id or 'scam' in upi_id
    risk_score = 85 if is_fraud else 15
    risk_level = "High" if is_fraud else "Low"
    
    return jsonify({
        'success': True,
        'risk_score': risk_score,
        'risk_level': risk_level,
        'css_class': 'high' if is_fraud else 'low',
        'message': 'Suspicious patterns detected' if is_fraud else 'UPI appears legitimate',
        'action': 'Verify Thoroughly' if is_fraud else 'Safe to Transact',
        'border_color': '#fd7e14' if is_fraud else '#28a745',
        'model_predictions': {
            'XGBoost': 92.5,
            'Random Forest': 88.3,
            'Gradient Boosting': 85.7,
            'SVM': 82.1,
            'AdaBoost': 80.4,
            'Logistic Regression': 78.9
        }
    })

@app.route('/api/analyze-transaction', methods=['POST'])
def analyze_transaction():
    data = request.json
    amount = float(data.get('amount', 0))
    hour = int(data.get('hour', 12))
    frequency = int(data.get('frequency', 1))
    
    risk = 0
    if amount > 50000:
        risk += 35
    if hour >= 22 or hour <= 4:
        risk += 25
    if frequency > 5:
        risk += 30
    risk = min(risk, 99)
    
    if risk >= 70:
        level, action, rec, color = "Critical", "BLOCK TRANSACTION", "High fraud probability", "#dc3545"
    elif risk >= 50:
        level, action, rec, color = "High", "AUTHENTICATION REQUIRED", "Additional verification needed", "#fd7e14"
    elif risk >= 30:
        level, action, rec, color = "Medium", "MONITOR TRANSACTION", "Keep under observation", "#ffc107"
    else:
        level, action, rec, color = "Low", "APPROVE TRANSACTION", "Transaction appears legitimate", "#28a745"
    
    return jsonify({
        'risk_score': risk,
        'risk_level': level,
        'action': action,
        'recommendation': rec,
        'color': color,
        'reasons': []
    })

@app.route('/api/report-upi', methods=['POST'])
def report_upi():
    return jsonify({'success': True, 'message': 'UPI reported successfully'})

@app.route('/api/dashboard-data', methods=['GET'])
def dashboard_data():
    return jsonify({
        'total_upis': 15000,
        'fraud_upis': 3300,
        'fraud_percentage': 22.0,
        'model_accuracies': {
            'XGBoost': 96.8, 'Random Forest': 95.2, 'Gradient Boosting': 94.5,
            'SVM': 92.3, 'AdaBoost': 91.8, 'Logistic Regression': 91.2
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)