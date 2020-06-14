import subprocess
import os
from github_config import *

example_url = github_url + "/this_right_here"


print("what url do you want to shorten?")

url_to_shorten = input("url to be shortened: http(s)://")
shortened_url = input("shorten to " + github_url + "/")

to_write = path_to_repo + "/" + shortened_url + "/index.html"

if os.path.exists(to_write) or os.path.exists(path_to_repo + "/" + shortened_url):
    print("unfortunately you have already shortened something to that url :(")

os.mkdir(path_to_repo + "/" + shortened_url)

index = open(to_write, "w+")

index.write("<meta http-equiv=\"refresh\" content=\"0; URL=\'http://" +
            url_to_shorten + "\'\" />")

index.close()

print("doing some stuff....")

current_directory = os.getcwd()
os.chdir(path_to_repo)

os.system("git add . > /dev/null 2>&1")
os.system("git commit -m " + "\"shortening " + url_to_shorten +
          " to " + github_url + "/" + shortened_url + "/\" > /dev/null 2>&1")
os.system("git push > /dev/null 2>&1")

os.chdir(current_directory)

print("url has been shortened to:", github_url + "/" + shortened_url + "/")
print("it might take ~5 mins for the link to become active")
