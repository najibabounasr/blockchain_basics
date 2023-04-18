import hashlib
import streamlit as st

def hash_data(data):
    sha = hashlib.sha256()
    encoded_data = str(data).encode()
    sha.update(encoded_data)
    return (sha.hexdigest())

st.markdown("# Application for hashing data")

input_data = str(st.text_area("User Data")).encode()

st.write(f"Input Length: {len(input_data)}")

if st.button("Hash Text"):
    input_hashed = hash_data(input_data)
    st.write(f"The Output hash (fingerprint): {input_hashed}")
    st.write(f"The Output Length is: {len(input_hashed)}")
