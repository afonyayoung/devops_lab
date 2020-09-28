#! /usr/bin/env python
import os
import tempfile
import zipfile
import argparse
import shutil
import logging

logging.basicConfig(filename='app.log',
                    format='%(filename)s[LINE:%(lineno)d]# %(levelname)\
                    -8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)
parser = argparse.ArgumentParser()
parser.add_argument("-z", help="Incomming zip file", default="first_try.zip")
args = parser.parse_args()
with tempfile.TemporaryDirectory() as tmpdir:
    logging.info(f'Created temporary directory {tmpdir}')
    try:
        with zipfile.ZipFile(args.z, 'r') as zf:
            zf.extractall(tmpdir)
            logging.info(f'Extracted files from from archive {args.z}')
            for dirpath, dirnames, files in os.walk(tmpdir):
                if dirpath != tmpdir:
                    if not os.path.exists(dirpath + '/__init__.py'):
                        try:
                            shutil.rmtree(dirpath)
                            logging.info(
                                f'Deleted directory {dirpath.replace(tmpdir, "")} from archive')
                        except OSError as e:
                            logging.error(f'Error: {dirpath} : {e.strerror}')
        with zipfile.ZipFile(args.z.replace(".zip", "") + "_new.zip", "w") as zf:
            logging.info(f'Created new archive {args.z.replace(".zip", "") + "_new.zip"}')
            for dirpath, dirnames, files in os.walk(tmpdir):
                zf.write(dirpath, dirpath.replace(tmpdir, ""))
                for filename in files:
                    zf.write(os.path.join(dirpath, filename),
                             dirpath.replace(tmpdir, "") + '/' + filename)
        logging.info(f'Removed temporary directory {tmpdir}')
    except FileNotFoundError:
        logging.error(f'File {args.z} does not exist')
        print(f'File {args.z} does not exist')
