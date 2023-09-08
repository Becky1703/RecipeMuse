from passlib.context import CryptContext

# Initialize Passlib's CryptContext with the desired hash algorithm(s)
crypt_context = CryptContext(schemes=["pbkdf2_sha256"])

# Hash a password
password = "bus"
hashed_password = crypt_context.hash(password)

# Verify a password
is_verified = crypt_context.verify(password, hashed_password)

if is_verified:
    print("Password is verified.")
else:
    print("Password verification failed.")
