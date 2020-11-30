import os
import inspect
import subprocess
import json
import html_parser
import requests
from pathlib import Path


PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))
ARWEAVE = os.path.join(PATH, "arweave-x64")
WALLET_PATH = None
VIDEO_PATH = None
VIDEO_FILE_SIZE = None
HASH = None
DEPLOYING = False
APP_FILE_SIZE = None
ARWEAVE_PRICE_URL = "https://arweave.net/price/"

def get_file_size_3(file):
    size = Path(file).stat().st_size
    return size


def convert_bytes(size, unit=None):
    if unit == "KB":
        return round(size / 1024, 3)
    elif unit == "MB":
        return round(size / (1024 * 1024), 3)
    elif unit == "GB":
        return round(size / (1024 * 1024 * 1024), 3)
    
    return size

def get_price(mb):
    print("Getting arweave price")
    dat = {'q':'goog'}
    kb = mb * 1000
    kb = str(int(kb))
    url = os.path.join(ARWEAVE_PRICE_URL, kb)
    resp = requests.get(url, params=dat, headers={'User-Agent': 'Mozilla/5.0'})
    winstons = int(resp.content.decode('utf-8'))
    ar = winstons * 0.000000000001
    print(ar)
    print(VIDEO_FILE_SIZE)

def network_info():
    tmp_file = os.path.join(PATH, "tmp")
    os.system(ARWEAVE + " network-info > " + tmp_file)
    return json.loads(open(tmp_file, 'r').read())
    # return "Disabled"

def create_key_file():
    print("loading key file")

def save_key_file():
    print("save key file")

def forget_key_file():
    print("forget key file")

def wallet_balance():
    print("wallet balance:")
    result = None
    if WALLET_PATH != None:
        print(WALLET_PATH)
        result = subprocess.run([ARWEAVE, 'balance', '--key-file', WALLET_PATH], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        print("Wallet balance is: " + result)

    return result

def transaction_status():
    print("transaction status for:")
    result = None
    if HASH != None:
        print(HASH)
        result = subprocess.run([ARWEAVE, 'status', HASH], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')

    return result

def test_package(srcHTML, destHTML):
    result = subprocess.run([ARWEAVE, 'package', srcHTML, destHTML, "--force-skip-warnings"], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    return result


def deploy_videos(templateDir):
    print("arweave deploy file")
    result = {}
    template_path = os.path.join(PATH, "templates")
    template_path = os.path.join(template_path, templateDir)
    video_path = os.path.join(template_path, "videos")

    print(WALLET_PATH)

    # if WALLET_PATH != None:

    #     for files in os.listdir(video_path ):
            
    #         result = subprocess.run([ARWEAVE, files, 'deploy', '--key-file', WALLET_PATH, '--package'], stdout=subprocess.PIPE)
    #         result = result.stdout.decode('utf-8')

    return result


def deploy_app():
    print("arweave deploy app")
    result = None
    test_file = os.path.join(PATH, 'test')
    test_file = os.path.join(test_file, 'index.html')
    arweave_cmd = ARWEAVE + ' deploy ' + test_file + ' --key-file ' + WALLET_PATH + ' --force-skip-confirmation --force-skip-warnings' + '\n'
    # arweave_cmd = [ARWEAVE, 'deploy', test_file, '--key-file', WALLET_PATH, '--force-skip-confirmation', '--force-skip-warnings']

    print(arweave_cmd)
    # result = subprocess.run(arweave_cmd, stdout=subprocess.PIPE)
    # result = result.stdout.decode('utf-8')

    result = subprocess_cmd(arweave_cmd)
    
    return result

def deploy_video_app():
    print("arweave deploy video app")
    # result = None
    # test_file = os.path.join(PATH, 'test')
    # test_file += os.path.join(test_file, 'index.html')
    # arweave_cmd = ARWEAVE + ' deploy ' + test_file, ' --key-file ' + WALLET_PATH + ' --package'
    # commands = [arweave_cmd, 'CONFIRM']

    # result = subprocess_cmd(commands)
    
    # return result

def deploy_video():
    print("arweave deploy video")
    result = None
    arweave_cmd = ARWEAVE + ' deploy ' + VIDEO_PATH + ' --key-file ' + WALLET_PATH + ' --force-skip-confirmation --force-skip-warnings' + '\n'
    # arweave_cmd = [ARWEAVE, 'deploy', test_file, '--key-file', WALLET_PATH, '--force-skip-confirmation', '--force-skip-warnings']

    print(arweave_cmd)
    # result = subprocess.run(arweave_cmd, stdout=subprocess.PIPE)
    # result = result.stdout.decode('utf-8')

    result = subprocess_cmd(arweave_cmd)
    
    return result
        

def subprocess_cmd(commands):
    result = None
    process = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))

    result = out.decode('utf-8')

    if err != None:
        result = err.decode('utf-8')

    print(result)

    return result