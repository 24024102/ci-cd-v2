from fastapi import FastAPI
import redis
import socket 
from fastapi.responses import HTMLResponse

app = FastAPI()
r = redis.Redis(host='redise-service', port=6379, decode_responses=True)
@app.get("/")
def read_root():
    try:
        hits =  r.incr('hits')
    except redis.ConnectionError:
        hits = "Redis is busy:("
    pod_name = socket.gethostname()
    html_content = f"""
    <DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Мой K8s Кластер</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #2c3e50; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background-color: #34495e; padding: 40px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); text-align: center; max-width: 500px; }}
                h1 {{ margin-top: 0; color: #ecf0f1; }}
                .pod-name {{ color: #e74c3c; font-size: 28px; font-weight: bold; margin: 20px 0; background: #2c3e50; padding: 10px; border-radius: 8px; }}
                .counter {{ color: #2ecc71; font-size: 48px; font-weight: bold; margin: 20px 0; }}
                button {{ background-color: #3498db; color: white; border: none; padding: 15px 30px; font-size: 16px; border-radius: 5px; cursor: pointer; transition: 0.3s; }}
                button:hover {{ background-color: #2980b9; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 K8s Web Cluster</h1>
                <p>XDXDXDXD:</p>
                <div class="counter">{hits}</div>
                <p>Ваш запрос обработал Pod:</p>
                <div class="pod-name">{pod_name}</div>
                <button onclick="window.location.reload();">🔄 Обновить и сменить сервер</button>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)