"""
Simulation of PoW for a blockchain
"""
import hashlib
import time


def mine_block(data, difficulty):
    """
    Simulates the mining process by finding a valid hash for a given difficulty level.
    """
    # The target is a string of '0' repeated 'difficulty' times
    target = '0' * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        block_data = f"{data}{nonce}".encode()
        hash_hex = hashlib.sha256(block_data).hexdigest()

        if hash_hex.startswith(target):
            elapsed_time = time.time() - start_time
            return nonce, hash_hex, elapsed_time

        nonce += 1


def main():
    """
    Main function to test the mining process with different difficulty levels.
    """
    data = "Sample transaction block data"
    difficulties = [1, 2, 3, 4, 5, 6]

    for difficulty in difficulties:
        print(f"Mining with difficulty level: {difficulty}")
        nonce, hash_hex, elapsed_time = mine_block(data, difficulty)
        print(f"Nonce: {nonce}")
        print(f"Hash: {hash_hex}")
        print(f"Time taken: {elapsed_time:.4f} seconds\n")


if __name__ == "__main__":
    main()
