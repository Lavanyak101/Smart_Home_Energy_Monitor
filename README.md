# Smart_Home_Energy_Monitor
A smart home energy monitoring dashboard with real-time tracking, budgeting, and visual analytics

⚡Smart Home Energy Monitor – A Next-Gen Energy Tracking Dashboard
Optimized for Real-Time Insights, Budgeting, and Smart Decision-Making
🚀 Why This Project?
💡 Energy efficiency is the need of the hour.
People often struggle with tracking and controlling their energy usage. High electricity bills? Inefficient appliances? No real-time data? These are common problems.

👉 Solution?
I built this Smart Home Energy Monitor to empower users with an interactive dashboard that provides:
✅ Real-time energy consumption updates
✅ Dynamic visual analytics (bar charts)
✅ Budget setting with alerts
✅ A sleek, responsive UI with Light/Dark mode

🎯 The goal? To help homeowners understand, control, and optimize their power usage effortlessl

# 🚀 Smart Home Energy Monitor

A sleek and interactive **smart home energy monitoring system** that helps users track real-time energy usage, set budgets, and visualize trends.

🔥 Key Features
✅ 📊 Real-time Energy Usage Tracking (Updates every 10 sec)
✅ 💰 Budget Setting & Alerts (Warns if energy usage exceeds limits)
✅ 🎨 Interactive Graphs & Insights (Bar charts for better analysis)
✅ 🌙 Light/Dark Mode (Enhances user experience)
✅ 💡 Easy to Extend (Can be connected to IoT devices in the future)  

## ⚙️ Tech Stack
| **Component**   | **Technology Used** |
|----------------|----------------|
| **Frontend**   | HTML, CSS, JavaScript, Chart.js |
| **Backend**    | Flask (Python) |
| **Styling**    | Custom CSS (with Light/Dark mode) |
| **API Handling** | Fetch API, Flask API |
| **Data Simulation** | Python (Randomized Values) |

## 📂 Project Structure
/smart-home-energy-monitor
│── backend/
│   ├── app.py          # Flask backend (API)
│── frontend/
│   ├── index.html      # UI of dashboard
│   ├── style.css       # Styling & light/dark mode
│   ├── script.js       # Fetches data & updates UI
│── README.md           # Documentation

🎯 Features I Implemented
✅ Real-time Energy Usage Tracking (Simulated sensor data updates every 10s)
✅ Dynamic Bar Chart for Energy Visualization
✅ Budget Setting & Alerts (Warns users if they exceed budget)
✅ Light/Dark Mode (User-friendly interface)
✅ Smooth UI & Interactive Design

🚀 Challenges Faced & Fixes
1️⃣ Delayed Chart Loading

Issue: Chart took 5 seconds to display data.
Fix: Called fetchEnergyData() immediately on page load to show data instantly.
2️⃣ CORS Policy Blocking API Requests

Issue: Frontend couldn’t fetch data due to CORS restrictions.
Fix: Used Flask-CORS to enable cross-origin requests.
3️⃣ Light Mode Not Persisting

Issue: Theme reset after page refresh.
Fix: Used localStorage to remember user preference.





