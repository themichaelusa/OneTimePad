# OneTimePad

A little script I threw together in an hour for generating a [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad). Very simple to use. Use at your own risk.

## Usage
```python
otp = OneTimePad()
secret = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
otp.encrypt(secret)

...

Terminal Outputs:
PAD_NAME: b'U\x94\nDT\xbb\xac\xe4R\x8b\xf9O\xe3\xeb:\x8e'.txt
PAD_LOCATION: /Users/michaelusa/Desktop
```
