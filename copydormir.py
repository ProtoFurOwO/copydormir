from telethon import TelegramClient, events
from metaapi_cloud_sdk import MetaApi
import asyncio
import os

# Credenciales de Telegram
api_id = '27176651'
api_hash = 'e346bb5a6e34c15ccfe9f40cbb757286'


# Credenciales de MetaAPI
META_API_TOKEN = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIyMmIyOTU2Y2U4YjgwM2UzNGEwMjhjZGI5NjNmODQzOSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6ImJpbGxpbmctYXBpIiwibWV0aG9kcyI6WyJiaWxsaW5nLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19XSwiaWdub3JlUmF0ZUxpbWl0cyI6ZmFsc2UsInRva2VuSWQiOiIyMDIxMDIxMyIsImltcGVyc29uYXRlZCI6ZmFsc2UsInJlYWxVc2VySWQiOiIyMmIyOTU2Y2U4YjgwM2UzNGEwMjhjZGI5NjNmODQzOSIsImlhdCI6MTczNDEzOTc1NH0.J2SsBND25yfDR7EsS4lin0Tuz6nABn3t4pIdLFDeDhBldmy9INHs9328r9rQ7f2pbJ_ClTD1F1xyUBogBuILq4Tu4BW82d79WWssLyT-QV0ewYuGXhvmQqWiAwunKIkB8Y1t7lTXZY-8m-ULUCO7m-XVSpnAT15LuLN27XtZ5j2xVgAvIMDy_rxjtj9iuUXJGoeUxXz_L6f3CHJk49MQjDqqHOeJuoZigUoRh2vUKUgjYtXOo_T7Hw-Cs9Is6tIZuAHBNpnB_dAt7NZpH6nD3qoyVRwcllqWhIpX_9PQvPEQPfA_FGvDCTHDA5qbbY8iC0KS0_5NkwUis3iuGAKS1qvIWYYGYdwBKtM2epvDSmYJDkixd36Oc_p3_VXFRrlXLOEiwuVmTtqJt4aiQzyBdmDqOrqtLwdorqmHrVdxhyq3xEKDlN8x289ig1wpDe1WDMXe9TyBNO0d7t1wXVG-bm-3Bh0JHpQX_uSghRz2P6qeus_5ChYMFHfBtDgHXUY8RGKNV22P4FcmKrHxxPYjNL2oA3E4A85v5rT-hn1Kp0i2tIiBgqP7LaMvTt9Y7PwJ5o0Kkx1G4j0Dg8n0NcAQ5RAYveiKjDhgyekU3USdoqhs0gFkQxuQvQ1uNk2lPINeLkEpI_V2KKdFuvEk5I_k0LsJtMAo4-Tq_llQ-FW7JTw'
ACCOUNT_ID = '16027ab7-b074-4fd4-b784-048910037d44'

# Nombre del cliente Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def check_connection():
    try:
        me = await client.get_me()
        print(f"Connected as: {me.username}")
        
        channel = await client.get_entity('@Gary_TheTrader')
        print(f"Channel found: {channel.title}")
        
        # Intentar obtener algunos mensajes
        messages = await client.get_messages(channel, limit=1)
        print(f"Can fetch messages: {bool(messages)}")
        
    except Exception as e:
        print(f"Connection check failed: {e}")



async def get_last_message():
    async with client:
        channel = await client.get_entity('@Gary_TheTrader')
        messages = await client.get_messages(channel, limit=1)
        if messages:
            print("\nÚltimo mensaje en el canal (confirmación de conexión):")
            print("-" * 50)
            print(messages[0].text)
            print("-" * 50)
            print("Bot iniciado y listo para recibir nuevas señales...\n")

