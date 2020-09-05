import os
import inspect
import subprocess
import json
import html_parser

PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))
ARWEAVE = os.path.join(PATH, "arweave-x64")
WALLET_PATH = None
HASH = None

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
        result = subprocess.run([ARWEAVE, 'srtatus', HASH], stdout=subprocess.PIPE)
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

    if WALLET_PATH != None:

        for files in os.listdir(video_path ):
            
            result = subprocess.run([ARWEAVE, files, 'deploy', '--key-file', WALLET_PATH, '--package'], stdout=subprocess.PIPE)
            result = result.stdout.decode('utf-8')

    return result


def deploy_app():
    print("arweave deploy app")
    result = None
    test_file = os.path.join(PATH, 'test')
    test_file += os.path.join(test_file, 'index.html')

    if WALLET_PATH != None:

        result = subprocess.run([ARWEAVE, 'deploy', test_file, ' --key-file ', WALLET_PATH, '--package'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
    
    return result

def deploy_video_app():
    print("arweave deploy video app")
    result = None
    test_file = os.path.join(PATH, 'test')
    test_file += os.path.join(test_file, 'index.html')

    if WALLET_PATH != None:

        result = subprocess.run([ARWEAVE, 'deploy', test_file, ' --key-file ', WALLET_PATH, '--package'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
    
    return result