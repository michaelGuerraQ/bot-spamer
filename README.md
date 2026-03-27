<p align="center">
  <img src="https://img.shields.io/badge/Telegram-Auto%20Bot-2AABEE?style=for-the-badge&logo=telegram&logoColor=white" />
</p>

<h1 align="center">🤖 Telegram Auto Messenger Bot (Telethon)</h1>

<p align="center">
Automatiza mensajes, difusión de contenido y respuestas privadas usando <b>Python + Telethon</b><br>
Diseñado para ventas, marketing y gestión de comunidades
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Telethon-Telegram%20Client-blue" />
  <img src="https://img.shields.io/badge/Asyncio-Enabled-green" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

---

## ⚠️ Disclaimer

Este proyecto es solo para **uso educativo y automatización responsable**.  
No debe utilizarse para spam no autorizado o actividades que violen las políticas de Telegram.

---

## 📌 Overview

Este bot funciona usando una **cuenta real de Telegram (no bot token)** y permite automatizar:

- 📣 Envío masivo de publicaciones en grupos  
- 🤖 Respuestas automáticas en chats privados  
- 🔁 Ejecución en bucle continuo  
- ⏱️ Control de tiempos para evitar restricciones  
- 💾 Registro de usuarios ya atendidos  

---

## ✨ Features

### 📣 Auto Broadcast

- Detecta automáticamente los grupos donde estás  
- Envía mensajes programados  
- Soporta texto, links e imágenes  
- Delay configurable entre envíos  
- Ejecución continua (loop infinito)  

---

### 🤖 Auto Reply (DM)

- Detecta mensajes privados entrantes  
- Responde automáticamente  
- Compatible con:
  - texto  
  - HTML  
  - enlaces  
  - imágenes  

---

### 💾 Smart User Tracking

Evita responder múltiples veces al mismo usuario:

```txt
respondidos.txt
```

✔ Guarda IDs automáticamente  
✔ Evita spam innecesario  
✔ Mejora control de interacción  

---

### 🔐 Login con QR

- No usa bot token  
- Login mediante QR Code  
- Compatible con 2FA  
- Sesión persistente  

---

## 🧠 Workflow

### 🔄 Broadcasting

```
Mensaje base
   ↓
Obtiene grupos
   ↓
Envía mensaje
   ↓
Espera delay
   ↓
Repite
```

---

### 💬 Auto Reply

```
Usuario escribe
   ↓
Verifica respondidos.txt
   ↓
¿Ya respondió?
   ├─ Sí → Ignora
   └─ No → Responde + Guarda ID
```

---

## 🛠️ Tech Stack

- Python 3  
- Telethon  
- asyncio  
- python-dotenv  
- logging  
- qrcode  

---

## 📦 Installation

```bash
git clone https://github.com/michaelGuerraQ/bot-spamer.git
cd bot-spamer
pip install -r requirements.txt
```

---

## 🔑 Telegram API Setup

1. Ir a: https://my.telegram.org  
2. Iniciar sesión con tu número  
3. Entrar a: **API Development Tools**  
4. Obtener:

```
API_ID
API_HASH
```

---

## ⚙️ Configuration

Crear archivo `.env`:

```env
API_ID=tu_api_id
API_HASH=tu_api_hash
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📱 Login

1. Ejecutas el bot  
2. Se genera QR en terminal  
3. Escaneas desde Telegram  
4. Sesión iniciada  
5. Bot activo 🚀  

---

## 📂 Project Structure

```
bot-spamer/
├── main.py
├── .env
├── respondidos.txt
├── requirements.txt
└── sessions/
```

---

## 🧩 Use Cases

- Marketing digital en Telegram  
- Automatización de ventas  
- Atención automática  
- Gestión de comunidades  

---

## 🚧 Roadmap

- [ ] Panel web (React)  
- [ ] Dashboard de métricas  
- [ ] Filtros por tipo de grupo  
- [ ] Integración con IA  
- [ ] Multi cuenta  

---

## 👨‍💻 Author

**Michael Stuward Guerra Quispe**

🔗 https://github.com/michaelGuerraQ  

---

<p align="center">
🚀 Automatiza con inteligencia, no hagas spam
</p>
