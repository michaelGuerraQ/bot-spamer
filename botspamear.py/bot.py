from telethon.sync import TelegramClient
from telethon import events
import asyncio
from telethon.errors import FloodWaitError, ForbiddenError
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE")
session_name = "a"

MAX_MENSAJES_POR_GRUPO = 8
grupos_restringidos = []

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    groups_info.append({'group_id': dialog.id, 'group_name': dialog.title})
        return groups_info
    except Exception as e:
        print("Error obteniendo lista de grupos:", e)
        return []

async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id, limit=20):
            if message.message or message.media:
                all_messages.append(message)
        return all_messages
    except Exception as e:
        print(f"Error obteniendo mensajes del grupo: {e}")
        return []

async def logUserBot():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        code = input("📲 Ingresa el código de verificación: ")
        await client.sign_in(phone_number, code)

    await client.send_message("@botametugampi", f'<b>Bot encendido</b>', parse_mode="HTML")

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        if event.is_private:
            try:
                sender = await event.get_sender()
                if not sender.bot:
                    await event.respond(
                        "Hola 👋\n\n"
                        "Soy el bot oficial de @MindsCodeTech (antes Asistente Dark).\n"
                        "📢 Muy pronto migraré a 👉 @MindsCodeTe\n\n"
                        "Para más información escribir 👉 @MindsCodeTe\n"
                        "O también por WhatsApp: https://wa.me/51998998179\n\n"
                        "⚠️ Este número no responderá mensajes personalizados. ¡Guarda el nuevo contacto!"
                    )
            except FloodWaitError as e:
                print(f"Flood en handler: esperando {e.seconds} segundos")
                await asyncio.sleep(e.seconds)

    spammer_group = -4760995905

    async def spam_loop():
        while True:
            groups_info = await getListOfGroups(client)
            messages_list = await getMessagesFromGroup(client, spammer_group)

            for i in groups_info:
                if i["group_id"] in grupos_restringidos:
                    continue

                nombres_excluidos = [
                    "bot spam-Dark", "RESPALDO🇵🇪BINS PERU", "➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧", "QUEMANDO ESTAFADORES",
                    "𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀", "Referencias Elmer 💸", "🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪", "TU MARKETPLACE",
                    "⚫️𝙈𝙀𝙍𝘾𝘼𝘿𝙊 𝙉𝙀𝙂𝙍𝙊⚫️", "💻 BLAK PERU OFC COMUNITY 💻", "🇵🇪PRIMITOS BINS PERU🇵🇪",
                    "CHAT ACCESO X", "𝔹𝕃𝔸𝕂_𝔻𝔸𝕋𝔸_𝕏 ~ CHAT", "𝘾𝘼𝙇𝙀𝙏𝘼𝙎 𝙇𝙄𝙈𝘼😍", "🇪🇸 Xiaomi Redmi Note 9S / 9 PRO 🇪🇸",
                    "Smart Fit Peru"
                ]

                if i["group_name"] in nombres_excluidos:
                    continue

                for j, message_spam in enumerate(messages_list):
                    if j == MAX_MENSAJES_POR_GRUPO:
                        break
                    try:
                        await client.send_message(i["group_id"], message_spam)
                        await client.send_message("@botametugampi", f'<b>Mensaje enviado a {i["group_name"]}</b>', parse_mode="HTML")

                    except FloodWaitError as e:
                        await client.send_message("@botametugampi", f"<b>FloodWait</b>: esperando {e.seconds} segundos...", parse_mode="HTML")
                        await asyncio.sleep(e.seconds)

                    except ForbiddenError as e:
                        if "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e):
                            try:
                                if message_spam.message:
                                    await client.send_message(i["group_id"], message_spam.message)
                                    await client.send_message("@botametugampi", f"Solo texto enviado a {i['group_name']}", parse_mode="HTML")
                                else:
                                    await client.send_message("@botametugampi", f"Multimedia prohibida y sin texto en {i['group_name']}", parse_mode="HTML")
                            except ForbiddenError as e2:
                                if "CHAT_SEND_PLAIN_FORBIDDEN" in str(e2):
                                    await client.send_message("@botametugampi", f"No se permite ni texto en {i['group_name']}, será excluido.", parse_mode="HTML")
                                    grupos_restringidos.append(i["group_id"])
                        elif "CHAT_SEND_PLAIN_FORBIDDEN" in str(e):
                            await client.send_message("@botametugampi", f"No se permite texto en {i['group_name']}, será excluido.", parse_mode="HTML")
                            grupos_restringidos.append(i["group_id"])
                        else:
                            await client.send_message("@botametugampi", f"Error de envío a {i['group_name']}: {e}", parse_mode="HTML")
                            grupos_restringidos.append(i["group_id"])

                    except Exception as error:
                        await client.send_message("@botametugampi", f"Error inesperado en {i['group_name']}: {error}", parse_mode="HTML")
                        grupos_restringidos.append(i["group_id"])

                    await asyncio.sleep(10)

            await client.send_message("@botametugampi", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(600)

    asyncio.create_task(spam_loop())
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(logUserBot())
