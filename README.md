<div align="center">
   <img src="src/img/icon.png" alt="CS2 NoFlash" width="200" height="200">
   <h1>🌟 CS2 NoFlash 🌟</h1>
   <p>Your ultimate anti-flash tool for Counter-Strike 2</p>
   <a href="#features"><strong>Features</strong></a> •
   <a href="#installation"><strong>Installation</strong></a> •
   <a href="#usage"><strong>Usage</strong></a> •
   <a href="#customization"><strong>Customization</strong></a> •
   <a href="#troubleshooting"><strong>Troubleshooting</strong></a> •
   <a href="#contributing"><strong>Contributing</strong></a>
   <br><br>
   <p><strong>🌍 Translations:</strong></p>
   <a href="README.ru.md"><img src="https://img.shields.io/badge/lang-Russian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.fr.md"><img src="https://img.shields.io/badge/lang-French-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Spanish-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.uk-UA.md"><img src="https://img.shields.io/badge/lang-Ukrainian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.pl.md"><img src="https://img.shields.io/badge/lang-Polish-purple?style=for-the-badge&logo=googletranslate"></a>
</div>

---

# Overview
CS2 NoFlash is an automated tool designed for Counter-Strike 2 that prevents the player from being fully flashed by automatically adjusting the flashbang alpha values in the game.

## Features
- **Anti-Flash Protection:** Automatically sets the flashbang alpha value to 0, preventing the player from being fully blinded.
- **Process Attachment:** Attaches to the `cs2.exe` process and reads memory values to apply real-time changes.
- **Update Checker:** Automatically checks for the latest version and notifies the user if an update is available.
- **Error Logging:** Logs errors and important events to a log file for debugging purposes.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Jesewe/cs2-noflash.git
   cd cs2-noflash
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   ```bash
   python main.py
   ```

## Usage
1. Ensure that Counter-Strike 2 is running.
2. Execute the script using the command above.
3. The script will automatically check for updates and fetch the necessary offsets from the provided sources.
4. The NoFlash protection will start automatically, reducing the flashbang effect to minimal.

## Customization
- **Log Directory:** The log files are saved in the `%LOCALAPPDATA%\Requests\ItsJesewe\crashes` directory by default. You can change this by modifying the `LOG_DIRECTORY` variable in the script.

## Troubleshooting
- **Failed to Fetch Offsets:** Ensure you have an active internet connection and that the source URLs are accessible.
- **Could Not Open `cs2.exe`:** Make sure the game is running and that you have the necessary permissions.
- **Unexpected Errors:** Check the log file located in the log directory for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/Jesewe/cs2-noflash).

## Disclaimer
This script is for educational purposes only. Using cheats or hacks in online games is against the terms of service of most games and can result in bans or other penalties. Use this script at your own risk.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.