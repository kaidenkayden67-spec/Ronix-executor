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

## Quick start

1. Ensure Python 3.11+ is available.
2. Clone this repository and enter the folder.
3. (Optional) Create and activate a virtual environment with `python -m venv .venv && source .venv/bin/activate`.
4. Run the executor directly with Python:

```bash
python -m ronix_executor list
```

This boots the CLI and shows all available scripts (a sample is auto-created on
first run).

## Usage

The CLI initializes with bundled scripts for popular games so you always have
something to test or customize.

```bash
# list available scripts (hello world + popular games)
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
* Default placeholders are created for `hello_world`, `blox_fruits`, `doors`,
  `pet_simulator`, `brookhaven`, `grow_a_garden`, `rivals_99`, and
  `night_in_the_forest` the first time you run the CLI (and they are
  regenerated if missing).
