# ImagesDownloader
Downloads all images given by a plaintext file containing URLs

### Prerequisites
This version of the code runs successfully on Windows 10 and Ubuntu-18.04. Should also compile on other variants of linux and Windows. Other operating systems are currently not supported.

### How to use:
* Download ImagesDownloader.py (the other files are for testing purposes). You'll also need Python 3 interpreter installed. (Download Python 3 from [here](https://www.python.org/downloads/)).
* Install urllib and requests libraries.
* Provide (as a command-line argument) a plaintext file containing URLs with images.
* You will be prompt for an output directory, for storing the downloaded images.

Run this for downloading images
```python
python3 ImagesDownloader.py FILENAME.txt
```

### Features
* Ignores blank lines.
* Accepts all URLs and filters non-image objects.
* Deals with already-existing files with similar names.