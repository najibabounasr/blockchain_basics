import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class Block:
    data: Any
    creator_id : int
    timestamp : str = datetime.utcnow().strftime("%H:%M:%S")

st.markdown("# PyBlock")
st.markdown("## Store Data in a Block")

input_data =  st.text_input("Block Data")

if st.button("Add Block"):
    st.write(input_data)
    new_block =  Block(
        data= input_data,
        creator_id=42,
        timestamp = datetime.utcnow().strftime("%H:%M:%S")
        )
    st.write(new_block)