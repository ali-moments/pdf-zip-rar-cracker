#!/usr/bin/python3
import zipfile
from tqdm import tqdm
import sys

try:
    zip_file = sys.argv[1]
    wordlist = sys.argv[2]
except:
        # the password list path you want to use, must be available in the (current directory)/(path)
        wordlist = input("[#] Enter Passwordlist name/path: ")
        # the zip file you want to crack its password, must be available in the (current directory)/(path)
        zip_file = input("[#] Enter ZipFile name/path: ")

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("[$] Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)

print("[!] Password not found, try other wordlist.")
