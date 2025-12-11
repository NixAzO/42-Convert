# 420CV Windows Installer
Write-Host "🎬 Installing 420CV - Fast Video Converter for Windows..." -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version 2>$null
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found!" -ForegroundColor Red
    Write-Host "📦 Please install Python from: https://python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    exit 1
}

# Check if ffmpeg is available
try {
    $ffmpegVersion = ffmpeg -version 2>$null | Select-String "ffmpeg version" | Select-Object -First 1
    Write-Host "✅ FFmpeg found" -ForegroundColor Green
} catch {
    Write-Host "❌ FFmpeg not found!" -ForegroundColor Red
    Write-Host "📦 Please download FFmpeg from: https://ffmpeg.org/download.html" -ForegroundColor Yellow
    Write-Host "   Extract to C:\ffmpeg\ or add to PATH" -ForegroundColor Yellow
    Write-Host "   Or use chocolatey: choco install ffmpeg" -ForegroundColor Yellow
}

# Create batch file in Windows directory
$windowsDir = $env:WINDIR
$batchContent = "@echo off`npython `"$PWD\420cv.py`" %*"

try {
    $batchContent | Out-File -FilePath "$windowsDir\420cv.bat" -Encoding ASCII
    Write-Host "✅ 420CV installed successfully!" -ForegroundColor Green
    Write-Host "🚀 Usage: Open Command Prompt and type '420cv'" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📖 Quick commands:" -ForegroundColor Yellow
    Write-Host "   420cv" -ForegroundColor White
    Write-Host "   420cv> video.avi mp4" -ForegroundColor White
    Write-Host "   420cv> batch *.mov webm" -ForegroundColor White
    Write-Host "   420cv> formats" -ForegroundColor White
    Write-Host "   420cv> exit" -ForegroundColor White
} catch {
    Write-Host "❌ Installation failed. Please run as Administrator." -ForegroundColor Red
    Write-Host "💡 Alternative: Add this folder to your PATH environment variable" -ForegroundColor Yellow
    exit 1
}
