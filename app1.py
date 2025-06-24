import os
import streamlit as st
api_key = st.secrets["GROQ_API_KEY"]
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompts=ChatPromptTemplate.from_messages([("system","you are a helpful assistant which helps in translating one language to other"),("user","tranlate {frominput} to {tooutput}")
                                          
])
llm=ChatGroq(model="llama3-70b-8192",api_key=api_key)
outputparser=StrOutputParser()
chain=prompts|llm|outputparser

st.title("TRANSLATION USING GROQ AI")
input=st.text_area("Enter Text")
output=st.selectbox("Translate To:",["english","French", "Spanish", "Tamil", "Hindi", "German"])
if st.button("Translate"):
    if input:
        try:
            res=chain.invoke({
                "frominput":input,
                "tooutput":output
            })
            st.subheader("translation:")
            st.write(res)
        except Exception as e:
            st.error(f"error:{e}")
    else:
        st.warning("enter text to translate")