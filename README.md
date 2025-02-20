## Origin Story

A long time ago, in a system not so far away, a curious challenge emerged: the taskbar's auto-hide feature would sometimes switch off on its own. Respecting the complexity of system design, I set out on a journey to restore desktop harmony. Thus, this program was created.

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
