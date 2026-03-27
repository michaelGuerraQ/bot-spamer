<p align="center">
  <img src="https://img.shields.io/badge/Telegram-Spamer%20Bot-2AABEE?style=for-the-badge&logo=telegram&logoColor=white" />
</p>

<h1 align="center">🤖📣 Bot Spamer para Telegram (Telethon)</h1>

<p align="center">
  Automatización avanzada de mensajería en Telegram usando <strong>Python + Telethon</strong><br>
  Respuestas automáticas en privado y publicaciones programadas en grupos/canales
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Telethon-Telegram%20Client-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Automatización-Mensajería-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Estado-Activo-success?style=flat-square" />
</p>

---

> ⚠️ **Aviso importante**
>
> Este proyecto es de carácter **educativo y administrativo**.  
> Debe utilizarse únicamente en grupos o chats donde tengas **permiso para interactuar**.

---

## 📌 Descripción

Este bot permite automatizar publicaciones de ventas o difusión dentro de Telegram utilizando una **cuenta real**, no un bot tradicional.

El sistema inicia sesión mediante **QR Code** y trabaja directamente con la sesión del usuario.  
Una vez autenticado, puede:

- enviar publicaciones automáticamente en grupos donde la cuenta ya está agregada
- trabajar en **bucle continuo**
- respetar tiempos de espera configurados para reducir riesgos de restricciones
- responder mensajes privados de forma automática
- guardar los usuarios ya respondidos en un archivo local para no repetir respuestas

---

## 🚀 Funcionalidades principales

### 📣 Difusión automática de publicaciones
- Usa una cuenta real de Telegram iniciada por sesión
- Toma un mensaje o publicación previamente configurada
- Detecta los grupos donde la cuenta está agregada
- Envía la publicación de forma automática
- Puede trabajar en **bucle continuo**
- Incluye pausas y delays entre envíos

### 🤖 Respuesta automática en mensajes privados
- Detecta mensajes entrantes por **chat privado**
- Envía una respuesta automática configurada
- Puede incluir:
  - texto
  - imagen
  - enlaces
  - formato HTML

### 💾 Control de usuarios ya respondidos
Para evitar responder varias veces al mismo usuario, el bot guarda los IDs en un archivo local:

```text
respondidos.txt

Funcionamiento:

Usuario escribe por primera vez → el bot responde y guarda su ID
Si vuelve a escribir → el bot detecta el ID y no responde otra vez

Ejemplo:

123456789
987654321
456789123

✔ Evita spam
✔ Controla la interacción

⏱️ Seguridad y control
Delays configurables
Pausas entre ciclos
Manejo de errores:
FloodWaitError
ForbiddenError
Exclusión de grupos problemáticos
🔐 Inicio de sesión por QR
No usa bot token
Se conecta con una cuenta real
Genera un QR en la terminal
Se escanea desde Telegram
Compatible con 2FA
🧠 Flujo del sistema

Difusión:

Mensaje base
   ↓
Obtiene grupos
   ↓
Envía mensajes
   ↓
Espera tiempo
   ↓
Repite en bucle

Respuesta automática:

Usuario escribe
   ↓
Bot detecta mensaje
   ↓
Revisa respondidos.txt
   ↓
¿Ya respondió?
   ├─ Sí → no responde
   └─ No → responde y guarda ID
🛠️ Tecnologías
Python 3
Telethon
asyncio
python-dotenv
qrcode
logging
📦 Instalación
git clone https://github.com/michaelGuerraQ/bot-spamer.git
cd bot-spamer
pip install -r requirements.txt
🔑 Credenciales Telegram
Ir a https://my.telegram.org
Entrar con tu número
Ir a API development tools
Obtener:
API_ID
API_HASH
⚙️ Configuración

Crear archivo .env:

API_ID=tu_api_id
API_HASH=tu_api_hash
▶️ Ejecución
python main.py
📱 Login con QR

Al ejecutar:

Se genera un QR en la terminal
Lo escaneas desde Telegram
Se inicia sesión
El bot comienza a trabajar

Flujo:

Ejecutas bot
   ↓
Sale QR en terminal
   ↓
Escaneas con Telegram
   ↓
Sesión iniciada
   ↓
Bot activo
📂 Estructura
bot-spamer/
├── main.py
├── .env
├── respondidos.txt
├── requirements.txt
└── sessions/
✅ Casos de uso
Difusión de promociones
Automatización de ventas
Atención automática en Telegram
Gestión de comunidades
👨‍💻 Autor

Michael Stuward Guerra Quispe
🔗 https://github.com/michaelGuerraQ

<p align="center"> 🚀 Automatiza inteligentemente, no satures </p> ```
