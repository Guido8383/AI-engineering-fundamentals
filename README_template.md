
# 🤖 Chatbot WiData

<!-- Badge dello stack tecnologico -->
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)

## 📋 Descrizione

<!-- TODO: 2-3 frasi che spiegano cosa fa il chatbot -->
...

## 🚀 Demo

<!-- TODO: link a Streamlit Cloud quando deployato -->
**Live**: [chatbot-widata.streamlit.app](https://...)

## ✨ Funzionalità

<!-- TODO: lista delle features principali -->
- ...

## 🛠 Stack tecnologico

<!-- TODO: tecnologie usate con descrizione breve -->
| Tecnologia | Uso |
|------------|-----|
| Claude Haiku | ... |
| ChromaDB | ... |
| Streamlit | ... |

## 📐 Architettura

<!-- TODO: descrizione del flusso RAG + tool in 3-4 righe -->
...

## ⚙️ Esecuzione in locale

```bash
# Clone
git clone https://github.com/TUO_USERNAME/AI-engineering-fundamentals
cd AI-engineering-fundamentals

# Installa dipendenze
pip install -r requirements.txt

# Configura API key
mkdir .streamlit
echo 'ANTHROPIC_API_KEY = "sk-ant-..."' > .streamlit/secrets.toml

# Avvia
streamlit run app.py
```

## 📍 Posizionamento Crawl-Walk-Run

<!-- TODO: dove si posiziona il chatbot e perché -->
Il chatbot si posiziona in zona **WALK** perché ha un'interfaccia grafica interattiva: Non è più un semplice script eseguito riga per riga nel terminale (fase Crawl), ma utilizza Streamlit per offrire una UI navigabile e user-friendly.

È accessibile online: È stato portato fuori dall'ambiente locale (localhost) ed è deployato in cloud, permettendo a qualsiasi utente di utilizzarlo tramite un URL pubblico.

Mantiene il contesto: Grazie all'uso di st.session_state, gestisce la memoria della conversazione e non tratta ogni messaggio come una singola chiamata API isolata.

Gestisce parametri dinamici: Permette all'utente di modificare in tempo reale impostazioni come la Temperature tramite una sidebar.

## 🔮 Passo successivo

<!-- TODO: cosa fareste per portarlo a RUN -->
Per avanzare verso RUN implementerei l'integrazione di un sistema RAG (Retrieval-Augmented Generation) completo utilizzando ChromaDB e PyPDF (già predisposti nel requirements.txt) per permettere al chatbot di rispondere basandosi su documenti aziendali proprietari.

Un sistema di autenticazione per limitare l'accesso solo agli utenti autorizzati.

Il salvataggio persistente delle conversazioni su un database esterno (es. PostgreSQL o MongoDB) per avere uno storico delle chat e fare analisi sui log.

---
*Progetto realizzato durante il corso AI Engineering Fundamentals*
*ITS Novitas 4.0 — Sassari, 2026*
