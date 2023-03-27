import argparse
import hashlib

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="Calculate the SHA-256 hash of a message")

# add an argument for the message to be hashed
parser.add_argument(
    "-m", "--message", type=str, help="the message to be hashed", required=True
)

# parse the command-line arguments
args = parser.parse_args()

# get the message from the command-line arguments
message = args.message

# create a SHA-256 hash object
hash_object = hashlib.sha256()

# update the hash object with the message
hash_object.update(message.encode("utf-8"))

# get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

# print the hash
print(hex_dig)
