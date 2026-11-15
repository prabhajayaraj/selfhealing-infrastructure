
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/alert", methods=["POST"])
def receive_alert():

    data = request.get_json(silent=True) or {}

    print("ALERT RECEIVED:", data, flush=True)

    for alert in data.get("alerts", []):

        status = alert.get("status")
        alertname = alert.get("labels", {}).get("alertname")

        print(f"Alert: {alertname}, Status: {status}", flush=True)

        if status == "firing" and alertname == "NginxDown":

            print("NGINX DOWN! Starting automatic recovery...", flush=True)

            result = subprocess.run(
                [
                    "ansible-playbook",
                    "-i",
                    "localhost,",
                    "-c",
                    "local",
                    "/ansible/restart-nginx.yml"
                ],
                capture_output=True,
                text=True
            )

            print("ANSIBLE OUTPUT:", result.stdout, flush=True)
            print("ANSIBLE ERRORS:", result.stderr, flush=True)

            if result.returncode != 0:
                return jsonify({
                    "status": "recovery_failed",
                    "error": result.stderr
                }), 500

            return jsonify({
                "status": "recovery_succeeded"
            }), 200

    return jsonify({"status": "no_action"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
