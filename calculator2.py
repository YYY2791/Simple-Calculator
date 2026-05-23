import streamlit as st

# 1. App Title
st.title("Simple Streamlit Calculator")
st.write("---")

# 2. User Input Fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# 3. Operation Selection
operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# 4. Calculation Logic
result = 0
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None

    # 5. Display Result
    if result is not None:
        st.success(f"The result is: {result}")