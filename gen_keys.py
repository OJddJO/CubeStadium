import pickle
import pathlib
import streamlit_authenticator as sa

# Path to the file containing the secret key
SECRET_KEY_PATH = pathlib.Path("secret")

names = ["user1", "user2"]
username = ["user1", "user2"]
passwords = ["pass1", "pass2"]

hashed_passwords = sa.Hasher(passwords).generate()

file_path = pathlib.Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)