## Alarm using Threads
Simple implementation using threading to create a simple alarm system based on current hour (days not supported, but should be easy to implement).
##### Testing:
```sh
# Clone this repo: 
git clone https://github.com/trusted-ws/alarm-thread
cd alarm-thread

# Requirements:
python3 -m pip install -r requirements.txt

# Ready to go:
python3 main.py
```
###### Only tested on *nix with Python 3.9 but also should work in Windows environment.
##### Project Tree:
```
├── audios                # Directory containing all audio files.
│   └── __init__.py       
├── main.py               # Main program. Use this to run.
├── modules               # Directory containing all classes/functions.
│   ├── alarm             # Alarm class.
│   │   ├── __init__.py
│   │   └── main.py       # File containing Alarm class implementation.
│   ├── auxiliary.py      # Auxiliary functions.
│   └── __init__.py
└── requirements.txt      # Requirements.
```
###### To avoid compatibility issues, beep (bell) modules were not used.
