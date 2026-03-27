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
