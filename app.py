import streamlit as st

st.set_page_config(page_title="PocketSmart-AI", page_icon="🤖")
st.title("PocketSmart-AI - Your Personal Assistant")

menu = st.sidebar.selectbox("Menu", ["Chat", "Notes", "Expenses"])

if menu == "Chat":
    st.header("AI Chat")
    user_input = st.text_input("Ask anything:")
    if user_input:
        st.success(f"PocketSmart AI says: You asked '{user_input}'. This is a smart offline reply!")

elif menu == "Notes":
    st.header("My Notes")
    note = st.text_area("Write your note")
    if st.button("Save Note"):
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        st.success("Note Saved!")

elif menu == "Expenses":
    st.header("Expense Tracker")
    amount = st.number_input("Amount", min_value=0)
    reason = st.text_input("For what?")
    if st.button("Add Expense"):
        st.success(f"Added {amount} for {reason}")
