import streamlit as st
import requests

st.set_page_config(
    page_title="DE pipeline Investigator",
    layout='wide',
)

st.title("Pipeline Investigator")
st.write("upload your data and Investigate the Pipeline failures")
st.divider()


left,right=st.columns([1,2])

with left:
    st.subheader("1.Upload file")
    upload_file= st.file_uploader(
        "upload csv files",type=["csv",'json']
    )
    if upload_file is not None:
        st.success(f"File Uploaded:{upload_file.name}")
        if st.button("upload to pipeline"):
            response=requests.post("http://127.0.0.1:8000/upload",
            files={
                "file": (
                    upload_file.name,
                    upload_file.getvalue(),
                    upload_file.type
                )
            })
        #run_pipeline=st.button("Run Pipeline", use_container_width=True)
        if st.button("Run_Pipeline", use_container_width=True):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/run_pipeline",
                    params={"filename": upload_file.name},
                    timeout=300
                )

                if response.ok:
                    st.success("Pipeline completed!")
                    st.json(response.json())
                else:
                    st.error(f"Pipeline failed: {response.status_code}")
                    st.code(response.text)

            except requests.RequestException as e:
                st.error(f"Could not connect to FastAPI: {e}")

    else:
        st.info("Please upload the file.")
        
    st.divider()
    
    st.subheader(" Pipeline status")
    st.write("Extract")
    st.write("Transform")
    st.write("validate")
    st.write("load")
    
    
    
with right:
    st.subheader("Investigation")

    if upload_file is None:
        st.info(
            "Please upload a file and run the pipeline "
            "to see investigation results."
        )
    elif Run_Pipeline:
        st.warning("Pipeline execution will be connected next")

        st.markdown("### Root Cause")
        st.write("AI investigation results will appear here.")

        st.markdown("### Evidence")
        st.write(
            "Pipeline logs, SQL results and data-quality "
            "checks will appear here."
        )

        st.markdown("### Impact")
        st.write("The impact of the pipeline failure will appear here.")

        st.markdown("### Recommendation")
        st.write("Recommendations will appear here.")
    else:
        st.info("Click Run Pipeline to start the pipeline.")

            
               
         
