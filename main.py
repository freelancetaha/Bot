import os
import json
import time
import threading
from random import randint, uniform
from datetime import datetime
from flask import Flask, render_template, jsonify, request
from utils.browser import setup_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import config, USER, START_TIME

# Initialize Flask app
app = Flask(__name__,
    template_folder=os.path.abspath('../templates'),
    static_folder=os.path.abspath('../static'))

# Load environment configuration
env = os.environ.get('FLASK_ENV', 'production')
app.config.from_object(config[env])

# Global variables
running = False
view_counts = {}
threads = []
thread_status = {}

# Configuration
CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.json')

def load_config():
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
    return {
        "video_urls": [],
        "threads": 2,
        "watch_time": 45,
        "loop_delay": 5
    }

bot_config = load_config()

def save_config():
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(bot_config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")

def log_message(message):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# ... (rest of the main.py code remains the same, just reference bot_config instead of config)