# Dynamic File Compression Utility

## 📌 Overview

Dynamic File Compression Utility is a Data Structures and Algorithms (DSA) project that implements **Huffman Coding**, a lossless data compression algorithm used to reduce file size while preserving the original content.

The project reads a text file, calculates character frequencies, constructs a Huffman Tree using a Min Heap (Priority Queue), generates optimal binary codes, compresses the file, and successfully decompresses it back to its original form.

This project demonstrates practical applications of:

* Hash Maps (Frequency Counting)
* Priority Queues / Min Heaps
* Binary Trees
* Recursion
* Greedy Algorithms
* File Handling

---

## 🎯 Problem Statement

Large files consume more storage space and require more bandwidth during transmission.

The objective of this project is to:

* Reduce file size efficiently
* Preserve original data integrity
* Demonstrate DSA concepts through a real-world application
* Build a reusable file compression and decompression utility

---

## 🚀 Features

✅ File Reading and Processing

✅ Character Frequency Calculation

✅ Huffman Tree Construction

✅ Huffman Code Generation

✅ File Compression

✅ File Decompression

✅ Compression Ratio Calculation

✅ Verification of Data Integrity

✅ Command-Line Execution

✅ GitHub Portfolio Ready

---

## 🧠 DSA Concepts Used

### 1. Hash Map (Dictionary)

Used to store character frequencies.

Example:

```python
frequency[char] += 1
```

---

### 2. Priority Queue / Min Heap

Used to repeatedly extract the two nodes with the smallest frequencies.

Python Module:

```python
heapq
```

---

### 3. Binary Tree

The Huffman Tree is constructed using binary tree nodes.

```text
        Root
       /    \
      A      *
            / \
           B   C
```

---

### 4. Recursion

Used to generate Huffman codes by traversing the Huffman Tree.

---

### 5. Greedy Algorithm

Huffman Coding follows a greedy strategy by always combining the two least frequent nodes first.

---

## ⚙️ Workflow

```text
Input File
    │
    ▼
Read File Content
    │
    ▼
Calculate Character Frequencies
    │
    ▼
Build Min Heap
    │
    ▼
Construct Huffman Tree
    │
    ▼
Generate Huffman Codes
    │
    ▼
Compress File
    │
    ▼
Compressed Output
    │
    ▼
Decompress File
    │
    ▼
Original File Restored
```

---

## 🏗️ Project Architecture

```text
                 INPUT FILE
                       │
                       ▼
             Read File Content
                       │
                       ▼
          Character Frequency Count
                       │
                       ▼
                Create Min Heap
                       │
                       ▼
               Build Huffman Tree
                       │
                       ▼
            Generate Huffman Codes
                       │
                       ▼
                Compress Data
                       │
                       ▼
             Compressed File (.bin)
                       │
                       ▼
                Decompress File
                       │
                       ▼
              Original Text Output
```

---

## 📂 Folder Structure

```text
Dynamic-File-Compression-Utility/
│
├── input_files/
│   └── sample.txt
│
├── compressed_files/
│   └── compressed.bin
│
├── decompressed_files/
│   └── output.txt
│
├── docs/
│
├── images/
│
├── outputs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## 💻 Technologies Used

* Python 3
* Heapq
* Collections (Counter)
* File Handling
* Object-Oriented Programming

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/dynamic-file-compression-utility.git
```

### Navigate to Project Folder

```bash
cd dynamic-file-compression-utility
```

### Run the Project

Windows:

```bash
python main.py
```

Linux / macOS:

```bash
python3 main.py
```

---

## 📄 Sample Input

File: `sample.txt`

```text
DATA STRUCTURES AND ALGORITHMS ARE IMPORTANT IN COMPUTER SCIENCE
```

---

## 📊 Sample Output

```text
Frequency Table:

Counter({' ': 8, 'T': 7, 'A': 6, 'R': 6, 'E': 5})

Huffman Codes:

'R' : 000
'T' : 010
'A' : 1111

Compression Statistics
----------------------
Original Size : 512 bits
Compressed Size : 250 bits
Compression Ratio : 48.83 %

Verification:
True
```

---

## 📈 Results

| Metric            | Value    |
| ----------------- | -------- |
| Original Size     | 512 bits |
| Compressed Size   | 250 bits |
| Compression Ratio | 48.83%   |
| Space Saved       | 51.17%   |
| Data Integrity    | Verified |

---

## 📸 Screenshots

Add screenshots inside the `images/` folder.

Suggested screenshots:

### Project Structure

```text
images/project-structure.png
```


### Frequency Table Output

```text
images/frequency-table.png
```

### Huffman Codes Output

```text
images/huffman-codes.png
```

### Compression Statistics

```text
images/compression-ratio.png
```

### GitHub Repository Preview

```text
images/github-preview.png
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* How lossless compression works
* Practical implementation of Huffman Coding
* Building and traversing Binary Trees
* Using Priority Queues effectively
* Applying Greedy Algorithms
* File Compression and Decompression Concepts
* Python File Handling
* Git and GitHub Project Management

---

## 🔮 Future Enhancements

* Real Binary File Compression
* GUI Application
* Multiple File Compression
* Folder Compression
* Compression Analytics Dashboard
* Multi-threaded Compression
* Support for ZIP, GZIP, Brotli, and Zstandard
* Cross-Platform CLI Tool

---

## 👨‍💻 Author

**Sinchana Gowda**

Aspiring Software Developer | DSA Enthusiast | Backend Developer

---

## ⭐ If you found this project useful

Give this repository a star and feel free to fork it for learning and experimentation.
