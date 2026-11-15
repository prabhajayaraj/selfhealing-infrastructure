# Self-Healing Infrastructure using Prometheus, Alertmanager & Ansible

## Project Overview

This project implements a Self-Healing Infrastructure system that automatically detects service failures and recovers them without manual intervention.

NGINX runs inside a Docker container and is monitored using Prometheus and Blackbox Exporter. When NGINX goes down, Prometheus generates an alert, and Alertmanager sends it to a Python Flask webhook. The webhook triggers an Ansible playbook to restart the failed NGINX container automatically.

## Project Objectives

- Monitor NGINX service availability.
- Detect service failures automatically.
- Generate alerts using Prometheus.
- Send alerts through Alertmanager.
- Receive alerts using Python Flask.
- Automatically restart NGINX using Ansible.
- Reduce manual intervention through automation.

## Technologies Used

- Docker
- Docker Compose
- NGINX
- Prometheus
- Blackbox Exporter
- Alertmanager
- Python
- Flask
- Ansible
- YAML
- Git & GitHub

## Architecture

```text
NGINX Web Server
       |
       v
Blackbox Exporter
       |
       v
Prometheus
       |
       v
Alertmanager
       |
       v
Python Flask Webhook
       |
       v
Ansible Playbook
       |
       v
Restart NGINX Container
       |
       v
Service Recovered
```

## Project Structure

```text
final-project1/
│
├── alertmanager/
│   └── alertmanager.yml
│
├── ansible/
│   └── restart-nginx.yml
│
├── nginx/
│   └── html/
│       └── index.html
│
├── prometheus/
│   ├── alerts.yml
│   ├── blackbox.yml
│   └── prometheus.yml
│
├── webhook/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

## How to Run the Project

**Step 1: Clone the repository**

```bash
git clone https://github.com/prabhajayaraj/selfhealing-infrastructure.git
```

**Step 2: Navigate to the project directory**

```bash
cd selfhealing-infrastructure
```

**Step 3: Start all services**

```bash
docker compose up -d --build
```

**Step 4: Check running containers**

```bash
docker ps
```

## Application URLs

| Service | URL |
|---|---|
| NGINX Website | http://localhost:8081 |
| Prometheus | http://localhost:9090 |
| Prometheus Targets | http://localhost:9090/targets |
| Prometheus Alerts | http://localhost:9090/alerts |
| Alertmanager | http://localhost:9093 |

## Testing Automatic Recovery

Stop the NGINX container to simulate a service failure:

```bash
docker stop demo-nginx
```

Prometheus detects the failure and triggers the `NginxDown` alert.

Alertmanager forwards the alert to the Flask webhook, which executes the Ansible playbook.

Ansible automatically restarts the NGINX container:

```bash
docker restart demo-nginx
```

Verify the container status:

```bash
docker ps
```

Open the website again:

http://localhost:8081

The NGINX service should be accessible after automatic recovery.

## Test Results

- All five Docker containers started successfully.
- Prometheus monitoring targets were UP.
- NGINX failure was detected successfully.
- Prometheus generated the `NginxDown` alert.
- Alertmanager delivered the alert to the webhook.
- Python Flask triggered Ansible automation.
- Ansible successfully restarted the NGINX container.
- The alert was subsequently resolved.

**Ansible Execution Result:**

```text
PLAY RECAP
localhost : ok=2 changed=1 unreachable=0 failed=0
```

## Key Benefits

- Automated failure detection.
- Automatic service recovery.
- Reduced manual intervention.
- Improved service availability.
- Infrastructure monitoring and automation.

## Future Enhancements

- Integrate Grafana dashboards.
- Add CPU and memory monitoring.
- Configure email notifications.
- Extend automation to additional services.
- Deploy infrastructure on AWS.

## Conclusion

This project demonstrates how DevOps monitoring and automation tools can work together to build a self-healing infrastructure.

By integrating Docker, Prometheus, Alertmanager, Python Flask and Ansible, service failures can be detected and recovered automatically.

## Author

**Surya Prabha J**

## GitHub Repository

https://github.com/prabhajayaraj/selfhealing-infrastructure
