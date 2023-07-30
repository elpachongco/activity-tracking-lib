# Activity tracking library

This library contains utility functions for recording desktop activity on windows and linux

I created this for my productivity tool [Activity Monitor](https://github.com/elpachongco/activity-monitor)

## Features 
- Cross platform [windows, linux(ubuntu, X window system)]

## Functions 

### Get foreground window name, process, pid

```python3
>>> getForegroundWindow()
('New Tab`, 2500)

>>> import psutil
>>> psutil.Process(2500).name()
'chrome.exe'
```

### isUserActive

```python3
>>> isUserActive()
True
```

## Installation

This library is now available on the python package index.

Visit the [pypi page](https://pypi.org/project/activity-tracking/).

```bash
pip install activity-tracking
```

or with python-poetry

```bash
poetry add activity-tracking
```

Please note that this software is in early stage of development. 
