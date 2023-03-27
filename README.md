# taylor-swift-eras
Taylor Swift  + Prefect + Langchain

## Setup 

### Services
- [Prefect Cloud Account and Workspace](app.prefect.com)
- [Google Custom Search Engine](https://developers.google.com/custom-search/docs/overview)

### Local Development Environment
pip install -r requirements.txt

prefect cloud login -> logging in to Prefect Cloud and selecting a workspace

Create a secrets block in Prefect Cloud with OpenAI API Key

### Prefect Blocks Required
- OpenAI API Key Secrets Block
- Google API Key Secrets Block
- Google Custom Search Engine ID Secrets Blocks
