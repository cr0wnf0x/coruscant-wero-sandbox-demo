from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    """
    Simulates a payment processing endpoint.
    Expects an XML payload.
    If 'FAIL' is present in the payload, rejects the payment.
    """
    try:
        # Get raw data as string to check for 'FAIL'
        payload = request.data.decode('utf-8')
        
        if 'FAIL' in payload:
            return jsonify({
                "status": "REJECTED",
                "reason": "MS03" # Reason code for 'Rejected by Agent'
            }), 400
            
        return jsonify({
            "status": "ACCEPTED",
            "tx_id": "WERO-12345"
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "ERROR",
            "reason": str(e)
        }), 500

if __name__ == '__main__':
    # Run with: python3 mock_gateway.py
    print("Starting Wero Mock Gateway on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
