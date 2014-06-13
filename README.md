rural
=====

Simple command line utility for uploading files to Amazon Web Services (AWS)
Simple Storage Service (S3) and copying a public link to that file to the
clipboard.

Installation
------------
```zsh
pip install rural
```

Usage
-----
Once ```rural``` has been configured, it's a simple command line interface.

```zsh
$ rural myfile.pdf
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
$ pbpaste
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
```

```rural``` also supports piped input from stdin, so long as it's UTF-8 
encodable.

```zsh
$ < myfile.txt | rural -f myfile.txt
https://my-s3-bucket.s3.amazonaws.com/myfile.txt
$ pbpaste
https://my-s3-bucket.s3.amazonaws.com/myfile.txt
```

To show more information, you can use multiple verbosity flags.

```zsh
$ rural -vv -b my-other-bucket myfile2.pdf
AWS Access Key ID:	LsUCBGhw7qZZLUmlmhvtX
AWS Secret Access Key:	mKDbRLKUmhocgVepept6QRLDv6GkBkNG1AxOnr
Bucket:	my-other-bucket
[========================================] 100%
https://my-other-bucket.s3.amazonaws.com/myfile2.pdf
```

For other options, use the ```--help``` flag.


Configuration
-------------
```rural``` requires both an AWS access key ID and AWS secret access key that
allow for access to a specified S3 bucket. 

You can configure rural with environment variables ```AWS_ACCESS_KEY_ID```,
```AWS_SECRET_ACCESS_KEY```, and ```RURAL_BUCKET_NAME```. We recommend that
you set these in your environment configuration files (e.g. ```~/.zshrc```).

```zsh
$ export AWS_ACCESS_KEY_ID=LsUCBGhw7qZZLUmlmhvtX
$ export AWS_SECRET_ACCESS_KEY=mKDbRLKUmhocgVepept6QRLDv6GkBkNG1AxOnr
$ export RURAL_BUCKET_NAME=my-s3-bucket
$ rural myfile.pdf
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
$ pbpaste
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
```

Additionally, ```rural``` configuration can be overridden at runtime.

```zsh
$ rural --aws-access-key-id=LsUCBGhw7qZZLUmlmhvtX \
> --aws-secret-access-key=mKDbRLKUmhocgVepept6QRLDv6GkBkNG1AxOnr \
> --bucket-name=my-s3-bucket \
> myfile.pdf
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
$ pbpaste
https://my-s3-bucket.s3.amazonaws.com/myfile.pdf
```

Compatibility
-------------
```rural``` requires Python 2.6 or higher, and might not work on Windows.
