import pandas as pd
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Leggi i dati delle fatture da un file Excel
df = pd.read_excel("fatture.xlsx")

# Genera una fattura in PDF per ogni riga
for index, row in df.iterrows():
    cliente = row["Cliente"]
    importo = row["Importo"]
    
    # Crea il PDF
    nome_file = f"Fattura_{cliente}.pdf"
    c = canvas.Canvas(nome_file)
    c.drawString(100, 750, f"Fattura per: {cliente}")
    c.drawString(100, 730, f"Importo: €{importo}")
    c.save()
    
    # Invia la fattura via email
    msg = MIMEMultipart()
    msg["Subject"] = f"Fattura {nome_file}"
    msg["From"] = "tua.azienda@gmail.com"
    msg["To"] = row["Email"]
    
    with open(nome_file, "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header("Content-Disposition", "attachment", filename=nome_file)
        msg.attach(attach)
    
    # Configura l'invio (es: Gmail)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("tua.azienda@gmail.com", "password-app")
        server.send_message(msg)

print("✅ Fatture generate e inviate con successo!")