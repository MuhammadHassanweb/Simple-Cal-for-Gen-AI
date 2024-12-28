import streamlit as st

# Streamlit App for a Simple Calculator
st.title("Simple Calculator")
st.write("Perform basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.")

# User input for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# User input for the operation
operation = st.radio("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
