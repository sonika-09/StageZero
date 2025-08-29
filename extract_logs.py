import py7zr
import os

seven_zip_path = r"C:\Users\suha_\Downloads\MDE_Investigation_Package.7z"
extract_path = "extracted_logs"

# Extract all files
with py7zr.SevenZipFile(seven_zip_path, mode='r', password="HackVerse") as archive:
    archive.extractall(path=extract_path)

print("Logs extracted to:", extract_path)






