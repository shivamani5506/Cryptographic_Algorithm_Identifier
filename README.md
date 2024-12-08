# Ciphertext Classification Using Machine Learning

This repository provides an implementation of a machine learning model that classifies the encryption algorithm used for ciphertext generation. The project demonstrates how Random Forest can analyze ciphertext features to predict whether AES, DES, or Blowfish encryption was used.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Requirements](#requirements)
7. [Example Output](#example-output)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

This project simulates a dataset of ciphertexts generated using three encryption algorithms:
- **AES (Advanced Encryption Standard)**
- **DES (Data Encryption Standard)**
- **Blowfish**

Using features extracted from the ciphertext, a machine learning model (Random Forest) is trained to classify the encryption algorithm used.

---

## Features

- **Dataset Generation:**
  - Random plaintext generation.
  - Ciphertext generation using AES, DES, and Blowfish encryption.
- **Feature Extraction:**
  - Ciphertext length.
  - Count of digits, letters, and hex-specific characters in the ciphertext.
- **Model Training:**
  - Train a Random Forest classifier to predict the encryption algorithm.
- **Evaluation:**
  - Measure model accuracy on a test set.
  - Test prediction on new ciphertexts.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ciphertext-classification.git
   cd ciphertext-classification
   ```

2. Install the required Python libraries:
   ```bash
   pip install numpy pandas scikit-learn pycryptodome
   ```

---

## Usage

1. **Run the script:**
   ```bash
   python ciphertext_classification.py
   ```

2. **Output Includes:**
   - Model accuracy.
   - Predicted encryption algorithm for a new ciphertext.

---

## How It Works

### 1. **Dataset Generation:**
- Generate random plaintext of fixed length.
- Encrypt plaintext using randomly chosen algorithms (AES, DES, Blowfish).
- Store ciphertext and corresponding algorithm label.

### 2. **Feature Extraction:**
Features extracted from ciphertext include:
- Length of ciphertext.
- Count of digits and letters in hexadecimal representation.
- Count of characters from `a-f` in hexadecimal representation.

### 3. **Model Training:**
- Train a Random Forest Classifier on the extracted features.
- Evaluate model accuracy on a test set.

### 4. **New Prediction:**
- Generate new ciphertext using AES.
- Extract features and predict the encryption algorithm.

---

## Requirements

- **Python 3.7+**
- **Libraries:**
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `pycryptodome`

---

## Example Output

```plaintext
Accuracy: 95.75%
Predicted algorithm: AES
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

