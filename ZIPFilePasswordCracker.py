import zipfile
import argparse

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def brute_force_zip(zip_file_path, wordlist_path):
    zip_file = zipfile.ZipFile(zip_file_path)
    with open(wordlist_path, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()
            if extract_zip(zip_file, password):
                print(f"[+] Password found: {password}")
                return
    print("[-] Password not found.")

def main():
    parser = argparse.ArgumentParser(description='Brute-force ZIP file password cracker.')
    parser.add_argument('zipfile', help='Path to the ZIP file')
    parser.add_argument('wordlist', help='Path to the wordlist file')
    args = parser.parse_args()

    brute_force_zip(args.zipfile, args.wordlist)

if __name__ == '__main__':
    main()
