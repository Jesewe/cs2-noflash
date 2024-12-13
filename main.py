import pymem, pymem.process, time, logging, os, ctypes
from requests import get
from packaging import version
from colorama import init, Fore

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
            format='[%(asctime)s %(levelname)s]: %(message)s',
            handlers=[logging.FileHandler(Logger.LOG_FILE), logging.StreamHandler()]
        )

class Utility:
    """Contains utility functions for the application."""
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

            return offset, client
        except Exception as e:
            logging.error(f"{Fore.RED}Failed to fetch offsets: {e}")
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
            elif version.parse(current_version) > version.parse(latest_version):
                logging.info(f"{Fore.YELLOW}Developer version: You are using a pre-release or developer version.")
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
            self.pm = pymem.Pymem("cs2.exe")
            logging.info(f"{Fore.GREEN}Successfully attached to cs2.exe process.")
        except pymem.exception.ProcessNotFound:
            logging.error(f"{Fore.RED}Could not find cs2.exe process. Please make sure the game is running.")
        except pymem.exception.PymemError as e:
            logging.error(f"{Fore.RED}Pymem encountered an error: {e}")
        except Exception as e:
            logging.error(f"{Fore.RED}Unexpected error during Pymem initialization: {e}")
        return self.pm is not None

    def get_client_module(self):
        """Retrieves the client.dll module base address."""
        try:
            if self.client_base is None:
                client_module = pymem.process.module_from_name(self.pm.process_handle, "client.dll")
                if not client_module:
                    raise pymem.exception.ModuleNotFoundError("client.dll not found")
                self.client_base = client_module.lpBaseOfDll
                logging.info(f"{Fore.GREEN}client.dll module found at {hex(self.client_base)}.")
        except pymem.exception.ModuleNotFoundError as e:
            logging.error(f"{Fore.RED}Error: {e}. Ensure client.dll is loaded.")
        except Exception as e:
            logging.error(f"{Fore.RED}Unexpected error retrieving client module: {e}")
        return self.client_base is not None

class NoFlashScript:
    """Main class for the CS2 NoFlash functionality."""
    
    VERSION = "v1.0.8"

    def __init__(self):
        """Initializes the NoFlashScript with necessary attributes."""
        self.pymem_handler = PymemHandler()
        self.dwLocalPlayerPawn = None
        self.m_flFlashDuration = None
        self.is_running = False

    def start(self):
        """Starts the main loop of the NoFlashScript."""
        Utility.set_console_title(f"CS2 NoFlash {self.VERSION}")

        logging.info(f"{Fore.CYAN}Checking for updates...")
        Utility.check_for_updates(self.VERSION)

        logging.info(f"{Fore.CYAN}Fetching offsets and client data...")
        offsets, client_data = Utility.fetch_offsets()
        if offsets is None or client_data is None:
            input(f"{Fore.RED}Press Enter to exit...")
            return

        # Set offsets and client data
        self.dwLocalPlayerPawn = offsets["client.dll"]["dwLocalPlayerPawn"]
        self.m_flFlashDuration = client_data["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashDuration"]
        
        logging.info(f"{Fore.CYAN}Searching for cs2.exe process...")
        if not self.pymem_handler.initialize_pymem() or not self.pymem_handler.get_client_module():
            input(f"{Fore.RED}Press Enter to exit...")
            return

        logging.info(f"{Fore.GREEN}NoFlash script started.")
        self.run_noflash_loop()

    def run_noflash_loop(self):
        """Runs the main loop of the NoFlash script."""
        try:
            while True:
                player_position = self.pymem_handler.pm.read_longlong(self.pymem_handler.client_base + self.dwLocalPlayerPawn)
                if player_position:
                    self.pymem_handler.pm.write_float(player_position + self.m_flFlashDuration, 0.0)
                time.sleep(0.1)
        except KeyboardInterrupt:
            logging.info(f"{Fore.YELLOW}NoFlash script terminated by user.")
        except Exception as e:
            logging.error(f"{Fore.RED}Unexpected error: {e}")
            input(f"{Fore.RED}Press Enter to exit...")

if __name__ == '__main__':
    Logger.setup_logging()
    noflash = NoFlashScript()
    noflash.start()