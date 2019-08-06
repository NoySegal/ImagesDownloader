import urllib.request
import requests
from urllib.error import HTTPError


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
