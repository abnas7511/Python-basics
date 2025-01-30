import bencode

# Check for specific deprecation warnings. Some libraries have their own ways of signaling deprecation.
# Example (not universal):
if hasattr(bencode, '__deprecated__'):
    print(f"{bencode} is deprecated: {bencode.__deprecated__}")