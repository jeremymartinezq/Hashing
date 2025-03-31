import hashlib

def sha256_hash(input_string):
    """Returns the SHA256 hash of the input string in hexadecimal format."""
    return hashlib.sha256(input_string.encode()).hexdigest()

def find_nonce(first_names, max_leading_zeros=10):
    """Finds a nonce that produces a hash with the specified number of leading zeros."""
    nonce = 0
    leading_zeros_target = '0' * max_leading_zeros  # Creates a string of target leading zeros
    while True:
        # Create the input string with the nonce
        input_string = f"{first_names} {nonce}"
        # Calculate the hash
        hash_output = sha256_hash(input_string)
        # Check if the hash has the desired number of leading zeros
        if hash_output.startswith(leading_zeros_target):
            return nonce, hash_output  # Return the found nonce and its hash
        nonce += 1  # Increment nonce and try again

# Example usage
if __name__ == "__main__":
    team_names = "Alice Bob Charlie"  # Replace with your actual team names
    nonce, hash_output = find_nonce(team_names)
    print(f"Input string: {team_names} {nonce}")
    print(f"Hash output: {hash_output}")
