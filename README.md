# Counter-Strike 2 NoFlash Script

This script disables the flashbang effect in Counter-Strike 2 by continuously setting the flash alpha value to zero.

## Features

- Continuously sets `m_flFlashMaxAlpha` to 0 to disable flashbang effects.
- Fetches the latest offsets from a remote source.
- Provides real-time logging and feedback.
- Graceful termination with `KeyboardInterrupt`.

## Requirements

- Python 3.7+
- `pymem`
- `requests`

## Installation

1. Clone the repository or download the script.

   ```sh
   git clone https://github.com/Jesewe/cs2-noflash.git
   cd cs2-noflash
   ```

2. Install the required Python libraries.

   ```sh
   pip install pymem requests
   ```

3. Run the script.

   ```sh
   python main.py
   ```

## Usage

1. Start Counter-Strike 2.
2. Run the `noflash.py` script.
3. The script will continuously disable the flash effect while the game is running.
4. To stop the script, simply close the console window or press `Ctrl+C`.

## Code Overview

The script performs the following steps:

1. Fetches the latest offsets and client data from a remote source using the `fetch_offsets` function.
2. Initializes `Pymem` to access the game's memory using the `initialize_pymem` function.
3. Continuously checks and updates the `m_flFlashMaxAlpha` value to 0 using the `noflash_loop` function, ensuring the flash effect is constantly disabled.

### Functions

- **fetch_offsets**: Fetches offsets and client data from a remote JSON source.
- **initialize_pymem**: Initializes `Pymem` and retrieves the base address of `client.dll`.
- **noflash_loop**: Continuously sets `m_flFlashMaxAlpha` to 0 to disable the flashbang effect.
- **main**: Orchestrates the flow of the script.

## Logging

The script uses the `logging` module to log important events and errors. The logs include timestamps and error messages, which can be helpful for debugging.

## Troubleshooting

- Ensure that Counter-Strike 2 is running and the window title matches `Counter-Strike 2`.
- Make sure you run the script with sufficient permissions to access the game's memory.
- Verify that the offsets are up to date. If the game updates, the offsets might change, and you will need to fetch the latest ones.

## Disclaimer

This script is for educational purposes only. Using cheats or hacks in online games is against the terms of service of most games and can result in bans or other penalties. Use this script at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.