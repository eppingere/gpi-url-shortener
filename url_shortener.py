import subprocess
import os
from github_config import *


print("what url do you want to shorten?")

url_to_shorten = input("url:")
shortened_url = input("shortened url:")

to_write = shortened_url + "/index.html"

if os.path.exists(to_write):
    print("unfortunately you have already shortened something to that url :(")

os.mkdir(shortened_url)

index = open(to_write, "w")

index.write("<meta http-equiv=\"refresh\" content=\"0; URL=\'" + url_to_shorten + "\'\" />")

index.close()

subprocess.check_output(["git", "add", "."])
subprocess.check_output(["git", "commit", "-m", "\"shortening " + url_to_shorten + " to " + shortened_url + " \""])

print("url has been shortened to:", github_url + "/" + url_to_shorten)
