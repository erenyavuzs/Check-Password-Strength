# Password Strength Tester

This Python script evaluates the strength of passwords using the `zxcvbn` module. It provides detailed feedback on password strength, estimated crack time, and suggestions for improvement. The script can analyze either a single password entered by the user or multiple passwords provided in a file.

## Features

- **Single Password Testing**: Prompt the user to enter a password and receive an immediate assessment of its strength.
- **Multiple Password Testing**: Analyze multiple passwords from a file, providing detailed feedback for each one.
- **Comprehensive Feedback**: The script offers password strength scores, estimated crack times, and suggestions for improving weak passwords.

## Usage

1. **Test a Single Password**:
    ```bash
    python3 main.py
    ```

   You'll be prompted to enter a password, and the script will evaluate its strength.

2. **Test Multiple Passwords from a File**:
    ```bash
    python3 main.py <file>
    ```

   Replace `<file>` with the path to your file containing a list of passwords (one password per line). The script will analyze each password in the file.

## Requirements

- Python 3.x
- `zxcvbn` module

## Installation

To install the required `zxcvbn` module, run:
```bash
pip install zxcvbn
```

## Example Output
For a single password: <br>
```bash
[?] Enter your password: 
Value: 123456
Password Score: 0/4
Crack Time: less than a second
Feedback: ['Add another word or two. Uncommon words are better.']
```

<br>

For multiple passwords: <br>
```bash
Value: aeds_7543
Password Score: 3/4
Crack Time: 3 hours
Feedback: []




Value: uuuuuuuuuuuu
Password Score: 0/4
Crack Time: less than a second
Feedback: ['Add another word or two. Uncommon words are better.', 'Avoid repeated words and characters.']




Value: 12345678
Password Score: 0/4
Crack Time: less than a second
Feedback: ['Add another word or two. Uncommon words are better.']
```

<br>

## Notes 

• Ensure your password file has one password per line.

• The script provides a password strength score from 0 to 4, with 4 being the strongest.

• Estimated crack times are provided based on common password cracking scenarios.
