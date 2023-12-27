

import os
# use your own OPENAPI Key
#os.environ["OPENAI_API_KEY"] = "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"

import gradio as gr
from langchain import OpenAI, PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from utils.llm_wrapper import get_llm
from anthropic_bedrock import AnthropicBedrock

llm = get_llm()


def count_tokens(text):
    client = AnthropicBedrock()
    token_count = client.count_tokens(text)
    
    return token_count

def estimate_tokens(text):
    # Count the number of 4-letter chunks in the text
    chunk_size = 4
    token_count = len(text) // chunk_size
    
    return token_count

def summarize_pdf(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    #page_content = docs[0].page_content
    input_token_count = 0
    estimated_input_token_count = 0

    for doc in docs:
        page_content = doc.page_content
        page_token_count = count_tokens(page_content)
        input_token_count += page_token_count
        estimate_token_count = estimate_tokens(page_content)
        estimated_input_token_count += estimate_token_count
    #print(page_content)
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)   
    # Calculate the token count for the generated summary
    #input_token_count = count_tokens(page_content)
    output_token_count = count_tokens(summary)
    #estimated_input_token_count = estimate_tokens(page_content)
    estimated_output_token_count = estimate_tokens(summary)

    return summary, input_token_count,output_token_count, estimated_input_token_count, estimated_output_token_count


input_pdf_path = gr.components.Textbox(label="Provide the PDF file path")
output_summary = gr.components.Textbox(label="Summary")
output_in_token_count = gr.components.Textbox(label="Token Count Input")
output_out_token_count = gr.components.Textbox(label="Token Count Output")
output_estimated_input = gr.components.Textbox(label="Estimated Input")
output_estimated_output = gr.components.Textbox(label="Estimated Output")

interface = gr.Interface(
    fn=summarize_pdf,
    inputs=input_pdf_path,
    outputs=[output_summary, output_in_token_count,output_out_token_count, output_estimated_input,output_estimated_output],
    title="PDF Summarizer",
    description="Provide PDF file path to get the summary.",
).launch(share=False)