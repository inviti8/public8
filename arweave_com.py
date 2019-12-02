import os
import json

SCRIPT_PATH = scriptpath = os.path.realpath(__file__)
FILE_NAME = os.path.basename(SCRIPT_PATH)
PATH = SCRIPT_PATH.replace(FILE_NAME, "")

ARWEAVE = os.path.join(PATH, "arweave")

def network_info():
    tmp_file = os.path.join(PATH, "tmp")
    os.system(ARWEAVE + " network-info > " + tmp_file)
    return json.loads(open(tmp_file, 'r').read())

def deploy_app():
    print("arweave deploy app")