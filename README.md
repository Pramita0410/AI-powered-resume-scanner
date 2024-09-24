# AI-Powered Resume Scanner

## Project Overview
This project develops an innovative chatbot that streamlines the resume screening process for hiring managers. It diverges from conventional keyword-search tools by utilizing advanced Large Language Models (LLMs) to interpret and manage the complex language typically found in job descriptions and resumes. This tool is designed for efficiency, ease of use, and to match the effectiveness of a human in processing applications.

## Operational Framework
The chatbot incorporates a sophisticated retrieval system that identifies the most suitable candidates for a role:
- **Similarity-Based Retrieval**: Utilizes vector embeddings to compare the semantic similarity between job descriptions and resumes. This can involve technologies like FAISS (Facebook AI Similarity Search) for efficient nearest neighbor searches in high-dimensional spaces.
- **Contextual Retrieval**: Leveraging RAG (Retrieval-Augmented Generation), the chatbot finds resumes that are contextually similar to the given job description, thereby refining the pool of potential candidates.
- **Direct Retrieval**: This feature allows for pinpointed searches using specific candidate IDs, facilitating quick access to detailed profiles.

These resumes then provide context to the LLM, enhancing its ability to undertake detailed analyses, synthesize information, and aid in making informed hiring decisions.

## Importance of Enhanced Resume Screening
The growing number of job applications each year necessitates more advanced screening tools that surpass the limitations of traditional keyword-based systems, which often overlook the subtleties of natural language.

## Advantages of Using RAG/RAG Fusion
Employing RAG bolsters the chatbot’s ability to access and utilize a vast repository of data, ensuring responses are both relevant and accurate. This capability is essential in the recruitment industry, where job descriptions can vary widely and require nuanced interpretation.

## Additional Resources
Experience the chatbot’s capabilities firsthand through our [Streamlit Demo](https://ai-powered-resume-scanner.streamlit.app/).

## How to Run

### Clone the Repository
```bash
git clone https://github.com/Pramita0410/AI-powered-resume-scanner

