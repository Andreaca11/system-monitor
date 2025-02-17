import psutil
import smtplib
from email.mime.text import MIMEText

# Soglie di allarme (personalizzabili)
DISK_THRESHOLD = 80  # 80% spazio su disco utilizzato
CPU_THRESHOLD = 85    # 85% utilizzo CPU
MEMORY_THRESHOLD = 75 # 75% utilizzo memoria

def check_system_health():
    alerts = []
    
    # Monitoraggio spazio su disco
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        alerts.append(f"🚨 Disco: {disk_usage.percent}% utilizzato (soglia: {DISK_THRESHOLD}%)")
    
    # Monitoraggio CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"🚨 CPU: {cpu_usage}% utilizzata (soglia: {CPU_THRESHOLD}%)")
    
    # Monitoraggio memoria
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        alerts.append(f"🚨 Memoria: {memory_usage}% utilizzata (soglia: {MEMORY_THRESHOLD}%)")
    
    return alerts

def send_email_alert(alerts):
    # Configurazione email (esempio con Gmail)
    sender = "your.email@gmail.com"
    receiver = "admin@company.com"
    password = "your-app-password"  # Usa una password specifica per app
    
    body = "\n".join(alerts)
    msg = MIMEText(body)
    msg['Subject'] = "⚠️ System Health Alert"
    msg['From'] = sender
    msg['To'] = receiver
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("✅ Allarme inviato con successo!")
    except Exception as e:
        print(f"❌ Errore: {e}")

if __name__ == "__main__":
    alerts = check_system_health()
    if alerts:
        send_email_alert(alerts)
    else:
        print("✅ Sistema in salute!")
