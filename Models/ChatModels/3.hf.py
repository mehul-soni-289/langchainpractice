def summarize_transcript(chunks):
    """
    Takes a list of transcript chunks and returns one final summarized text
    using a Hugging Face LLM through LangChain prompts.
    """

    from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
    from langchain.prompts import PromptTemplate
    from dotenv import load_dotenv

    # Load environment (optional if using HuggingFace API key or HF_TOKEN)
    load_dotenv()

    # Initialize model
    llm = HuggingFaceEndpoint(
        repo_id='meta-llama/Llama-3.1-8B-Instruct',
        task='text-generation'
    )
    model = ChatHuggingFace(llm=llm)

    # Prompt templates
    chunk_prompt = PromptTemplate(
        input_variables=["chunk"],
        template=(
            "You are an AI assistant. Summarize the following part of a transcript "
            "in 3-5 bullet points, keeping it clear and concise.\n\n"
            "Transcript part:\n{chunk}\n\nSummary:"
        )
    )

    final_prompt = PromptTemplate(
        input_variables=["summaries"],
        template=(
            "Combine the following short summaries into a single, coherent, and concise "
            "summary of around 150 words. Avoid repetition and maintain logical flow.\n\n"
            "Chunk summaries:\n{summaries}\n\nFinal summary:"
        )
    )

    # Summarize each chunk
    chunk_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)} ...")
        prompt_text = chunk_prompt.format(chunk=chunk)
        try:
            result = model.invoke(prompt_text)
            summary_text = result.content if hasattr(result, "content") else str(result)
            chunk_summaries.append(summary_text.strip())
        except Exception as e:
            print(f"⚠️ Error summarizing chunk {i+1}: {e}")
            chunk