async def place_trade(api, action, symbol, entry, sl, tp1, tp2, volume=0.01):
    try:
        # Conectar a la cuenta de trading
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        await account.wait_connected()
        
        # Obtener API de trading
        connection = account.get_rpc_connection()
        await connection.connect()
        await connection.wait_synchronized()

        # Obtener el precio actual
        price_info = await connection.get_symbol_price(symbol)
        current_price = price_info['ask'] if action.lower() == 'buy' else price_info['bid']

        # Extraer rango de entrada
        entry_range = [float(x.strip()) for x in str(entry).split('-')] if '-' in str(entry) else [float(entry), float(entry)]
        entry_min, entry_max = entry_range

        print(f"Precio actual: {current_price}")
        print(f"Rango objetivo: {entry_min} - {entry_max}")
        print(f"SL: {sl}")
        print(f"TP1: {tp1}")
        if tp2:
            print(f"TP2: {tp2}")

        # Validar stops para SELL
        if action.lower() == 'sell':
            if sl <= current_price or tp1 >= current_price:
                raise ValueError("Para SELL: SL debe estar arriba del precio y TP debe estar abajo")
        # Validar stops para BUY
        else:
            if sl >= current_price or tp1 <= current_price:
                raise ValueError("Para BUY: SL debe estar abajo del precio y TP debe estar arriba")

        if entry_min <= current_price <= entry_max:
            # Si el precio está en el rango, crear orden de mercado
            print("Creando orden de mercado...")
            order_function = connection.create_market_buy_order if action.lower() == 'buy' else connection.create_market_sell_order
            
            # Colocar orden de mercado
            result = await order_function(
                symbol,
                volume,
                sl,
                tp1,
                {'comment': 'Signal from Telegram'}
            )
        else:
            # Determinar si usar limit o stop
            if action.lower() == 'buy':
                if current_price < entry_min:
                    print("Creando orden buy limit...")
                    order_function = connection.create_limit_buy_order
                    entry_price = entry_min
                else:
                    print("Creando orden buy stop...")
                    order_function = connection.create_stop_buy_order
                    entry_price = entry_max
            else:  # sell
                if current_price > entry_max:
                    print("Creando orden sell limit...")
                    order_function = connection.create_limit_sell_order
                    entry_price = entry_max
                else:
                    print("Creando orden sell stop...")
                    order_function = connection.create_stop_sell_order
                    entry_price = entry_min

            # Colocar orden pendiente
            result = await order_function(
                symbol,
                volume,
                entry_price,
                sl,
                tp1,
                {'comment': 'Signal from Telegram'}
            )

        # Colocar la orden principal
        if entry_min <= current_price <= entry_max:
            # Orden de mercado
            result = await order_function(
                symbol,
                volume,
                sl,
                tp1,
                {'comment': 'Signal from Telegram'}
            )
        else:
            # Orden limit o stop
            result = await order_function(
                symbol,
                volume,
                entry_price,
                sl,
                tp1,
                {'comment': 'Signal from Telegram'}
            )

        # Si hay TP2, crear una orden adicional
        if tp2:
            additional_volume = volume / 2
            if entry_min <= current_price <= entry_max:
                # Orden de mercado para TP2
                result2 = await order_function(
                    symbol,
                    additional_volume,
                    sl,
                    tp2,
                    {'comment': 'Signal from Telegram TP2'}
                )
            else:
                # Orden limit o stop para TP2
                result2 = await order_function(
                    symbol,
                    additional_volume,
                    entry_price,
                    sl,
                    tp2,
                    {'comment': 'Signal from Telegram TP2'}
                )

        print(f"Orden ejecutada: {result}")
        return result

    except Exception as e:
        print(f"Error al colocar la orden: {e}")
        return None
    
async def process_signal(api, text):
    text_lower = text.lower()
    
    is_gold = 'gold' in text_lower or 'xauusd' in text_lower
    is_xrp = 'xrp' in text_lower or 'xrpusd' in text_lower

    if (is_gold or is_xrp) and ('sell' in text_lower or 'buy' in text_lower):
        print(f"Mensaje detectado: {text}")
        
        symbol = 'XAUUSD' if is_gold else 'XRPUSD'
        
        lines = text.split('\n')
        action = None
        entry = None
        sl = None
        tp1 = None
        tp2 = None
        
        for line in lines:
            if 'sell' in line.lower():
                action = 'sell'
                # Extraer el rango de entrada después del @
                entry_part = line.split('@')[1].strip() if '@' in line else None
                entry = entry_part
            elif 'buy' in line.lower():
                action = 'buy'
                # Extraer el rango de entrada después del @
                entry_part = line.split('@')[1].strip() if '@' in line else None
                entry = entry_part
            elif 'sl:' in line.lower():
                sl = float(line.split(':')[1].strip())
            elif 'tp1:' in line.lower():
                tp1 = float(line.split(':')[1].strip())
            elif 'tp2:' in line.lower():
                tp2 = float(line.split(':')[1].strip())

        if action and entry and sl and tp1:
            print(f"Ejecutando orden: {action} {symbol} @ {entry}")
            await place_trade(api, action, symbol, entry, sl, tp1, tp2)

async def start_telegram_client(api):
    @client.on(events.NewMessage(chats='@Gary_TheTrader'))
    async def handler(event):
        text = event.message.text
        if text:
            await process_signal(api, text)

    await client.start()
    print("Cliente de Telegram iniciado. Escuchando mensajes...")
    await client.run_until_disconnected()

async def main():
    # Añadir al inicio de main()
    await check_connection()
    
    try:
        print("Iniciando MetaAPI...")
        api = MetaApi(META_API_TOKEN)

        print("Iniciando cliente de Telegram...")
        # Primero obtener el último mensaje solo como confirmación
        await client.start()
        await get_last_message()

        # Luego iniciar la escucha de nuevos mensajes
        await start_telegram_client(api)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        raise e

if __name__ == "__main__":
    # Crear y ejecutar el bucle de eventos
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Programa terminado por el usuario")
    finally:
        loop.close()
        
