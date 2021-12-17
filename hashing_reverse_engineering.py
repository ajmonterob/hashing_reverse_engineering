#Created by Andres Montero
import hashlib
import secrets
import base64
import json

def main():
    print("\nThis program allow you to identify the correct SHA-1 hashing, in case you need to confirm the password but only having the salt as base64URL \n")
    print("Please refer to the following document for the hashing process: https://developer.okta.com/blog/2021/03/05/ultimate-guide-to-password-hashing-in-okta  \n")
    print("If you used the code in the previous link to hash your password you should have an output similiar to this one: \n ")
    print( "\n" + "{" + "\n" 
    " algorithm: \"SHA-1\"," + "\n"
    " salt: \"WtAA0AREjKfKRDTCrskd9A==\", " + "\n"
    " saltOrder: \"POSTFIX\", " + "\n"
    " value: \"PrL6zaCRxFqduROMbABkZKphDUw=\" " + "\n" + "}" )
    print("\nPlease use introduce the following information using the quotes as in the example output.")

    #Requesting information to the user. 
    password = input("\nPlease enter the password in plain text: ")
    salt_in_base64URL_ascii = input("Please enter the salt value: ")
    salt_order = input("Please enter the salt order: ")

    #decoding password to bytes-like object.
    salt = base64.b64decode(salt_in_base64URL_ascii)
    postfix = '"POSTFIX"'

    print( "\nThe result of decoding the base64URL salt to bytes-like object is : " + str(salt) + "\n")


    #Selecting the result base on the salt order. 
    if salt_order == '"POSTFIX"' :
        salted_password = bytes(password, "utf-8") + salt
        hashed = hashlib.sha1(salted_password)
        result = {
        "algorithm": "SHA-1",
        "salt": base64.b64encode(salt).decode("ascii"),
        "saltOrder": "POSTFIX",
        "value": base64.b64encode(hashed.digest()).decode("ascii"),
        }
        print(json.dumps(result, indent=4))
    elif salt_order == '"PREFIX"':
        salted_password = salt + bytes(password, "utf-8")
        hashed = hashlib.sha1(salted_password)
        result = {
        "algorithm": "SHA-1",
        "salt": base64.b64encode(salt).decode("ascii"),
        "saltOrder": "PREFIX",
        "value": base64.b64encode(hashed.digest()).decode("ascii"),
        }
        print(json.dumps(result, indent=4))
    else  :
        print("The order value was incorrect please enter \"POSTFIX\" or \"PREFIX\" ")


if __name__ == "__main__":
    main()

 
