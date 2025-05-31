#!/usr/bin/env python3
"""
Simple web interface for JEE Progress Tracker
Run this script to start a local web server for easier interaction
"""

import json
import os
from datetime import datetime, date
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import webbrowser
import threading
import time

from jee_tracker import JEEProgressTracker

class JEEWebHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.tracker = JEEProgressTracker()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        
        if path == '/':
            self.serve_dashboard()
        elif path == '/api/progress':
            self.serve_progress_api()
        elif path == '/api/subjects':
            self.serve_subjects_api()
        elif path.startswith('/static/'):
            self.serve_static_file(path)
        else:
            self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        if path == '/api/log-study':
            self.handle_log_study(post_data)
        elif path == '/api/update-topic':
            self.handle_update_topic(post_data)
        elif path == '/api/add-test':
            self.handle_add_test(post_data)
        else:
            self.send_error(404)

    def serve_dashboard(self):
        html_content = self.generate_dashboard_html()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

    def serve_progress_api(self):
        progress_data = {}
        for subject in ["Physics", "Chemistry", "Mathematics"]:
            progress_data[subject] = self.tracker.get_subject_progress(subject)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(progress_data).encode())

    def serve_subjects_api(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(self.tracker.syllabus).encode())

    def handle_log_study(self, post_data):
        try:
            data = json.loads(post_data)
            self.tracker.log_daily_study(
                data['subject'], 
                float(data['hours']), 
                data.get('topics', []), 
                data.get('notes', '')
            )
            self.send_json_response({"status": "success"})
        except Exception as e:
            self.send_json_response({"status": "error", "message": str(e)})

    def handle_update_topic(self, post_data):
        try:
            data = json.loads(post_data)
            self.tracker.update_topic_progress(
                data['subject'],
                data['chapter'],
                data['topic'],
                status=data.get('status'),
                confidence=data.get('confidence'),
                time_spent=data.get('time_spent'),
                notes=data.get('notes')
            )
            self.send_json_response({"status": "success"})
        except Exception as e:
            self.send_json_response({"status": "error", "message": str(e)})

    def handle_add_test(self, post_data):
        try:
            data = json.loads(post_data)
            self.tracker.add_test_score(
                data['test_name'],
                data['subject'],
                float(data['score']),
                float(data['max_score']),
                data.get('date')
            )
            self.send_json_response({"status": "success"})
        except Exception as e:
            self.send_json_response({"status": "error", "message": str(e)})

    def send_json_response(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def generate_dashboard_html(self):
        # Get current progress
        progress_data = {}
        for subject in ["Physics", "Chemistry", "Mathematics"]:
            progress_data[subject] = self.tracker.get_subject_progress(subject)

        html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JEE Progress Tracker</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}
        .container {{ 
            max-width: 1200px; 
            margin: 0 auto; 
            padding: 20px;
        }}
        .header {{ 
            text-align: center; 
            color: white; 
            margin-bottom: 30px;
        }}
        .header h1 {{ 
            font-size: 2.5em; 
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .dashboard {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
            gap: 20px; 
            margin-bottom: 30px;
        }}
        .card {{ 
            background: white; 
            border-radius: 15px; 
            padding: 25px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            transition: transform 0.3s ease;
        }}
        .card:hover {{ transform: translateY(-5px); }}
        .card h2 {{ 
            color: #4a5568; 
            margin-bottom: 15px; 
            border-bottom: 2px solid #e2e8f0; 
            padding-bottom: 10px;
        }}
        .progress-bar {{ 
            width: 100%; 
            height: 8px; 
            background: #e2e8f0; 
            border-radius: 4px; 
            overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{ 
            height: 100%; 
            background: linear-gradient(90deg, #48bb78, #38a169); 
            transition: width 0.3s ease;
        }}
        .stats {{ 
            display: grid; 
            grid-template-columns: repeat(2, 1fr); 
            gap: 15px; 
            margin-top: 15px;
        }}
        .stat {{ 
            text-align: center; 
            padding: 10px; 
            background: #f7fafc; 
            border-radius: 8px;
        }}
        .stat-value {{ 
            font-size: 1.5em; 
            font-weight: bold; 
            color: #2d3748;
        }}
        .stat-label {{ 
            font-size: 0.9em; 
            color: #718096; 
            margin-top: 5px;
        }}
        .actions {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 20px;
        }}
        .form-group {{ 
            margin-bottom: 15px;
        }}
        .form-group label {{ 
            display: block; 
            margin-bottom: 5px; 
            font-weight: 600; 
            color: #4a5568;
        }}
        .form-group input, .form-group select, .form-group textarea {{ 
            width: 100%; 
            padding: 10px; 
            border: 1px solid #e2e8f0; 
            border-radius: 8px; 
            font-size: 14px;
        }}
        .btn {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; 
            padding: 12px 24px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer; 
            font-size: 16px;
            transition: transform 0.2s ease;
        }}
        .btn:hover {{ transform: scale(1.02); }}
        .success {{ color: #38a169; font-weight: bold; }}
        .error {{ color: #e53e3e; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 JEE Progress Tracker</h1>
            <p>Track your preparation journey to success</p>
        </div>
        
        <div class="dashboard">
        '''
        
        # Generate subject cards
        colors = {"Physics": "#4299e1", "Chemistry": "#38b2ac", "Mathematics": "#ed8936"}
        
        for subject in ["Physics", "Chemistry", "Mathematics"]:
            progress = progress_data[subject]
            if "error" not in progress:
                completion = progress.get('completion_rate', 0)
                confidence = progress.get('avg_confidence', 0)
                study_time = progress.get('total_study_time', 0)
                total_topics = progress.get('total_topics', 0)
                
                html += f'''
            <div class="card">
                <h2 style="color: {colors[subject]}">📚 {subject}</h2>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {completion}%; background: {colors[subject]};"></div>
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value">{completion:.1f}%</div>
                        <div class="stat-label">Completed</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{confidence:.1f}/10</div>
                        <div class="stat-label">Confidence</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{study_time:.1f}h</div>
                        <div class="stat-label">Study Time</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{total_topics}</div>
                        <div class="stat-label">Total Topics</div>
                    </div>
                </div>
            </div>
                '''
        
        html += '''
        </div>
        
        <div class="actions">
            <div class="card">
                <h2>📝 Log Study Session</h2>
                <form id="studyForm">
                    <div class="form-group">
                        <label>Subject:</label>
                        <select name="subject" required>
                            <option value="">Select Subject</option>
                            <option value="Physics">Physics</option>
                            <option value="Chemistry">Chemistry</option>
                            <option value="Mathematics">Mathematics</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Hours Studied:</label>
                        <input type="number" name="hours" step="0.5" min="0" required>
                    </div>
                    <div class="form-group">
                        <label>Topics Covered (comma-separated):</label>
                        <input type="text" name="topics" placeholder="e.g., Kinematics, Laws of Motion">
                    </div>
                    <div class="form-group">
                        <label>Notes:</label>
                        <textarea name="notes" rows="3" placeholder="Any additional notes..."></textarea>
                    </div>
                    <button type="submit" class="btn">Log Study Session</button>
                </form>
                <div id="studyResult"></div>
            </div>
            
            <div class="card">
                <h2>🎯 Update Topic Progress</h2>
                <form id="topicForm">
                    <div class="form-group">
                        <label>Subject:</label>
                        <select name="subject" required>
                            <option value="">Select Subject</option>
                            <option value="Physics">Physics</option>
                            <option value="Chemistry">Chemistry</option>
                            <option value="Mathematics">Mathematics</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Chapter:</label>
                        <input type="text" name="chapter" required placeholder="e.g., Mechanics">
                    </div>
                    <div class="form-group">
                        <label>Topic:</label>
                        <input type="text" name="topic" required placeholder="e.g., Kinematics">
                    </div>
                    <div class="form-group">
                        <label>Status:</label>
                        <select name="status">
                            <option value="">Keep Current</option>
                            <option value="not_started">Not Started</option>
                            <option value="in_progress">In Progress</option>
                            <option value="completed">Completed</option>
                            <option value="revision">Revision</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Confidence (1-10):</label>
                        <input type="number" name="confidence" min="1" max="10">
                    </div>
                    <button type="submit" class="btn">Update Topic</button>
                </form>
                <div id="topicResult"></div>
            </div>
        </div>
    </div>

    <script>
        // Handle study form submission
        document.getElementById('studyForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                subject: formData.get('subject'),
                hours: formData.get('hours'),
                topics: formData.get('topics').split(',').map(t => t.trim()).filter(t => t),
                notes: formData.get('notes')
            };
            
            try {
                const response = await fetch('/api/log-study', {
                    method: 'POST',
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                
                const resultDiv = document.getElementById('studyResult');
                if (result.status === 'success') {
                    resultDiv.innerHTML = '<p class="success">✅ Study session logged successfully!</p>';
                    e.target.reset();
                    setTimeout(() => location.reload(), 1500);
                } else {
                    resultDiv.innerHTML = `<p class="error">❌ Error: ${result.message}</p>`;
                }
            } catch (error) {
                document.getElementById('studyResult').innerHTML = `<p class="error">❌ Error: ${error.message}</p>`;
            }
        });

        // Handle topic form submission
        document.getElementById('topicForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                subject: formData.get('subject'),
                chapter: formData.get('chapter'),
                topic: formData.get('topic'),
                status: formData.get('status') || undefined,
                confidence: formData.get('confidence') ? parseInt(formData.get('confidence')) : undefined
            };
            
            try {
                const response = await fetch('/api/update-topic', {
                    method: 'POST',
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                
                const resultDiv = document.getElementById('topicResult');
                if (result.status === 'success') {
                    resultDiv.innerHTML = '<p class="success">✅ Topic updated successfully!</p>';
                    e.target.reset();
                    setTimeout(() => location.reload(), 1500);
                } else {
                    resultDiv.innerHTML = `<p class="error">❌ Error: ${result.message}</p>`;
                }
            } catch (error) {
                document.getElementById('topicResult').innerHTML = `<p class="error">❌ Error: ${error.message}</p>`;
            }
        });
    </script>
</body>
</html>
        '''
        
        return html

def start_web_server(port=8080):
    """Start the web server"""
    server = HTTPServer(('localhost', port), JEEWebHandler)
    print(f"🚀 JEE Progress Tracker Web Interface")
    print(f"🌐 Server starting at http://localhost:{port}")
    print(f"📱 Open your browser and visit the above URL")
    print(f"⏹️  Press Ctrl+C to stop the server")
    
    # Open browser automatically after a short delay
    def open_browser():
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}')
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        server.shutdown()

if __name__ == "__main__":
    import sys
    port = 8080
    
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8080.")
    
    start_web_server(port)
