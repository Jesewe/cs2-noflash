import pymem, pymem.process, time, ctypes
from colorama import Fore, init
from requests import get

init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("CS2 NoFlash Script | ItsJesewe")

offset = get("https://raw.githubusercontent.com/sezzyaep/CS2-OFFSETS/main/offsets.json").json()
client = get("https://raw.githubusercontent.com/sezzyaep/CS2-OFFSETS/main/client.dll.json").json()

dwLocalPlayerPawn = offset["client.dll"]["dwLocalPlayerPawn"]
m_flFlashMaxAlpha = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]

def noflash():
    try:
        print(Fore.YELLOW + "[*] Searching for cs2.exe process...\n")
        pm = pymem.Pymem("cs2.exe")
        client_module = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except pymem.exception.ProcessNotFound:
        print(Fore.RED + '[*] cs2.exe process is not running!')
    except pymem.exception.ProcessError:
        print(Fore.RED + '[*] Error accessing process cs2.exe')
    except pymem.exception.MemoryReadError:
        print(Fore.RED + '[*] Error reading memory')
    except pymem.exception.MemoryWriteError:
        print(Fore.RED + '[*] Error writing memory')
    except AttributeError:
        print(Fore.RED + '[*] Byte pattern not found')
    else:
        print(Fore.GREEN + "[*] cs2.exe is running.\n\n[*] Client loaded...")
        player_position = pm.read_longlong(client_module + dwLocalPlayerPawn)
        pm.write_int(player_position + m_flFlashMaxAlpha, 0)
    finally:
        input('\n[*] All done, you can close this window by pressing Enter...')

if __name__ == "__main__":
    noflash()