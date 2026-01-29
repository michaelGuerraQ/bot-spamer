# bot-spamer (Telegram – Telethon)

Bot desarrollado en **Python** usando **Telethon** para automatizar tareas de mensajería en Telegram,
incluyendo **respuestas automáticas en privado** y **publicaciones programadas en grupos/canales**.

> ⚠️ Nota importante  
> Este proyecto es de carácter **educativo y administrativo**.  
> Debe utilizarse únicamente en chats, grupos o canales donde el usuario tenga **permiso explícito** para interactuar.

---

## 🚀 Funcionalidades principales

### 🤖 Respuesta automática en mensajes privados
- Detecta mensajes entrantes por **chat privado**.
- Envía una **respuesta automática** con:
  - Imagen
  - Texto formateado (HTML)
  - Enlaces de contacto (WhatsApp / Telegram)
- Responde **una sola vez por usuario**, evitando spam.
- Guarda los usuarios respondidos en un archivo local (`respondidos.txt`).

---

### 📣 Publicación automática en grupos y canales
- Obtiene la lista de grupos/canales donde la cuenta tiene permiso para enviar mensajes.
- Publica mensajes y/o contenido multimedia de forma automática.
- Permite:
  - Límites de mensajes por grupo
  - Delays aleatorios entre mensajes
  - Pausas largas entre rondas de envío
- Incluye **modos de seguridad** para reducir riesgos:
  - `pruebas`
  - `normal`
  - `seguro`

---

### ⏱️ Control de velocidad y protección
- Cooldown por grupo para evitar envíos repetidos.
- Manejo de errores comunes:
  - `FloodWaitError`
  - `ForbiddenError`
- Exclusión de grupos por nombre o restricción automática.

---

### 🔐 Inicio de sesión seguro
- Login mediante **QR Code** (no requiere bot token).
- Soporte para cuentas con **2FA**.

---

## 🛠️ Tecnologías usadas
- Python 3
- Telethon
- asyncio
- python-dotenv
- qrcode
- logging

---

## 📦 Instalación
## Instalación y ejecución

# Bot de Telegram - Configuración y Uso

Este proyecto requiere **Python 3.10** o superior y una cuenta de Telegram activa.

## 🛠️ Instalación y Configuración

1. **Obtener Credenciales:**
   - Regístrate en [my.telegram.org](https://my.telegram.org).
   - Ve a **API development tools** para obtener tu `API_ID` y `API_HASH`.

2. **Preparar el entorno:**
   - **Crear entorno virtual:**
     - Windows: `python -m venv venv`
     - Linux/Mac: `python3 -m venv venv`
   - **Activar entorno:**
     - Windows: `venv\Scripts\activate`
     - Linux/Mac: `source venv/bin/activate`
   - **Instalar dependencias:**
     ```bash
     pip install -r requirements.txt
     ```

3. **Configurar variables:**
   Crea un archivo `.env` en la raíz del proyecto (no lo subas al repositorio) con el siguiente formato:
   ```text
   API_ID=tu_api_id
   API_HASH=tu_api_hash
