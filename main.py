import pymem
import pymem.process
import time
import logging
from requests import get
from packaging import version

VERSION = "v1.0.6"

def fetch_offsets():
    try:
        offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
        client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()
        return offset, client
    except Exception as e:
        logging.error(f"Failed to fetch offsets: {e}")
        return None, None

def initialize_pymem():
    try:
        pm = pymem.Pymem("cs2.exe")
        return pm
    except pymem.exception.PymemError as e:
        logging.error(f"Could not open cs2.exe: {e}")
        return None

def check_for_updates():
    try:
        response = get("https://api.github.com/repos/Jesewe/cs2-noflash/tags")
        response.raise_for_status()
        latest_version = response.json()[0]["name"]
        if version.parse(latest_version) > version.parse(VERSION):
            logging.info(f"New version available: {latest_version}. Please update for the latest fixes and features.")
        else:
            logging.info("You are using the latest version.")
    except Exception as e:
        logging.error(f"Error checking for updates: {e}")

def get_client_module(pm):
    client_module = pymem.process.module_from_name(pm.process_handle, "client.dll")
    if not client_module:
        logging.error("Could not find client.dll module.")
        return None
    return client_module.lpBaseOfDll

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
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    check_for_updates()
    logging.info("Fetching offsets and client data...")
    offsets, client_data = fetch_offsets()
    if offsets is None or client_data is None:
        return

    global dwLocalPlayerPawn, m_flFlashMaxAlpha
    dwLocalPlayerPawn = offsets["client.dll"]["dwLocalPlayerPawn"]
    m_flFlashMaxAlpha = client_data["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]

    logging.info("Searching for cs2.exe process...")
    pm = initialize_pymem()
    if pm is None:
        return

    client_base = get_client_module(pm)
    if client_base is None:
        return

    logging.info("cs2.exe is running.")
    noflash_loop(pm, client_base, dwLocalPlayerPawn, m_flFlashMaxAlpha)

if __name__ == "__main__":
    main()