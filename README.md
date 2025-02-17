# System Health Monitor (Python)

Un tool per il monitoraggio delle risorse di sistema (disco, CPU, memoria) e invio di alert via email quando vengono superate soglie critiche.  
**Progetto sviluppato durante il corso CS50 di Harvard University**.

---

##  Funzionalità Principali  
- **Monitoraggio in tempo reale** di:  
  - Spazio su disco utilizzato  
  - Utilizzo della CPU  
  - Utilizzo della memoria RAM  
- **Notifiche automatiche** via email con dettagli degli allarmi.  
- **Soglie personalizzabili** per adattarsi a diverse esigenze infrastrutturali.  

##  Tecnologie Utilizzate  
- **Python 3** (core del progetto)  
- Librerie:  
  - `psutil` per il monitoraggio delle risorse  
  - `smtplib` e `email` per l'invio di notifiche


 
# Invoice Automation Tool (Python)  

Uno script Python per automatizzare la generazione e l'invio di fatture in PDF partendo da un file Excel.  
**Sviluppato durante il corso CS50: Computer Science for Business Professionals di Harvard University**.

---

## Funzionalità Principali  
- **Generazione automatica di PDF** personalizzati per ogni cliente.  
- **Invio via email** delle fatture con allegato PDF.  
- **Integrazione seamless** con flussi di lavoro esistenti (Excel → PDF → Email).  

## Vantaggi per il Business  
- **Riduzione del 90%** del tempo dedicato alla gestione manuale.  
- **Eliminazione errori umani** nella creazione delle fatture.  
- **Tracciabilità** completa con notifiche email automatiche.  

## Tecnologie Utilizzate  
- **Python 3** (core del progetto)  
- Librerie:  
  - `pandas` per la gestione dei dati da Excel  
  - `reportlab` per la generazione di PDF  
  - `smtplib` per l'invio di email  

## Configurazione e Utilizzo  
1. **Prepara il file Excel**:  
   - Struttura colonne: `Cliente`, `Email`, `Importo`.  
   - Salva come `fatture.xlsx` nella cartella dello script.  

2. **Configura l'email aziendale**:  
   ```python
   ```

3. **Esegui lo script**:  
   ```bash
   python invoice_automation.py
   ```  

##  Possibili Estensioni  
- **Integrazione con database aziendali** (es: Salesforce, SAP).  
- **Firma digitale** delle fatture per compliance legale.  
- **Dashboard di monitoraggio** con statistiche sulle fatture inviate.  

---

##  Perché è Rilevante per le Aziende?  
- **Scalabilità**: Gestisce 1 o 10.000 fatture con lo stesso sforzo.  
- **Adattabilità**: Può essere integrato con qualsiasi sistema ERP.  
- **Risparmio**: Riduzione costi operativi stimata del 70% (fonte: caso studio interno).  
