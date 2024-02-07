import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import time 
import multiprocessing
import json
import argparse
import os
import subprocess
from pyvirtualdisplay import Display
import sys
import random
import math
import signal

def check_port(port):
    try:
        # Run netstat command and grep the port
        result = subprocess.check_output(['netstat', '-tulpn'], text=True)
        if str(port) in result:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def is_loaded(webdriver):
    return webdriver.execute_script("return document.readyState") == "complete"

def wait_until_loaded(webdriver, timeout=30, period=0.25, min_time=0):
    start_time = time.time()
    mustend = time.time() + timeout
    while time.time() < mustend:
        if is_loaded(webdriver):
            if time.time() - start_time < min_time:
                time.sleep(min_time + start_time - time.time())
            return True
        time.sleep(period)
    return False

def remove_popup(driver):
    print('popup:', driver.current_url)
    close_button = []
    close_anchor = []
    # Find the close button (this uses a common convention of 'x' or 'close' text)
    try:
        close_button = driver.find_elements(By.XPATH, "//button[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
        close_anchor = driver.find_elements(By.XPATH, "//a[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
    except Exception as e:
        # print(close_button, close_anchor)
        print('close_button find element error', 1, e)

    close_button.extend(close_anchor)
    if len(close_button) > 0:
        for i in close_button:
            try:
                # print(i.text)
                i.click()

            except Exception as e:
                print('popup', 2, e)

# could possibly make the driver stale. plz check!
def remove_alert(driver):
    print('alert:', driver.current_url)
    alert_find = 1
    # Alert
    try:
        # Wait for the alert to be present
        WebDriverWait(driver, 5).until(EC.alert_is_present())
    except Exception as e:
        alert_find = 0
        print("No alert present.", 1, e)

    # Wait for the modal to be visible
    try: 
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal') and contains(@role, 'dialog')]"))
        )
    except Exception as e:
        alert_find = 0
        print('modal element not found', 2, e)

    if alert_find:
        try:
            # Switch to the alert
            alert = driver.switch_to.alert

            # You can also retrieve alert text if needed: alert_text = alert.text

            # Accept the alert (clicks "Ok")
            alert.accept()

            # If you need to dismiss the alert (clicks "Cancel"), use: alert.dismiss()
        except Exception as e:
            print("couldn't switch to alert", 3, e)

def remove_cmp_banner(options):
    options.add_extension(f'/home/ritik/work/pes/measurements/extensions/extn_crx/Consent-O-Matic.crx')
    return options
        
# this removes captcha and brings determinism
def use_catapult(options, fname, port, wpr_index):
    folder_path = f"/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{fname}_{wpr_index}"
    if not os.path.exists(folder_path):
    # Create the folder
        os.makedirs(folder_path)

    # options.add_argument('--ignore-certificate-errors')
    options.add_argument(f'--user-data-dir={folder_path}')
    # options.add_argument(folder_path)
    options.add_argument(f'--host-resolver-rules="MAP *:80 127.0.0.1:{port},MAP *:443 127.0.0.1:{port+1},EXCLUDE localhost"')
    options.add_argument('--ignore-certificate-errors-spki-list=PhrPvGIaAMmd29hj8BCZOq096yj7uMpRNHpn5PDxI6I=,2HcXCSKKJS0lEXLQEWhpHUfGuojiU0tiT5gOF9LP6IQ=')
    return options

def start_servers(replay, index, extn):
    port = 9090
    processes = []

    folder_path = f'/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{extn}'
    if not os.path.exists(folder_path):
    # Create the folder
        os.makedirs(folder_path)

    original_directory = os.getcwd()
    target_directory = '/home/ritik/go/src/catapult/web_page_replay_go/'

    # Change to the target directory
    os.chdir(target_directory)

    for i in range(2):
        temp_port1 = port + 2*(index + i)
        temp_port2 = port + 2*(index + i) + 1
        print(f'starting servers with ports: {temp_port1} {temp_port2}')
        try:
            if replay:
                cmd = ['go', 'run', 'src/wpr.go', 'replay', '--http_port', str(temp_port1), '--https_port', str(temp_port2), f'/home/ritik/work/pes/measurements/break/html_elements/archive/{extn}_{index+i}.wprgo']
            else:
                cmd = ['go', 'run', 'src/wpr.go', 'record', '--http_port', str(temp_port1), '--https_port', str(temp_port2), f'/home/ritik/work/pes/measurements/break/html_elements/archive/{extn}_{index+i}.wprgo']

            process = subprocess.Popen(cmd, env = os.environ.copy(), stdout = sys.stdout, stderr = sys.stdout)
            print('functions.py', process, process.pid)
            processes.append(process)
            # os.system(" ".join(cmd))
            while True:
                print(f'Waiting for port {temp_port1} to be occupied')
                time.sleep(2)
                if check_port(temp_port1):
                    break
            # out, err = process.communicate()
            # print(out.decode('utf-8'), err.decode('utf-8'))

        except subprocess.TimeoutExpired as t:
            print(f'Timeout for num_server: {index}')
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f'Error for num_server: {index}')
            sys.exit(1)

        except Exception as e:
            print(e)
            sys.exit(1)

    os.chdir(original_directory)
    
    return processes

def stop_servers(i, ports_list):
    port = 9090
    try:
        pid1 = get_pid_by_port(port+2*(i))
        pid2 = get_pid_by_port(port+2*(i+1))
        print(pid1, pid2)
        
        if pid1 != None:
            os.kill(int(pid1), signal.SIGINT)
            time.sleep(2)
        ports_list.remove(port+2*(i))

        if pid2 != None:
            os.kill(int(pid2), signal.SIGINT)
            time.sleep(2)
        ports_list.remove(port+2*(i+1))

    except ProcessLookupError:
        print(f"No process with PID {pid1} found.")
    except PermissionError:
        print(f"Permission denied to send signal to process {pid1}.")

    return ports_list
    
def get_pid_by_port(port):
    try:
        output = subprocess.check_output(['lsof', '-i', f'tcp:{port}']).decode()
    except subprocess.CalledProcessError as e:
        print("Error:", subprocess.check_output(['lsof', '-i', 'tcp']).decode())
        return None

    for line in output.splitlines():
        if "LISTEN" in line:
            parts = line.split()
            return parts[1]  # PID is typically in the second column

    return None