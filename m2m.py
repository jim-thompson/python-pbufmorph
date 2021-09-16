#! /usr/bin/env python3

import subprocess
import re
import time

match_regex = re.compile("mailto:.*")

def pbpaste():
    paste_buffer_bytes = subprocess.check_output("pbpaste")
    paste_buffer_string = paste_buffer_bytes.decode("utf-8")
    return paste_buffer_string

def pbcopy(string_to_paste):
    bytes_to_paste = string_to_paste.encode("utf-8")
    subprocess.run(["pbcopy"], input=bytes_to_paste)

if __name__ == "__main__":
    while True:
        maybe_mailto_link = pbpaste()
        if re.match(match_regex, maybe_mailto_link):
            mailto_link = maybe_mailto_link[7:]
            print(mailto_link)
            pbcopy(mailto_link)
        time.sleep(1)

