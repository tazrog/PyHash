import hashlib
import sys

def calculate_hash(filename):
  try:
    with open(filename, 'rb') as file:
      data = file.read()
      hash_value = hashlib.sha256(data).hexdigest()
      print(f"The hash value of {filename} is: {hash_value}")
  except FileNotFoundError:
    print(f"File '{filename}' not found.")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Please provide a filename as an argument.")
  else:
    filename = sys.argv[1]
    calculate_hash(filename)