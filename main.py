import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import random
import string
from Crypto.Cipher import AES, DES, Blowfish
from Crypto.Util.Padding import pad
import os

# Generate random plaintext
def generate_plaintext(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Encrypt plaintext using AES
def encrypt_aes(plaintext):
    key = os.urandom(32)  # AES-256
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext

# Encrypt plaintext using DES
def encrypt_des(plaintext):
    key = os.urandom(8)  # DES key must be 8 bytes
    iv = os.urandom(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return ciphertext
# # Encrypt plaintext using Blowfish
def encrypt_blowfish(plaintext):
    key = os.urandom(16)  # Blowfish key
    iv = os.urandom(8)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), Blowfish.block_size))
    return ciphertext

# Generate dataset with ciphertexts and labels
def generate_dataset(n_samples=100):
    algorithms = ['AES', 'DES' ,'Blowfish']
    data = []
    
    for _ in range(n_samples):
        algorithm = random.choice(algorithms)
        plaintext = generate_plaintext()
        
        if algorithm == 'AES':
            ciphertext = encrypt_aes(plaintext)
        elif algorithm == 'DES':
            ciphertext = encrypt_des(plaintext)
        elif algorithm == 'Blowfish':
            ciphertext = encrypt_blowfish(plaintext)
        data.append([ciphertext, algorithm])
    
    return data
# Feature extraction (based on ciphertext properties)
def extract_features(ciphertext):
    features = []
    features.append(len(ciphertext))  # Ciphertext length
    features.append(sum(c.isdigit() for c in ciphertext.hex()))  # Number of digits in ciphertext (hex)
    features.append(sum(c.isalpha() for c in ciphertext.hex()))  # Number of letters in ciphertext (hex)
    features.append(sum(c in 'abcdef' for c in ciphertext.hex()))  # Number of hex characters (a-f)
    return features

# Generate the dataset
dataset = generate_dataset(n_samples=1000)

# Convert dataset to a DataFrame
df = pd.DataFrame(dataset, columns=['ciphertext', 'algorithm'])

# Extract features from ciphertext
X = np.array([extract_features(ciphertext) for ciphertext in df['ciphertext']])
y = np.array(df['algorithm'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict the algorithms for the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Test with a new ciphertext (AES)
new_plaintext = generate_plaintext()
new_ciphertext=encrypt_aes(new_plaintext)
new_features = np.array([extract_features(new_ciphertext)])
predicted_algorithm = clf.predict(new_features)
print(f"Predicted algorithm: {predicted_algorithm[0]}")
