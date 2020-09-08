import os
import inspect
import subprocess
import json
import html_parser

PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))
ARWEAVE = os.path.join(PATH, "arweave-x64")
WALLET_PATH = None
HASH = None
DEPLOYING = False

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
    arweave_cmd = ARWEAVE + ' deploy ' + test_file + ' --key-file ' + WALLET_PATH + ' --force-skip-warnings'
    print(arweave_cmd)
    # commands = [arweave_cmd, 'CONFIRM']
    commands = arweave_cmd + "\n" + " CONFIRM"

    print(commands)

    result = subprocess_cmd(commands)
    
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

def subprocess_cmd(commands):
    process = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))

    if err != None:
        print(err.decode('utf-8'))

    return out.decode('utf-8')