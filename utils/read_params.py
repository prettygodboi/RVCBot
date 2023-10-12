import os
import json


def read_secrets() -> dict:
    filename = os.path.join("secrets.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}
        
def read_gradio_host() -> dict:
    filename = os.path.join("gradio.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())["host"]
    except FileNotFoundError:
        return {}

def read_voices() -> dict:
    filename = os.path.join("voices.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}        