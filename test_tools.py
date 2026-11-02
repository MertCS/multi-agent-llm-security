
from tools import read_document, send_email

print("Testing read_document:")
print(read_document("doc1"))

print("\nTesting send_email:")
print(send_email("test@example.com", "This is a test email."))
