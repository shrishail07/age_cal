import streamlit as st
from datetime import date

# Set up page configuration
st.set_page_config(page_title="Age Calculator", page_icon="🎂", layout="centered")

# Title and description
st.title("🎂 Precision Age Calculator")
st.write("Enter your birthdate below to find out exactly how long you've been around in years, months, and days!")

st.markdown("---")

# User Input: Date of Birth
# We set a reasonable minimum date (120 years ago) and maximum date (today)
today = date.today()
min_date = date(today.year - 120, 1, 1)

birth_date = st.date_input(
    "Select your Date of Birth:",
    value=date(2000, 1, 1), # Default value
    min_value=min_date,
    max_value=today
)

st.markdown("---")

# Calculation Logic
if st.button("Calculate Age", type="primary"):
    if birth_date > today:
        st.error("The date of birth cannot be in the future!")
    else:
        # Calculate initial differences
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        # Adjust for negative days
        if days < 0:
            # Go back one month
            months -= 1
            # Find the last day of the previous month to borrow days properly
            # We calculate this by finding the difference between the 1st of this month 
            # and the 1st of last month
            if today.month == 1:
                prev_month_year = today.year - 1
                prev_month = 12
            else:
                prev_month_year = today.year
                prev_month = today.month - 1
                
            # Total days in that previous month
            days_in_prev_month = (date(today.year, today.month, 1) - date(prev_month_year, prev_month, 1)).days
            days += days_in_prev_month

        # Adjust for negative months
        if months < 0:
            years -= 1
            months += 12

        # Display results nicely
        st.success("Calculation Complete!")
        
        # Grid layout for displaying the breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="Years", value=years)
        with col2:
            st.metric(label="Months", value=months)
        with col3:
            st.metric(label="Days", value=days)
            
        # Fun extra: Total days milestone
        total_days = (today - birth_date).days
        st.info(f"🎉 You have been alive for a grand total of **{total_days:,}** days!")
