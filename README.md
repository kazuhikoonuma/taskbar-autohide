## Origin Story

A long time ago, in a system not so far away, a curious challenge emerged: the taskbar's auto-hide feature would sometimes switch off on its own. Respecting the complexity of system design, I set out on a journey to restore desktop harmony. Thus, this program was created.

## Motivation

![dialog](https://github.com/kazuhikoonuma/taskbar-autohide/blob/main/resources/dialog.png)

> A toolbar is already hidden on this side of your screen.  
> You can have only one auto-hide toolbar per side.

My note pc has an OLED display. To prevent burn-in, I want to hide the taskbar. However, when I wake up from sleep, the taskbar's auto-hide feature is disabled. It's a bit of a hassle to re-enable it from the settings. So I made a program that monitors this and re-enables it if necessary.

## Features

- **Auto-hide Taskbar**: Automatically re-enables the taskbar's auto-hide feature if it is disabled.
- **System Tray Icon**: Provides a visual indicator of the program's status.
- **Notification System**: Notifies the user when the taskbar's auto-hide feature is re-enabled.
- **Prevention of Multiple Instances**: Ensures that only one instance of the program is running at a time.

## Usage
### Simple Usage

1. Download the latest release from the [Releases]() page.
2. Run the executable file.

### Advanced Usage

1. Download
2. Put the executable link file in a startup directory. (e.g., `shell:startup`)
3. When you log in Windows, the program will start automatically.

## Operating Principle

This program monitors the taskbar's auto-hide feature by polling it every 10 seconds. If the auto-hide feature is disabled, the program re-enables it. The program runs in the background and can be accessed via the system tray icon.

## Test Environment

- Windows 11 Pro (24H2)
- Python 3.13

## Build

```bash
pip install -r resources/requirements.txt
pyinstaller resources/autohide.spec
```
Then, the executable will be in the `dist` directory.

## About

Repository : [GitHub](https://github.com/kazuhikoonuma/taskbar-autohide)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kazuhikoonuma/taskbar-autohide/LICENSE) file for details.

## Third-Party Licenses

This project uses the following third-party libraries, each under their respective licenses:

- **[cairosvg](https://github.com/Kozea/CairoSVG)**: LGPL-3.0
- **[Pillow (PIL)](https://github.com/python-pillow/Pillow)**: MIT-CMU
- **[pystray](https://github.com/moses-palmer/pystray)**: GPL-3.0 or LGPL-3.0 (dual-licensed)
- **[tendo](https://github.com/pycontribs/tendo)**: PSF-2.0
- **[winotify](https://github.com/versa-syahptr/winotify)**: MIT
- **[PyInstaller](https://github.com/pyinstaller/pyinstaller)**: GPL-2.0-or-later with Bootloader Exception (core); runtime hooks are under the Apache License 2.0; the isolated submodule is under the MIT license.

Please refer to the official license texts of these libraries for further details.

## Support

I hope this project can be of use to you. If you would like to support me, please use the link below.

[![ko-fi](https://github.com/kazuhikoonuma/taskbar-autohide/blob/main/resources/support_me_on_kofi_dark.png)](https://ko-fi.com/kazuhikoonuma)
