import pymem, pymem.process, time, ctypes
from colorama import Fore, init

init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("CS2 NoFlash Script | ItsJesewe")

dwLocalPlayerPawn = 24338920 # Offset : https://github.com/sezzyaep/CS2-OFFSETS/blob/main/offsets.json
m_flFlashMaxAlpha = 5320 # Offset : https://github.com/sezzyaep/CS2-OFFSETS/blob/main/client.dll.json

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