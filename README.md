# Luau-Updater
Thanks for using Luau-Automatic Updater by SpinnySpiwal!

## How to use

1. Open your terminal.

2. Run the following command to download and execute the installation script:

   ```sh
   curl -sSL https://raw.githubusercontent.com/SpinnySpiwal/Luau-Updater/main/install.sh | sh
   ```

   This command will:
   - Download the `install.sh` script from the GitHub repository
   - Add the Luau updater to your `.zshrc` file
   - Source the `.zshrc` file to apply the changes

3. After the installation is complete, restart your terminal.

4. From now on Luau Updater will run automatically each time you open a new terminal, checking for updates and prompting you if a new version is available.

Note: The updater requires root access to install Luau in `/opt/local/bin`. You may be prompted for your password during the update process.

Thank you for using Luau Updater!

## What is `.zshrc`?
`.zshrc` is a file that contains the configuration for your Zsh shell.
It is used to set environment variables, aliases, and other settings that are applied when you open a new terminal.
It runs special commands whenever you open a new terminal.

## License
This project is licensed under the AGPL-3.0 License. See the [LICENSE](LICENSE) file for details.
