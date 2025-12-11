#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def convert_video(input_file, output_file, format_type="mp4"):
    """Convert video using ffmpeg"""
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return False
    
    try:
        cmd = ["ffmpeg", "-i", input_file, "-y", output_file]
        print(f"Converting {input_file} to {output_file}...")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Conversion successful: {output_file}")
            return True
        else:
            print(f"❌ Conversion failed: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ ffmpeg not found! Please install ffmpeg first.")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <output_file>")
        print("Example: python main.py video.avi video.mp4")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_video(input_file, output_file)

if __name__ == "__main__":
    main()
