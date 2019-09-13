import subprocess
import os
from github_config import *

example_url = github_url + "/this_right_here"


print("what url do you want to shorten?")

url_to_shorten = input("url: http://")
shortened_url = input("shortened url location " + example_url + ":")

to_write = shortened_url + "/index.html"

if os.path.exists(to_write):
    print("unfortunately you have already shortened something to that url :(")

os.mkdir(shortened_url)

index = open(to_write, "w")

index.write("<meta http-equiv=\"refresh\" content=\"0; URL=\'http://" + url_to_shorten + "\'\" />")

index.close()

os.system("git add .")
os.system("git commit -m " + "\"shortening " + url_to_shorten + " to " + shortened_url + " \"")
os.system("git push")
# print(subprocess.check_output(["git", "add", "."]))
# print(subprocess.check_output(["git", "commit", "-m", "\"shortening " + url_to_shorten + " to " + shortened_url + " \""]))

print("url has been shortened to:", github_url + "/" + shortened_url)
