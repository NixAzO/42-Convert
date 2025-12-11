#!/bin/bash

echo "🎬 Installing 420CV - Fast Video Converter..."

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg not found!"
    echo "📦 Please install FFmpeg first:"
    echo "   sudo pacman -S ffmpeg      # Arch Linux"
    echo "   sudo apt install ffmpeg   # Ubuntu/Debian"
    echo "   brew install ffmpeg       # macOS"
    exit 1
fi

# Make executable
chmod +x 420cv

# Install to system
if sudo cp 420cv /usr/local/bin/; then
    echo "✅ 420CV installed successfully!"
    echo "🚀 Usage: Type '420cv' to start"
    echo ""
    echo "📖 Quick commands:"
    echo "   420cv> video.avi mp4"
    echo "   420cv> batch *.mov webm"
    echo "   420cv> formats"
    echo "   420cv> exit"
else
    echo "❌ Installation failed. Try running with sudo."
    exit 1
fi
