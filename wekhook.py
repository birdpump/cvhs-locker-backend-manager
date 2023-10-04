from flask import Flask, request
import subprocess
import time

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verify the webhook payload (optional)

    # Stop and remove the existing container (if it exists)
    subprocess.run(['docker', 'stop', 'locker-backend'], stderr=subprocess.DEVNULL)
    subprocess.run(['docker', 'rm', 'locker-backend'], stderr=subprocess.DEVNULL)

    # Add a delay before pulling the new Docker image (e.g., 30 seconds)
    time.sleep(30)

    # Pull the new Docker image
    subprocess.run(['docker', 'pull', 'ghcr.io/birdpump/cvhs-locker-backend/cvhs-locker-backend:latest'])

    # Start a new container using the updated image
    subprocess.run(['docker', 'run', '-d', '-p', '3000:3000', '--name', 'locker-backend', 'cvhs-locker-backend:latest'])

    return 'Webhook received and processed', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
