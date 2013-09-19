#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rural
~~~~~
Simple command line utility for uploading local files to Amazon Web Services
(AWS) Simple Storage Service (S3).
"""

__author__ = "Brandon Wood"
__copyright__ = "Copyright 2013, Brandon Wood"
__license__ = "BSD"

__version__ = "0.0.1"
__maintainer__ = "Brandon Wood"
__email__ = "btwood+rural@h6o6.com"
__status__ = "Development"


CONFIG_MISSING_MESSAGE = """rural has not yet been configured, or the configuration 
file appears to be missing. Run the configuration wizard with `rural --configure`
"""

def _create_config(fh):
    """
    rural._create_config
    ~~~~~~~~~~~~~~~~~~~~
    Prompts to create the configuration file.
    """
    sys.stdout.write("AWS Access Key ID: ")
    aws_access_key = raw_input().upper()

    sys.stdout.write("   AWS Secret Key: ")
    aws_secret_key = raw_input().upper()

    sys.stdout.write("   Default Bucket: ")
    default_bucket_name = raw_input()

    fh.write(yaml.dump({'aws_access_key' : aws_access_key,
               'aws_secret_key' : aws_secret_key,
               'bucket_name'    : default_bucket_name},
               Dumper=Dumper))


def _load_config(fh):
    cfg_data = yaml.load(fh)
    return cfg_data['aws_access_key'], cfg_data['aws_secret_key'], \
        cfg_data['bucket_name']


def _main():
    """
    rural._main
    ~~~~~~~~~~~
    Handles option parsing, configuration management and command execution.
    """

    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="name of file to upload", nargs=1,
            default=None)
    parser.add_argument("--configure", dest="configure", action="store_true")
    args = parser.parse_args()
    filename = args.filename[0]

    config_file = None
    if os.getenv("HOME"):
        config_file = os.path.join(os.getenv("HOME"), ".rural")
    else:
        raise NotImplementedError, "rural currently only supports POSIX \
            compliant environments (i.e. rural does not work on Windows)"
        sys.exit(1)
    try:
        config_fh = open(config_file, "r")
    except IOError:
        if not args.configure:
            print CONFIG_MISSING_MESSAGE
            sys.exit(1)
    
    if args.configure:
        config_fh = open(config_file, 'w')
        _create_config(config_fh)
        config_fh.seak(0)

    # Upload to S3
    aws_access_key, aws_secret_key, bucket_name = _load_config(config_fh)
    if bucket_name and aws_access_key and aws_secret_key:
        from boto.s3.connection import S3Connection
        from boto.s3.key import Key

        s3conn = S3Connection(aws_access_key_id=aws_access_key,
                    aws_secret_access_key=aws_secret_key)
        bucket = s3conn.get_bucket(bucket_name)

        k = Key(bucket)
        k.key = filename
        k.set_contents_from_filename(filename)
        k.make_public()

        url = k.generate_url(86400)
        
        xerox.copy(url)
    else:
        raise ValueError, "AWS configuration incomplete"
        sys.exit(1)


if __name__ == '__main__':
    import os
    import sys

    import xerox
    import yaml
    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    except Exception as exc:
        raise exc
        sys.exit(1)

    _main()