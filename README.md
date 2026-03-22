# David's System Monitor

## Description

David's System Monitor is a lightweight terminal-based tool that displays real-time system resource usage. It provides a clear and readable overview of CPU, memory (RAM), disk usage, and optional GPU statistics.

The interface uses color-coded bars to help you quickly understand system load at a glance.
<img width="823" height="288" alt="preview" src="https://github.com/user-attachments/assets/5e6c6083-4032-4450-ac2e-4645e2c999e1" />
---

## Features

* Real-time system monitoring
* CPU usage tracking
* Memory (RAM) usage tracking
* Disk usage tracking
* Optional GPU monitoring (if supported)
* Color-coded output:

  * **Green** → Normal usage
  * **Yellow** → Moderate usage
  * **Red** → High usage
* Smooth terminal updates
* Works without a GPU
* Cross-platform support (Windows & Linux)
* Easy to stop with `Ctrl + C`

---

## Requirements

* Python 3.10 or newer

* Required library:

  ```bash
  pip install psutil
  ```

* Optional (for GPU monitoring):

  ```bash
  pip install gpustat
  ```

---

## Usage

1. Open a terminal
2. Navigate to the project folder:

   ```bash
   cd path/to/davids_system_monitor
   ```
3. Run the program:

   ```bash
   python system_monitor.py
   ```

Press `Ctrl + C` to stop the program.

---

## Optional Enhancements (Future Ideas)

* Monitor GPU usage and temperature
* Display per-core CPU usage
* Track network usage (upload/download speed)
* Log system data to a file
* Show top resource-consuming processes

---

## Notes

* Works best in terminals that support ANSI colors (PowerShell, Linux terminal, etc.)
* GPU monitoring is optional and only available if supported hardware and libraries are installed

---

## License

MIT License
