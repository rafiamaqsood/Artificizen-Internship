from security import hash_password, verify_password

password = "abc123"

hashed_password = hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed_password)

result = verify_password(password, hashed_password)

print("Password Verified:", result)