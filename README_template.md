
# 🤖 Chatbot WiData

<!-- Badge dello stack tecnologico -->
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)

## 📋 Descrizione

<!-- TODO: 2-3 frasi che spiegano cosa fa il chatbot -->
Il Chatbot WiData è un assistente virtuale intelligente sviluppato per supportare le attività e l'operatività di WiData Srl, startup IoT con sede a Sassari. L'applicazione offre un'interfaccia web intuitiva e personalizzabile, progettata per interagire con gli utenti fornendo risposte rapide, coerenti e strettamente aderenti al contesto aziendale.

## 🚀 Demo

<!-- TODO: link a Streamlit Cloud quando deployato -->
**Live**: [chatbot-widata.streamlit.app]([(https://ai-engineering-fundamentals-birqdcu9nkygcvgpd6wons.streamlit.app/))]

## ✨ Funzionalità

<!-- TODO: lista delle features principali -->
Interazione in Real-Time: Conversazioni fluide con streaming progressivo del testo (effetto macchina da scrivere).

Gestione del Contesto: Memoria integrata (Session State) che permette al chatbot di ricordare i messaggi precedenti durante la singola sessione.

Parametri Dinamici: Sidebar interattiva per la regolazione della "Temperature", che permette all'utente di bilanciare la precisione e la creatività del modello.

Isolamento del Dominio: System prompt customizzato per garantire che l'assistente rimanga nel proprio ruolo e risponda solo a temi pertinenti all'azienda.

Predisposizione RAG: Infrastruttura di base già configurata per l'integrazione e l'interrogazione di documenti proprietari.

## 🛠 Stack tecnologico

<!-- TODO: tecnologie usate con descrizione breve -->
| Tecnologia | Uso |
|------------|-----|
| Claude Haiku | Motore LLM (Large Language Model) veloce ed efficiente per la generazione e la comprensione del linguaggio naturale. |
| ChromaDB | Database vettoriale locale per l'archiviazione e il recupero semantico delle informazioni (Retrieval). |
| Streamlit | Framework Python per lo sviluppo e il deploy rapido dell'interfaccia grafica (Frontend). |
|PyPDF & Sentence-Transformers | Strumenti per l'estrazione del testo dai documenti e la generazione degli embedding vettoriali.|

## 📐 Architettura

<!-- TODO: descrizione del flusso RAG + tool in 3-4 righe -->
L'applicazione si basa su un flusso client-server leggero orchestrato tramite Streamlit. L'input dell'utente viene intercettato dalla UI, arricchito con il System Prompt aziendale e lo storico della chat, per poi essere inviato tramite chiamata API al modello Anthropic Claude. L'architettura è progettata in ottica RAG (Retrieval-Augmented Generation): l'inclusione di ChromaDB e modelli di embedding pone le basi per un imminente aggancio a una knowledge base documentale (es. manuali IoT, report), permettendo al LLM di generare risposte basate su dati vettorializzati e recuperati in tempo reale

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
