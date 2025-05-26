import speedtest
import threading
import tkinter as tk
from tkinter import ttk


def run_speed_test():
    try:
        start_button.config(state=tk.DISABLED)
        progress_label.config(text="Finding best server...")
        progress_bar["value"] = 20
        root.update_idletasks()

        speed = speedtest.Speedtest()
        speed.get_best_server()

        progress_label.config(text="Testing download speed...")
        progress_bar["value"] = 50
        root.update_idletasks()

        download_speed = speed.download() / (1024 * 1024)

        progress_label.config(text="Testing upload speed...")
        progress_bar["value"] = 80
        root.update_idletasks()

        upload_speed = speed.upload() / (1024 * 1024)
        ping = speed.results.ping

        progress_bar["value"] = 100
        progress_label.config(text="Test Completed!")

        result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\n"
                                 f"Upload Speed: {upload_speed:.2f} Mbps\n"
                                 f"Ping: {ping:.2f} ms")

        start_button.config(state=tk.NORMAL)
        start_button.config(text="Start Test")
    except:
        result_label.config(fg="red", text="An error was encountered.\nPlease, try again.")

def start_speed_test():
    threading.Thread(target=run_speed_test, daemon=True).start()


# Main Tkinter GUI
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("400x300")

title_label = tk.Label(root, text="Internet Speed Test", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

start_button = tk.Button(root, text="Start Test", font=("Arial", 12), command=start_speed_test)
start_button.pack(pady=10)

progress_label = tk.Label(root, text="", font=("Arial", 12))
progress_label.pack()

progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
progress_bar.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
