FROM python:3.11-slim

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Update and install dependencies
RUN apt-get update && apt-get install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
COPY pyproject.toml  ./
RUN uv sync

COPY . .

EXPOSE 8501

# Run app
CMD ["uv", "run", "streamlit", "run", "notion_finance.py", "--server.port=8501", "--server.address=0.0.0.0"]

