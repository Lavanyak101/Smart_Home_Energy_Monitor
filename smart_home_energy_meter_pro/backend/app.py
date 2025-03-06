from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Simulated energy data
energy_data = {
    "Air Conditioner": random.randint(500, 1200),
    "Refrigerator": random.randint(200, 400),
    "TV": random.randint(100, 300),
    "Lights": random.randint(50, 150),
}

# Store user budget
user_budget = {"budget": 500}

@app.route('/')
def home():
    return "Smart Home Energy Monitor Pro API is running!"

@app.route('/get_energy_data')
def get_energy_data():
    return jsonify(energy_data)

@app.route('/set_budget', methods=['POST'])
def set_budget():
    try:
        data = request.get_json()
        if data and "budget" in data:
            user_budget["budget"] = int(data["budget"])
            return jsonify({"message": "Budget updated successfully!", "budget": user_budget["budget"]})
        else:
            return jsonify({"error": "Invalid request, 'budget' key missing!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/check_budget')
def check_budget():
    total_usage = sum(energy_data.values())
    budget_exceeded = total_usage > user_budget["budget"]
    return jsonify({"total_usage": total_usage, "budget_exceeded": budget_exceeded})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


