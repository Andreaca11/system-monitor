#  System Health Monitor (Python)

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
