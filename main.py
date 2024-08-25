import pymem
import pymem.process
import time
import logging
from requests import get
from packaging import version
from colorama import init, Fore
import json
import os
import ctypes

# Initialize colorama for colored console output
init(autoreset=True)

class Logger:
    """Handles logging setup for the application."""
    
    LOG_DIRECTORY = os.path.expandvars(r'%LOCALAPPDATA%\Requests\ItsJesewe\crashes')
    LOG_FILE = os.path.join(LOG_DIRECTORY, 'nf_logs.log')

    @staticmethod
    def setup_logging():
        """Set up the logging configuration."""
        os.makedirs(Logger.LOG_DIRECTORY, exist_ok=True)
        with open(Logger.LOG_FILE, 'w') as f:
            pass
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s: %(message)s',
            handlers=[logging.FileHandler(Logger.LOG_FILE), logging.StreamHandler()]
        )

class Utility:
    """Contains utility functions for the application."""

    CACHE_DIRECTORY = os.path.expandvars(r'%LOCALAPPDATA%\Requests\ItsJesewe')
    CACHE_FILE = os.path.join(CACHE_DIRECTORY, 'offsets_cache.json')
    
    @staticmethod
    def set_console_title(title):
        """Sets the console window title."""
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    @staticmethod
    def fetch_offsets():
        """Fetches offsets and client data from remote sources or local cache."""
        try:
            response_offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json")
            response_client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json")
            
            if response_offset.status_code != 200 or response_client.status_code != 200:
                logging.error(f"{Fore.RED}Failed to fetch offsets from server.")
                return None, None

            offset = response_offset.json()
            client = response_client.json()

            if os.path.exists(Utility.CACHE_FILE):
                with open(Utility.CACHE_FILE, 'r') as f:
                    cached_data = json.load(f)
                
                if cached_data.get('offsets') != offset or cached_data.get('client') != client:
                    logging.info(f"{Fore.YELLOW}Offsets have changed, updating cache...")
                    with open(Utility.CACHE_FILE, 'w') as f:
                        json.dump({'offsets': offset, 'client': client}, f)
                else:
                    logging.info(f"{Fore.CYAN}Using cached offsets.")
                    return cached_data['offsets'], cached_data['client']
            else:
                os.makedirs(Utility.CACHE_DIRECTORY, exist_ok=True)
                with open(Utility.CACHE_FILE, 'w') as f:
                    json.dump({'offsets': offset, 'client': client}, f)

            return offset, client
        except Exception as e:
            logging.error(f"{Fore.RED}Failed to fetch offsets: {e}")
            logging.error(f"{Fore.RED}Please report this issue on the GitHub repository: https://github.com/Jesewe/cs2-noflash/issues")
            return None, None

    @staticmethod
    def check_for_updates(current_version):
        """Checks for software updates on GitHub."""
        try:
            response = get("https://api.github.com/repos/Jesewe/cs2-noflash/tags")
            response.raise_for_status()
            latest_version = response.json()[0]["name"]
            if version.parse(latest_version) > version.parse(current_version):
                logging.warning(f"{Fore.YELLOW}New version available: {latest_version}. Please update for the latest fixes and features.")
            else:
                logging.info(f"{Fore.GREEN}You are using the latest version.")
        except Exception as e:
            logging.error(f"{Fore.RED}Error checking for updates: {e}")

class PymemHandler:
    """Handles interaction with the game process using pymem."""

    def __init__(self, process_name="cs2.exe"):
        self.pm = None
        self.client_base = None
        self.process_name = process_name

    def initialize_pymem(self):
        """Initializes Pymem and attaches to the game process."""
        try:
            self.pm = pymem.Pymem(self.process_name)
        except pymem.exception.PymemError as e:
            logging.error(f"{Fore.RED}Could not open {self.process_name}: {e}")
            return False
        return True

    def get_client_module(self, module_name="client.dll"):
        """Retrieves the client.dll module base address."""
        client_module = pymem.process.module_from_name(self.pm.process_handle, module_name)
        if not client_module:
            logging.error(f"{Fore.RED}Could not find {module_name} module.")
            return False
        self.client_base = client_module.lpBaseOfDll
        return True

class NoFlashScript:
    """Main class for the CS2 NoFlash functionality."""
    
    VERSION = "v1.0.7"

    def __init__(self):
        """Initializes the NoFlashScript with necessary attributes."""
        self.pymem_handler = PymemHandler()
        self.dwLocalPlayerPawn = None
        self.m_flFlashMaxAlpha = None
        self.is_running = False

    def start(self):
        """Starts the main loop of the NoFlashScript."""
        Utility.set_console_title(f"CS2 NoFlash {self.VERSION}")
        Utility.check_for_updates(self.VERSION)
        logging.info(f"{Fore.CYAN}Fetching offsets and client data...")

        offsets, client_data = Utility.fetch_offsets()
        if offsets is None or client_data is None:
            input(f"{Fore.RED}Press Enter to exit...")
            return

        # Set offsets and client data
        self.dwLocalPlayerPawn = offsets["client.dll"]["dwLocalPlayerPawn"]
        self.m_flFlashMaxAlpha = client_data["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]
        
        logging.info(f"{Fore.CYAN}Searching for cs2.exe process...")
        if not self.pymem_handler.initialize_pymem():
            input(f"{Fore.RED}Press Enter to exit...")
            return

        if not self.pymem_handler.get_client_module():
            input(f"{Fore.RED}Press Enter to exit...")
            return

        logging.info(f"{Fore.GREEN}NoFlash script started.")
        self.is_running = True
        self.run_noflash_loop()

    def run_noflash_loop(self):
        """Runs the main loop of the NoFlash script."""
        try:
            while self.is_running:
                player_position = self.pymem_handler.pm.read_longlong(self.pymem_handler.client_base + self.dwLocalPlayerPawn)
                if player_position:
                    self.pymem_handler.pm.write_float(player_position + self.m_flFlashMaxAlpha, 0.0)
                time.sleep(0.1)
        except KeyboardInterrupt:
            logging.info(f"{Fore.YELLOW}NoFlash script terminated by user.")
            self.is_running = False
        except Exception as e:
            logging.error(f"{Fore.RED}Unexpected error: {e}")
            input(f"{Fore.RED}Press Enter to exit...")

if __name__ == '__main__':
    Logger.setup_logging()
    noflash = NoFlashScript()
    noflash.start()