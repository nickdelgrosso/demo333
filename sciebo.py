import os
from textwrap import dedent
from unittest.mock import patch
from dotenv import load_dotenv
from owncloud import Client
from zipfile import ZipFile


from tqdm import tqdm
from unittest.mock import patch


def download_file(origin, dest):
    # os.makedirs(os.pardir(dest), exist_ok=True)
    if not os.path.exists(dest):
        load_dotenv()
        client = Client(os.environ["SCIEBO_URL"])
        client.login(
            os.environ["SCIEBO_USERNAME"], 
            os.environ["SCIEBO_PASSWORD"],
        )
        
        client.get_file(origin, dest)


def download_folder(origin, dest):
    zipfilename = dest + "/" + os.path.split(origin)[-1] + '.zip'
    os.makedirs(dest, exist_ok=True)
    if not os.path.exists(zipfilename):
        load_dotenv()
        client = Client(os.environ["SCIEBO_URL"])
        client.login(
            os.environ["SCIEBO_USERNAME"], 
            os.environ["SCIEBO_PASSWORD"],
        )
        
        client.get_directory_as_zip(origin, zipfilename)

    if not os.path.isdir(dest + "/" + os.path.split(origin)[-1]):
        with ZipFile(zipfilename , 'r') as zip_ref:
            zip_ref.extractall(dest)


def create_dotenv_file():
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(dedent("""
                SCIEBO_URL=
                SCIEBO_USERNAME=
                SCIEBO_PASSWORD=
            """))