# Password Complexity Checker

This Python script evaluates the strength of a password based on various criteria.

## Features

- **Length Check:** Ensures the password is at least 8 characters long.
- **Uppercase Check:** Requires at least one uppercase letter.
- **Lowercase Check:** Requires at least one lowercase letter.
- **Digit Check:** Requires at least one digit.
- **Special Character Check:** Requires at least one special character from `!@#$%^&*()_-+=<>?./`.

## Usage

1. **Running the Script:**
   - Make sure you have Python installed on your system.
   - Clone this repository or download the `PRODIGY_CS_03(Password Complexity Checker).py` file.

2. **Executing the Script:**
   - Open your terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script by entering:
     ```
     python PRODIGY_CS_03(Password Complexity Checker).py
     ```

3. **Enter Your Password:**
   - When prompted, enter the password you want to check.

4. **Evaluation:**
   - The script will evaluate the password based on the following criteria:
     - Minimum length of 8 characters.
     - At least one uppercase letter.
     - At least one lowercase letter.
     - At least one digit.
     - At least one special character.

5. **Result:**
   - If the password meets all criteria, it will display:
     ```
     Password is strong!
     ```
   - If any criteria are not met, it will display:
     ```
     Password is weak. Please ensure it meets all criteria.
     ```

## Example

Suppose you run the script and enter the password `SecurePwd123!`. The script will output: Password is strong!

## Notes

- Adjust the special characters list (`special_chars`) in the script if your password policy requires different characters.
- Feel free to modify the script to include additional password complexity rules as per your specific security requirements.

Feel free to explore, use, and modify this script according to your needs. If you have any questions or suggestions, please don't hesitate to reach out.

