import os
from app import app

port = int(os.environ.get("env_app_port"))
host = os.environ.get("env_app_listen")

if __name__ == "__main__":
    app.run(port=port, host=host)
