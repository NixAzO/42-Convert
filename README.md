[README.md](https://github.com/user-attachments/files/24092080/README.md)
# 420CV - Fast Video Converter 🎬

Ultra-fast CLI video converter with interactive shell and 16+ format support.

## Features ✨

- 🚀 **Interactive Shell** - Type `420cv` once, convert forever
- ⚡ **16+ Formats** - MP4, AVI, MOV, MKV, WebM, FLV, WMV, 3GP, etc.
- 📦 **Batch Processing** - Convert multiple files with wildcards
- 🎯 **Smart Commands** - Simple syntax, powerful results
- 💻 **Cross-Platform** - Works on Linux, macOS, Windows

## Quick Start 🚀

```bash
# Install
git clone https://github.com/<username>/420cv.git
cd 420cv
chmod +x 420cv
sudo cp 420cv /usr/local/bin/

# Use
420cv                    # Enter interactive shell
420cv> video.avi mp4     # Convert single file
420cv> batch *.mov webm  # Batch convert
420cv> formats           # Show all formats
420cv> exit              # Exit shell
```

## Usage Examples 💻

### Single Conversion
```bash
420cv> movie.avi mp4              # Convert to MP4
420cv> clip.mov webm              # Convert to WebM
420cv> old_video.wmv mkv          # Convert legacy format
```

### Batch Conversion
```bash
420cv> batch *.mp4 avi            # Convert all MP4 to AVI
420cv> batch vacation_* webm      # Convert matching files
420cv> batch "*.mov" mp4          # Convert with quotes
```

### Format Categories
```
🎯 POPULAR: mp4 (best), avi (quality), mov (apple), mkv (open), webm (web)
📱 MOBILE: 3gp, m4v, f4v
🌐 WEB: flv, ogv, ts
💻 LEGACY: wmv, asf, rm, rmvb, vob
```

## Installation Requirements 📋

- **Python 3.6+**
- **FFmpeg** (the conversion engine)

```bash
# Install FFmpeg
sudo pacman -S ffmpeg      # Arch Linux
sudo apt install ffmpeg   # Ubuntu/Debian
brew install ffmpeg       # macOS
```

## Why 420CV? 🤔

- **420** = **4** times faster, **2** simple commands, **0** complexity
- **CV** = **C**on**V**ert (short and memorable)
- **Interactive shell** = No repetitive typing
- **16+ formats** = Convert anything to anything

## Commands Reference 📖

| Command | Description |
|---------|-------------|
| `<input> <format>` | Convert single file |
| `batch <pattern> <format>` | Batch convert files |
| `formats` | Show supported formats |
| `help` | Show help |
| `exit` | Exit shell |

## Contributing 🤝

Feel free to submit issues and pull requests!

## License 📄

MIT License - see LICENSE file for details.

---

**Made with ❤️ for video creators who love efficiency**
