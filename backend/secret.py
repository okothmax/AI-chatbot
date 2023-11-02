import os
import base64

# Generate a random JWT and Cookie  secret of 256 bits (32 bytes)
jwt_secret = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
cookie_secret = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print(f"The jwt_secret is: {jwt_secret[:-2]}")
print(f"The cookie_secret is: {cookie_secret[:-2]}")

