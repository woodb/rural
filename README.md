rural
=====

Simple command line utility for uploading files to AWS S3, copying a public link 
to that file to the clipboard.

Installation
------------
```
$ git clone https://github.com/woodb/rural.git
$ cd rural
$ sudo python setup.py install
$ rural --configure
```

Usage
-----
After configuring rural, you can upload any file via the following command:
```
$ rural myfile.pdf
$ 
```

This will put the public link to the file into the clipboard and is valid for 24 hours.
