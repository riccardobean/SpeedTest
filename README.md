# 🧭 Internet Speed Test (Tkinter GUI)

A simple **Python GUI application** that measures your **download speed, upload speed, and ping** using the [`speedtest`](https://pypi.org/project/speedtest-cli/) module.  
Built with **Tkinter** and **threading** for a smooth, responsive experience.

---

## 🚀 Features

- 🖥️ Clean and minimal **Tkinter interface**  
- ⚙️ Real-time progress updates  
- ⚡ Measures **download**, **upload**, and **ping**  
- 🔄 Uses **threads** to keep the UI responsive  
- 🧩 Cross-platform (Windows, macOS, Linux)

---

## 🧰 Requirements

Make sure you have **Python 3.7+** installed.

Install dependencies:

`bash
pip install speedtest-cli`

---

## 🏗️ How to Run
1) Clone this repository
2) Run the Python script `python main.py`
3) Click Start Test to begin measuring your internet speed.

---

## 🧠 How It Works

The script uses the speedtest module to locate the best server for testing.

It measures download, upload, and ping speeds in sequence.

The test runs inside a thread, ensuring the GUI remains responsive.

Progress is displayed through a progress bar and status messages.

---

## ⚠️ Error Handling

If any error occurs (e.g., network issue, timeout), a message will appear:

An error was encountered.
Please, try again.
