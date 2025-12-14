import hashlib
import re

# Hashes a password using SHA-256 for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Checks if a provided password matches the stored hash
def verify_password(stored_hash, password):
    return stored_hash == hashlib.sha256(password.encode()).hexdigest()

# Validates that the package ID follows the correct format (uppercase letters, numbers, dashes)
def validate_package_id(package_id):
    pattern = r"^[A-Z0-9-]{6,20}$"
    return re.match(pattern, package_id) is not None
