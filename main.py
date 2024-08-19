from zxcvbn import zxcvbn
import pprint, getpass, sys

def test_single_password():
    password = getpass.getpass("[?] Enter your password: ")
    result = zxcvbn(password)
    print(f"Value: {result['password']}")
    print(f"Password Score: {result['score']}/4")
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"Feedback: {result['feedback']['suggestions']}")


def test_multiple_passwords(password_file):
    try:
        with open(password_file, 'r') as passwords:
            for password in passwords:
                password = password.strip()  
                if password:  
                    result = zxcvbn(password)
                    print("\n") # for readability
                    print(f"Value: {result['password']}")
                    print(f"Password Score: {result['score']}/4")
                    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
                    print(f"Feedback: {result['feedback']['suggestions']}")
                    print("\n") # for readability
    except Exception as e:
        print(f'[!] Error: {str(e)}')


if len(sys.argv) == 2:
    test_multiple_passwords(sys.argv[1])
elif len(sys.argv) == 1:
    test_single_password()
else:
    print("\n[!] Usage: python3 main.py <file> (for a file containing passwords) or \
        \npython3 main.py (for a single password)")
