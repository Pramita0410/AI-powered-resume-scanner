# AI-Powered Resume Scanner

## Project Overview
This project, a part of my Optional Practical Training (OPT), develops an innovative chatbot that streamlines the resume screening process for hiring managers. It diverges from conventional keyword-search tools by utilizing advanced Large Language Models (LLMs) to interpret and manage the complex language typically found in job descriptions and resumes. This tool is designed for efficiency, ease of use, and to match the effectiveness of a human in processing applications.

## Operational Framework
The chatbot incorporates a sophisticated retrieval system that identifies the most suitable candidates for a role:
- **Similarity-Based Retrieval**: Utilizes vector embeddings to compare the semantic similarity between job descriptions and resumes. This can involve technologies like FAISS (Facebook AI Similarity Search) for efficient nearest neighbor searches in high-dimensional spaces.
- **Contextual Retrieval**: Leveraging RAG (Retrieval-Augmented Generation), the chatbot finds resumes that are contextually similar to the given job description, thereby refining the pool of potential candidates.
- **Direct Retrieval**: This feature allows for pinpointed searches using specific candidate IDs, facilitating quick access to detailed profiles.

These resumes then provide context to the LLM, enhancing its ability to undertake detailed analyses, synthesize information, and aid in making informed hiring decisions.

## Importance of Enhanced Resume Screening
The growing number of job applications each year necessitates more advanced screening tools that surpass the limitations of traditional keyword-based systems, which often overlook the subtleties of natural language.

## Advantages of Using RAG
Employing RAG bolsters the chatbot’s ability to access and utilize a vast repository of data, ensuring responses are both relevant and accurate. This capability is essential in the recruitment industry, where job descriptions can vary widely and require nuanced interpretation.

## Additional Resources
Experience the chatbot’s capabilities firsthand through our [Streamlit Demo](https://ai-powered-resume-scanner.streamlit.app/).

## Setup and Execution
Below is a single bash script to clone the repo, set up the environment, install dependencies, and run the application. Ensure you have Conda installed on your machine before running this script.

```bash
# Clone the repository
git clone https://github.com/Pramita0410/AI-powered-resume-scanner

# Navigate into the repository
cd AI-powered-resume-scanner

# Create and activate a new Conda environment
conda create -n "genai" python=3.10 ipython -y
conda activate genai

# Install the required packages
pip install -r requirements.txt

# Run the application
streamlit run app.py
```


## Future Scope
1. **Data Engineering Tools**: Implement data engineering tools to automate the extraction and real-time processing of applicant data. This will facilitate the continuous updating of the model with new resumes and job descriptions.
2. **Data Visualization**: Integrate the automated pipeline with dashboarding tools for analyzing and displaying key metrics such as match percentage, skills overlap, and experience levels, helping recruiters quickly assess candidate suitability.

## Contributing
Interested in contributing? Great! Please fork the repository and submit a pull request with your proposed changes.
