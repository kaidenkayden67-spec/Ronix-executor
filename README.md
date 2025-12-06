# Ronix Executor

A lightweight CLI for organizing Roblox Lua scripts before sending them to your
preferred injector. The tool **does not** perform any injection itself; it keeps
scripts tidy, lets you create new ones quickly, and prints them so you can feed
them into other tools.

## Installation

The executor is pure Python and requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
```

## Usage

The CLI initializes with a sample script so you always have something to test.

```bash
# list available scripts
python -m ronix_executor list

# add a new script from stdin
python -m ronix_executor add fly_script <<'LUA'
-- fly hack placeholder
print("Enable fly mode")
LUA

# print the script body for piping into your injector
python -m ronix_executor run fly_script
```

To store scripts somewhere else, pass a custom directory:

```bash
python -m ronix_executor --scripts-dir ./my_scripts list
```

## Notes

* Scripts are saved as `.lua` files under `ronix_executor/scripts` by default.
* `python -m ronix_executor run <name>` simply prints the Lua source so you can
  copy it into Delta or another executor.
* The sample script lives at `ronix_executor/scripts/hello_world.lua` after the
  first run.
