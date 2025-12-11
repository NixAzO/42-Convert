#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading
import os

class ModernVideoConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Converter Pro")
        self.root.geometry("600x500")
        self.root.configure(bg="#0f0f23")
        self.root.resizable(False, False)
        
        # Colors
        self.bg_color = "#0f0f23"
        self.card_color = "#1a1a2e"
        self.accent_color = "#6c5ce7"
        self.success_color = "#00b894"
        self.text_color = "#ddd"
        self.white = "#ffffff"
        
        self.input_file = ""
        self.output_file = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, height=80)
        header_frame.pack(fill="x", padx=20, pady=(20, 0))
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="Video Converter Pro", 
                        font=("Helvetica", 24, "bold"), 
                        fg=self.white, bg=self.bg_color)
        title.pack(side="left", pady=20)
        
        subtitle = tk.Label(header_frame, text="Transform your videos with style", 
                           font=("Helvetica", 10), 
                           fg="#74b9ff", bg=self.bg_color)
        subtitle.pack(side="left", padx=(10, 0), pady=(30, 0))
        
        # Main card
        main_card = tk.Frame(self.root, bg=self.card_color, relief="flat", bd=0)
        main_card.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Input section
        input_section = tk.Frame(main_card, bg=self.card_color)
        input_section.pack(fill="x", padx=30, pady=(30, 20))
        
        tk.Label(input_section, text="SELECT VIDEO FILE", 
                font=("Helvetica", 10, "bold"), 
                fg="#74b9ff", bg=self.card_color).pack(anchor="w")
        
        input_container = tk.Frame(input_section, bg=self.card_color)
        input_container.pack(fill="x", pady=(10, 0))
        
        self.input_display = tk.Frame(input_container, bg="#2d3436", relief="flat", bd=1)
        self.input_display.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.input_label = tk.Label(self.input_display, text="🎬 Drop your video here or click browse", 
                                   font=("Helvetica", 11), fg="#636e72", bg="#2d3436", 
                                   pady=15, cursor="hand2")
        self.input_label.pack(fill="x")
        self.input_label.bind("<Button-1>", lambda e: self.select_input_file())
        
        browse_btn = tk.Button(input_container, text="BROWSE", 
                              font=("Helvetica", 10, "bold"),
                              bg=self.accent_color, fg=self.white, 
                              relief="flat", bd=0, padx=20, pady=15,
                              cursor="hand2", command=self.select_input_file)
        browse_btn.pack(side="right")
        
        # Format section
        format_section = tk.Frame(main_card, bg=self.card_color)
        format_section.pack(fill="x", padx=30, pady=20)
        
        tk.Label(format_section, text="OUTPUT FORMAT", 
                font=("Helvetica", 10, "bold"), 
                fg="#74b9ff", bg=self.card_color).pack(anchor="w")
        
        self.format_var = tk.StringVar(value="mp4")
        format_container = tk.Frame(format_section, bg=self.card_color)
        format_container.pack(fill="x", pady=(15, 0))
        
        formats = [
            ("MP4", "mp4", "🎥"),
            ("AVI", "avi", "📹"), 
            ("MOV", "mov", "🎬"),
            ("MKV", "mkv", "📺"),
            ("WEBM", "webm", "🌐")
        ]
        
        for i, (name, value, icon) in enumerate(formats):
            btn_frame = tk.Frame(format_container, bg="#2d3436" if i == 0 else "#636e72", 
                               relief="flat", bd=0, cursor="hand2")
            btn_frame.pack(side="left", padx=(0, 10), fill="y")
            
            btn = tk.Radiobutton(btn_frame, text=f"{icon} {name}", 
                               variable=self.format_var, value=value,
                               font=("Helvetica", 10, "bold"),
                               fg=self.white, bg="#2d3436" if i == 0 else "#636e72",
                               selectcolor=self.accent_color, relief="flat", bd=0,
                               padx=15, pady=10, cursor="hand2",
                               command=lambda: self.update_format_buttons())
            btn.pack()
        
        # Convert section
        convert_section = tk.Frame(main_card, bg=self.card_color)
        convert_section.pack(fill="x", padx=30, pady=(30, 20))
        
        self.convert_btn = tk.Button(convert_section, text="🚀 START CONVERSION", 
                                   font=("Helvetica", 14, "bold"),
                                   bg=self.success_color, fg=self.white, 
                                   relief="flat", bd=0, pady=20,
                                   cursor="hand2", command=self.convert_video)
        self.convert_btn.pack(fill="x")
        
        # Progress section
        progress_section = tk.Frame(main_card, bg=self.card_color)
        progress_section.pack(fill="x", padx=30, pady=(0, 30))
        
        self.progress_frame = tk.Frame(progress_section, bg=self.card_color)
        
        self.status_label = tk.Label(self.progress_frame, text="Ready to convert", 
                                   font=("Helvetica", 11), 
                                   fg="#74b9ff", bg=self.card_color)
        self.status_label.pack(pady=(10, 5))
        
        # Custom progress bar
        self.progress_bg = tk.Frame(self.progress_frame, bg="#2d3436", height=6)
        self.progress_bg.pack(fill="x", pady=(0, 10))
        
        self.progress_fill = tk.Frame(self.progress_bg, bg=self.accent_color, height=6)
        
        # Footer
        footer = tk.Frame(self.root, bg=self.bg_color, height=40)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)
        
        tk.Label(footer, text="Made with ❤️ for creators", 
                font=("Helvetica", 9), 
                fg="#636e72", bg=self.bg_color).pack(pady=10)
    
    def update_format_buttons(self):
        # Visual feedback for format selection
        pass
    
    def select_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv *.webm *.flv *.wmv"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file = file_path
            filename = os.path.basename(file_path)
            self.input_label.config(text=f"✅ {filename}", fg=self.success_color)
            self.input_display.config(bg="#00b894")
    
    def convert_video(self):
        if not self.input_file:
            messagebox.showerror("Error", "Please select an input file!")
            return
        
        # Generate output filename
        input_path = os.path.splitext(self.input_file)
        self.output_file = f"{input_path[0]}_converted.{self.format_var.get()}"
        
        # Start conversion
        self.convert_btn.config(state="disabled", text="🔄 CONVERTING...", bg="#636e72")
        self.progress_frame.pack(fill="x")
        self.status_label.config(text="Converting your video...", fg="#fdcb6e")
        self.animate_progress()
        
        thread = threading.Thread(target=self.run_conversion)
        thread.start()
    
    def animate_progress(self):
        # Simple progress animation
        self.progress_fill.pack(side="left", fill="y")
        self.progress_fill.config(width=0)
        
        def animate(width=0):
            if width <= 300:
                self.progress_fill.config(width=width)
                self.root.after(50, lambda: animate(width + 5))
        
        animate()
    
    def run_conversion(self):
        try:
            cmd = ["ffmpeg", "-i", self.input_file, "-y", self.output_file]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            self.root.after(0, self.conversion_complete, result.returncode == 0)
            
        except FileNotFoundError:
            self.root.after(0, self.conversion_complete, False, "ffmpeg not found!")
    
    def conversion_complete(self, success, error_msg=""):
        self.convert_btn.config(state="normal")
        
        if success:
            self.convert_btn.config(text="✅ CONVERSION COMPLETE", bg=self.success_color)
            self.status_label.config(text="🎉 Video converted successfully!", fg=self.success_color)
            self.progress_fill.config(bg=self.success_color, width=300)
            messagebox.showinfo("Success", f"🎬 Video converted successfully!\n📁 Saved as: {os.path.basename(self.output_file)}")
        else:
            self.convert_btn.config(text="❌ CONVERSION FAILED", bg="#e17055")
            self.status_label.config(text="💥 Conversion failed!", fg="#e17055")
            self.progress_fill.config(bg="#e17055")
            messagebox.showerror("Error", f"❌ Conversion failed!\n{error_msg}")
        
        # Reset after 3 seconds
        self.root.after(3000, self.reset_ui)
    
    def reset_ui(self):
        self.convert_btn.config(text="🚀 START CONVERSION", bg=self.success_color)
        self.status_label.config(text="Ready for next conversion", fg="#74b9ff")
        self.progress_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernVideoConverter(root)
    root.mainloop()
