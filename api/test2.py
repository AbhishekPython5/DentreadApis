# import pydicom
# import zipfile
# from io import BytesIO
#
# def check_dicom_files_in_zip(zip_file_path):
#     dicom_extensions = ['.dcm', '.ima', '.dicom']
#
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
#         for name in zip_file.namelist():
#             if any(name.lower().endswith(ext) for ext in dicom_extensions):
#                 with zip_file.open(name) as file:
#                     try:
#                         dicom_file = pydicom.dcmread(BytesIO(file.read()))
#                         print('dicom_file length', len(dicom_file))
#
#                         return True
#                     except pydicom.errors.DicomError:
#                         print(f"{name} is not a valid DICOM file.")
#
#
# zip_file_path = r'C:\Users\abhis\Downloads\Ashok.zip'
# d = check_dicom_files_in_zip(zip_file_path)
# print('d',d)


import random
import string

def generate_unique_key(length):
    characters = string.ascii_letters + string.digits
    unique_key = ''.join(random.choice(characters) for _ in range(length))
    return unique_key

# Generate a unique key with a length of 30
key = generate_unique_key(50)
print(key)
