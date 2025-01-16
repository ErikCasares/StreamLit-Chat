import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    """Extrai texto de uma lista de PDFs."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def query_gpt(prompt, content):
    """Consulta o GPT com um prompt e o conteúdo extraído."""
    gpt = ChatOpenAI(temperature=0.7)  
    full_prompt = f"""
Você é um assistente que responde com base no seguinte conteúdo extraído de PDFs:

{content}

Pergunta: {prompt}

Responda com base no conteúdo fornecido acima.
"""
    response = gpt.predict(full_prompt)  
    return response

def handle_userinput(user_question, pdf_content):
    """Responde à pergunta do usuário com base nos PDFs processados."""
    if not pdf_content:
        st.warning("Por favor, carregue e processe os PDFs primeiro.")
        return

    gpt_response = query_gpt(user_question, pdf_content)

    st.write(user_template.replace("{{MSG}}", user_question), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", gpt_response), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.logo("./images/logo-white.png", icon_image="./images/ISAC.png")
    st.set_page_config(page_title="Chat com múltiplos PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    st.header(":grey[Escolha :books:]")

    if "pdf_content" not in st.session_state:
        st.session_state.pdf_content = None

    user_question = st.text_input(":grey[Faça uma pergunta sobre seus documentos:]")
    if user_question:
        handle_userinput(user_question, st.session_state.pdf_content)

    with st.sidebar:
        st.subheader(":primary[Carregue seus documentos]")
        pdf_docs = st.file_uploader(
            ":primary[Carregue seus PDFs para análise:]", accept_multiple_files=True)

        if st.button("Processar PDFs"):
            if pdf_docs and len(pdf_docs) >= 1:
                with st.spinner("Processando..."):
                    raw_text = get_pdf_text(pdf_docs)
                    st.session_state.pdf_content = raw_text 
                    st.success("PDFs processados! Você pode fazer perguntas agora.")
            else:
                st.warning("Por favor, carregue pelo menos um PDF.")

if __name__ == '__main__':
    main()
