#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading
import os

class VideoConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Converter")
        self.root.geometry("500x300")
        
        self.input_file = ""
        self.output_file = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        # Input file selection
        tk.Label(self.root, text="Input Video:").pack(pady=5)
        
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5, padx=20, fill="x")
        
        self.input_label = tk.Label(input_frame, text="No file selected", bg="white", relief="sunken")
        self.input_label.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        tk.Button(input_frame, text="Browse", command=self.select_input_file).pack(side="right")
        
        # Output format selection
        tk.Label(self.root, text="Output Format:").pack(pady=(20, 5))
        
        self.format_var = tk.StringVar(value="mp4")
        format_frame = tk.Frame(self.root)
        format_frame.pack(pady=5)
        
        formats = ["mp4", "avi", "mov", "mkv", "webm"]
        for fmt in formats:
            tk.Radiobutton(format_frame, text=fmt.upper(), variable=self.format_var, value=fmt).pack(side="left", padx=10)
        
        # Convert button
        self.convert_btn = tk.Button(self.root, text="Convert Video", command=self.convert_video, 
                                   bg="#4CAF50", fg="white", font=("Arial", 12))
        self.convert_btn.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(pady=10, padx=20, fill="x")
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready", fg="blue")
        self.status_label.pack(pady=5)
    
    def select_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv *.webm *.flv *.wmv"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file = file_path
            self.input_label.config(text=os.path.basename(file_path))
    
    def convert_video(self):
        if not self.input_file:
            messagebox.showerror("Error", "Please select an input file!")
            return
        
        # Generate output filename
        input_path = os.path.splitext(self.input_file)
        self.output_file = f"{input_path[0]}_converted.{self.format_var.get()}"
        
        # Start conversion in separate thread
        self.convert_btn.config(state="disabled")
        self.progress.start()
        self.status_label.config(text="Converting...", fg="orange")
        
        thread = threading.Thread(target=self.run_conversion)
        thread.start()
    
    def run_conversion(self):
        try:
            cmd = ["ffmpeg", "-i", self.input_file, "-y", self.output_file]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            self.root.after(0, self.conversion_complete, result.returncode == 0)
            
        except FileNotFoundError:
            self.root.after(0, self.conversion_complete, False, "ffmpeg not found!")
    
    def conversion_complete(self, success, error_msg=""):
        self.progress.stop()
        self.convert_btn.config(state="normal")
        
        if success:
            self.status_label.config(text="Conversion completed!", fg="green")
            messagebox.showinfo("Success", f"Video converted successfully!\nSaved as: {os.path.basename(self.output_file)}")
        else:
            self.status_label.config(text="Conversion failed!", fg="red")
            messagebox.showerror("Error", f"Conversion failed!\n{error_msg}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverter(root)
    root.mainloop()
