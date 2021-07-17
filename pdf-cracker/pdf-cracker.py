import pikepdf
from tqdm import tqdm
import sys

try:
    pdf_file = sys.argv[1]
    wordlist = sys.argv[2]
except:
        # the password list path you want to use, must be available in the (current directory)/(path)
        wordlist = input("[#] Enter Passwordlist name/path: ")
        # the pdf file you want to crack its password, must be available in the (current directory)/(path)
        pdf_file = input("[#] Enter pdfFile name/path: ")
        
# load password list
passwords = [ line.strip() for line in open(wordlist) ]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open(pdf_file, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
