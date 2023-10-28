import os
import base64

# Generate a random JWT secret of 256 bits (32 bytes)
secret = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')

print(secret)
