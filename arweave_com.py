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


def deploy_app():
    print("arweave deploy app")
    if WALLET_PATH != None:
        print(WALLET_PATH)
        result = subprocess.run([ARWEAVE, 'deploy', '--key-file', WALLET_PATH, '--package', '--ipfs-publish'], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        return result