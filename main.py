import pymem
import pymem.process
import time
import ctypes
import logging
from requests import get

ctypes.windll.kernel32.SetConsoleTitleW("CS2 NoFlash Script | ItsJesewe")

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetch offsets and client data
def fetch_offsets():
    try:
        offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
        client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client.dll.json").json()
        return offset, client
    except Exception as e:
        logging.error(f"Failed to fetch offsets: {e}")
        return None, None

def initialize_pymem():
    try:
        pm = pymem.Pymem("cs2.exe")
        client_module = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        return pm, client_module
    except pymem.exception.ProcessNotFound:
        logging.error('cs2.exe process is not running!')
    except pymem.exception.ProcessError:
        logging.error('Error accessing process cs2.exe')
    except pymem.exception.MemoryReadError:
        logging.error('Error reading memory')
    except pymem.exception.MemoryWriteError:
        logging.error('Error writing memory')
    except AttributeError:
        logging.error('Byte pattern not found')
    return None, None

def noflash_loop(pm, client_module, dwLocalPlayerPawn, m_flFlashMaxAlpha):
    try:
        while True:
            player_position = pm.read_longlong(client_module + dwLocalPlayerPawn)
            if player_position:
                pm.write_float(player_position + m_flFlashMaxAlpha, 0.0)
            time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("NoFlash script terminated by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def main():
    logging.info("Fetching offsets and client data...")
    offsets, client = fetch_offsets()
    if not offsets or not client:
        return

    global dwLocalPlayerPawn, m_flFlashMaxAlpha
    dwLocalPlayerPawn = offsets["client.dll"]["dwLocalPlayerPawn"]
    m_flFlashMaxAlpha = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]

    logging.info("Searching for cs2.exe process...")
    pm, client_module = initialize_pymem()
    if not pm or not client_module:
        return

    logging.info("cs2.exe is running.")
    noflash_loop(pm, client_module, dwLocalPlayerPawn, m_flFlashMaxAlpha)

if __name__ == "__main__":
    main()