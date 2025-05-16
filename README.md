# PulseSub

**PulseSub** is a fast Python CLI tool to check which subdomains are live and reachable.  
It’s ideal for bug bounty hunters, penetration testers, and anyone needing to filter a large list of subdomains.

---

## Features

- Accepts single domains, files, or piped input.
- Fast, concurrent checking using multiprocessing.
- Outputs live subdomains with their IP and HTTP status code.
- CLI flags for flexible usage and output customization.

---

## Requirements

- Python 3.x
- Python modules: `requests`, `multiprocessing`, `socket` (all standard except `requests`)
- A list of subdomains (e.g., `subdomains.txt`)

---

## Installation
```bash
pip install requests
```

---

## Usage

### 1. **Single Domain**
```bash
python3 pulsesub.py -t example.com
```

### 2. **From a File**
```bash
python3 pulsesub.py -f subdomains.txt
```

### 3. **Via Pipe**
```bash
cat subdomains.txt | python3 pulsesub.py
```

### 4. **Custom Output File & Concurrency**
```bash
python3 pulsesub.py -f subdomains.txt -o results.csv -c 8
```

---

## Example Output
![image](https://github.com/user-attachments/assets/25fcca10-ee22-48f5-8251-d020d884708d)

---

## License

(c) 2025 Aayush Samriya  
[MIT License](LICENSE)

---

## Author

[github.com/MAAYTHM](https://github.com/MAAYTHM)
