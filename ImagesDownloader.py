#!/usr/bin/python3

import sys
import urllib.request
import requests
import os
import errno
from urllib.error import HTTPError
from pathlib import Path
import mimetypes


class ImageId:
    """A class used to represent an image-ID: Organizes image information in encapsulated and re-usable way.

        Attributes:
            url: A string containing the final url path of an image e.g. after possible redirection.
            name: A string containing the image file name.
            image_format: A string containing the image file format type (.jpg, .png, etc).
            is_image: A boolean indicating if url points to an image content.
            output_path: A string containing the full output file path including filename.
            overwrite: A boolean indicating if user wants to overwrite similar names files.
    """
    def __init__(self, url_address):
        """Inits ImageId with a current url_address and blank attributes."""
        self.url = url_address
        self.name = None
        self.image_format = None
        self.is_image = False
        self.output_path = None
        self.overwrite = False

    def get_name(self, output_dir):
        """Sets file and full output path names."""
        url_split = self.url.split('/')
        self.name = url_split[-1]
        self.output_path = output_dir + self.name

    def image_data(self):
        """Evaluates url to determine if content is image."""
        try:
            source = requests.head(self.url, allow_redirects=True)
            header = source.headers
            source_info = header.get('content-type').split('/')
            self.url = source.url

            if source_info[0] == 'image':
                self.is_image = True
                self.image_format = source_info[1]

            else:
                self.is_image = False

        except ValueError:
            self.is_image = False
            return

    def is_overwrite(self):
        """Takes in user's overwrite choice for when image already exists."""
        while True:
            answer = input(self.name + " already exists. Do you want to replace it? (y/n) ")

            if answer.lower() in ('y', 'yes'):
                self.overwrite = True
                break

            elif answer.lower() in ('n', 'no'):
                self.overwrite = False
                break

            else:
                print(f'Error: Input {answer} unrecognized. Please try again')

    def get_image(self, original_url):
        """Downloads the image."""
        try:
            urllib.request.urlretrieve(self.url, self.output_path)
            print("Downloading image from: " + original_url + " to: " + self.output_path)

        except FileNotFoundError as err:
            print(err)

        except HTTPError as err:
            print(err)


# Handles urls plaintext file
try:
    urls_txt = sys.argv[1]

    if mimetypes.guess_type(urls_txt)[0] != 'text/plain':
        print("Usage: " + sys.argv[1] + " not of type <text/plain>")
        sys.exit(1)

except IndexError:
    print("Usage: " + os.path.basename(__file__) + " <arg1>")
    sys.exit(1)


# Setup of output dir
out_path = input("Enter output folder path: ")
out_path = f'{Path(out_path)}{os.sep}'

try:
    os.mkdir(out_path)
except OSError as e:
    if e.errno != errno.EEXIST:
        print(f"Creation of the directory failed {out_path}")
        sys.exit(1)


# Analyzes the text line-by-line and sets image ID for corresponding image urls.
with open(urls_txt, 'r') as file:
    for line in file:

        line = line.rstrip()
        if not line:
            continue

        img = ImageId(line)
        img.image_data()

        if img.is_image is False:
            print(f"Error: Invalid image URL <{img.url}>")
            continue

        img.get_name(out_path)

        is_exist = os.path.isfile(img.output_path)
        if is_exist:
            img.is_overwrite()
            if img.overwrite is False:
                continue

        img.get_image(line)
