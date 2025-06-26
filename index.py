from flask import Flask, request, jsonify, render_template_string
import hashlib
import time

app = Flask(__name__)
app.secret_key = 'moonton-secret-2025'

# HTML Template sebagai string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moonton Account Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .main-container { background: rgba(255,255,255,0.95); border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="main-container p-5">
                    <div class="text-center mb-5">
                        <h1 class="display-4 text-primary">
                            <i class="fas fa-gamepad me-3"></i>Moonton Account Manager
                        </h1>
                        <p class="lead text-muted">Manage your Mobile Legends account with ease</p>
                    </div>

                    <div class="row">
                        <div class="col-md-6 offset-md-3">
                            <div class="card shadow">
                                <div class="card-header bg-primary text-white text-center">
                                    <h4><i class="fas fa-sign-in-alt me-2"></i>Login to Moonton</h4>
                                </div>
                                <div class="card-body">
                                    <form id="loginForm">
                                        <div class="mb-3">
                                            <label class="form-label">
                                                <i class="fas fa-user me-1"></i>Username/Email
                                            </label>
                                            <input type="text" class="form-control" id="username" required>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label">
                                                <i class="fas fa-lock me-1"></i>Password
                                            </label>
                                            <input type="password" class="form-control" id="password" required>
                                        </div>
                                        <div class="d-grid">
                                            <button type="submit" class="btn btn-primary btn-lg">
                                                <i class="fas fa-sign-in-alt me-2"></i>Login
                                            </button>
                                        </div>
                                    </form>
                                    <div id="result" class="mt-3"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="row mt-5">
                        <div class="col-md-4">
                            <div class="card text-center">
                                <div class="card-body">
                                    <i class="fas fa-shield-alt fa-3x text-primary mb-3"></i>
                                    <h5>Secure Login</h5>
                                    <p class="text-muted">Login safely without mobile app</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card text-center">
                                <div class="card-body">
                                    <i class="fas fa-envelope fa-3x text-success mb-3"></i>
                                    <h5>Change Email</h5>
                                    <p class="text-muted">Update email easily</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card text-center">
                                <div class="card-body">
                                    <i class="fas fa-mobile-alt fa-3x text-info mb-3"></i>
                                    <h5>Mobile Ready</h5>
                                    <p class="text-muted">Works on all devices</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="alert alert-warning mt-4" role="alert">
                        <i class="fas fa-exclamation-triangle me-2"></i>
                        <strong>Demo Version:</strong> This is a working prototype. For educational purposes only.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const result = document.getElementById('result');
            
            result.innerHTML = '<div class="alert alert-info"><i class="fas fa-spinner fa-spin me-2"></i>Processing login...</div>';
            
            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({username, password})
                });
                
                const data = await response.json();
                
                if (data.success) {
                    result.innerHTML = `
                        <div class="alert alert-success">
                            <i class="fas fa-check-circle me-2"></i>
                            <strong>Login Demo Successful!</strong><br>
                            Username: <strong>${data.username}</strong><br>
                            <small class="text-muted">In real implementation, this would connect to Moonton API</small>
                        </div>
                        <div class="mt-3">
                            <h6>Next Steps (Demo):</h6>
                            <button class="btn btn-success btn-sm me-2" onclick="showChangeEmail()">
                                <i class="fas fa-envelope me-1"></i>Change Email
                            </button>
                            <button class="btn btn-info btn-sm" onclick="showAccountInfo()">
                                <i class="fas fa-user me-1"></i>Account Info
                            </button>
                        </div>`;
                } else {
                    result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-times-circle me-2"></i>${data.message}</div>`;
                }
            } catch (error) {
                result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle me-2"></i>Error: ${error.message}</div>`;
            }
        });

        function showChangeEmail() {
            document.getElementById('result').innerHTML += `
                <div class="mt-3 p-3 border rounded">
                    <h6><i class="fas fa-envelope me-2"></i>Change Email (Demo)</h6>
                    <div class="mb-2">
                        <input type="email" class="form-control form-control-sm" placeholder="New email address">
                    </div>
                    <div class="mb-2">
                        <input type="password" class="form-control form-control-sm" placeholder="Current password">
                    </div>
                    <button class="btn btn-success btn-sm" onclick="alert('Demo: Email would be changed via Moonton API')">
                        <i class="fas fa-save me-1"></i>Change Email
                    </button>
                </div>`;
        }

        function showAccountInfo() {
            document.getElementById('result').innerHTML += `
                <div class="mt-3 p-3 border rounded bg-light">
                    <h6><i class="fas fa-user me-2"></i>Account Info (Demo)</h6>
                    <small class="text-muted">
                        <strong>User ID:</strong> 123456789<br>
                        <strong>Email:</strong> user@example.com<br>
                        <strong>Country:</strong> Indonesia<br>
                        <strong>Status:</strong> <span class="badge bg-success">Active</span>
                    </small>
                </div>`;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            return jsonify({
                'success': False,
                'message': 'Username and password are required'
            })
        
        # Demo validation - dalam implementasi real, ini akan connect ke Moonton API
        if len(username) >= 3 and len(password) >= 6:
            # Simulate Moonton API response
            return jsonify({
                'success': True,
                'username': username,
                'user_id': '123456789',
                'email': f'{username}@example.com',
                'message': 'Demo login successful',
                'note': 'This is a working demo. Real implementation would validate with Moonton servers.'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Username must be at least 3 characters and password at least 6 characters'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Moonton Account Manager',
        'version': '1.0.0',
        'timestamp': time.time()
    })

@app.route('/api/info')
def api_info():
    return jsonify({
        'name': 'Moonton Account Manager API',
        'version': '1.0.0',
        'endpoints': {
            '/': 'Main application',
            '/login': 'Login endpoint (POST)',
            '/health': 'Health check',
            '/api/info': 'API information'
        },
        'status': 'running'
    })

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=True)
