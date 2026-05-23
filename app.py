import streamlit as st
from src.pipeline.pipeline import research_pipeline

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("🔍 AI Multi-Agent Research System")

st.markdown("""
### Workflow
- 🔎 Search Agent
- 📄 Reader Agent
- ✍️ Writer Agent
- 🎯 Critic Agent
""")

st.divider()

# -----------------------------------
# User Input
# -----------------------------------

topic = st.text_input(
    "Enter a Research Topic",
    placeholder="Example: Future of Generative AI in Healthcare"
)

# -----------------------------------
# Start Research Button
# -----------------------------------

if st.button("Start Research", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Agents are researching..."):

            try:

                # Run Pipeline
                result = research_pipeline(topic)

                st.success("Research completed successfully!")

                # -----------------------------------
                # Search Results
                # -----------------------------------

                with st.expander("🔎 Search Results", expanded=True):
                    st.write(result["search_result"])

                # -----------------------------------
                # Reader Output
                # -----------------------------------

                with st.expander("📄 Reader Extracted Content", expanded=True):
                    st.write(result["reader_result"])

                # -----------------------------------
                # Final Report
                # -----------------------------------

                st.subheader("📝 Final Research Report")

                st.markdown(result["report"])

                # -----------------------------------
                # Critic Feedback
                # -----------------------------------

                st.subheader("🎯 Critic Feedback")

                st.markdown(result["feedback"])

                # -----------------------------------
                # Download Button
                # -----------------------------------

                st.download_button(
                    label="⬇ Download Report",
                    data=result["report"],
                    file_name="research_report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(f"Error: {str(e)}")    