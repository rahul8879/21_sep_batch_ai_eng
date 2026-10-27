import streamlit as st
import pandas as pd
import json
from pipeline import process_email
st.title("Email Classifier Use Case")


# step 1 : Upload file

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv","json"])

if uploaded_file is not None:
    # step 2 : 
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            data = json.load(uploaded_file)
            df = pd.DataFrame(data)

        required_columns = ['subject', 'body', 'sender']
        if not all(col in df.columns for col in required_columns):
            st.error("File must contain : subject, body, sender")
            st.stop()
        st.subheader("Uploaded Data")
        # step 3: Process emails

        if st.button('Process email',type='primary'):
            results = []
            progress = st.progress(0)
            for index,row in df.iterrows():
                email = {
                    "subject": row['subject'],
                    "body": row['body'],
                    "sender": row['sender']
                }
                try:
                    result = process_email(email)
                    results.append(result)
                except Exception as e:
                    results.append(
                        {"email_id": email["sender"],
                        "classification": "Error",
                        "routed_to": None,
                        "drafted_response": str(e)}
                    )

                progress.progress((index + 1) / len(df))

            # step 4 save the results
            result_df = pd.DataFrame(results)
            st.session_state['results'] = result_df
            st.success("Email processing completed!")


    except Exception as e:
        st.error(f"Error reading file: {e}")
    


# step 5 : Display and download
if "results" in st.session_state:
    result_df = st.session_state['results']
    st.subheader("Processed Results")
    st.dataframe(result_df,use_container_width=True)

    # download CSV
    csv = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
       label="Download CSV",
       data=csv,
       file_name="processed_emails.csv",
       mime="text/csv"
   )
    
    json_data = result_df.to_json(orient="records").encode('utf-8')
    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name="processed_emails.json",
        mime="application/json"
    )

