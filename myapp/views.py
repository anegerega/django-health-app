from django.http import JsonResponse, HttpResponse
import platform

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Container App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #f5f5f5;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #0c4b33; }
            .info { 
                background: #e8f5e9;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
            }
            a {
                color: #0c4b33;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐳 Django Container App</h1>
            <p>Welcome to your containerized Django application!</p>
            
            <div class="info">
                <h3>System Information:</h3>
                <ul>
                    <li><strong>Platform:</strong> """ + platform.system() + """</li>
                    <li><strong>Python Version:</strong> """ + platform.python_version() + """</li>
                    <li><strong>Hostname:</strong> """ + platform.node() + """</li>
                </ul>
            </div>
            
            <h3>Available Endpoints:</h3>
            <ul>
                <li><a href="/">/</a> - Home page (this page)</li>
                <li><a href="/about/">/about/</a> - About page</li>
                <li><a href="/health/">/health/</a> - Health check (JSON)</li>
            </ul>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About - Django Container App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #f5f5f5;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #0c4b33; }
            a { color: #0c4b33; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About This App</h1>
            <p>This is a minimal Django application designed for practicing Docker containerization.</p>
            <p>Perfect for learning:</p>
            <ul>
                <li>Docker basics</li>
                <li>Docker Compose</li>
                <li>Container orchestration</li>
                <li>CI/CD pipelines</li>
            </ul>
            <p><a href="/">← Back to Home</a></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def health(request):
    return JsonResponse({
        'status': 'healthy',
        'platform': platform.system(),
        'python_version': platform.python_version(),
        'hostname': platform.node()
    })