# Simple Timer

A graphical countdown timer

## Prerequisites

Install python (developed with python 3.10.11).
Recommended to use [pyenv](https://github.com/pyenv/pyenv) to manage python versions and virtual environments.

### Install python packages

```bash
pip install -r requirements.txt
```

## Usage

### Launch the application

```bash
python main.py
```

### Modify the timers
Edit the csv file `timers.csv` with your favorite editor.
The format is `time,text` where time is in the format `DD/MM/YYYY HH:MM:SS` and text is the text to display.

## Development

VSCode is recommended as an IDE, launch scripts are provided.

main.py - instantiates the user interface and the threads
ui_main.py - the user interface (AUTOMATICALLY GENERATED DO NOT EDIT)
thread_timer.py - the thread that handles the timer

### Modify the user interface using qt designer

Install from [website](https://build-system.fman.io/qt-designer-download) or using your package manager.

### Generate the user interface

```bash
pyuic6 ui_main.ui -o ui_main.py
```