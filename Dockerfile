FROM python:3.11-slim

RUN pip install --upgrade pip setuptools
RUN pip install pipenv
RUN apt-get -q update && apt-get install -y --no-install-recommends gcc supervisor && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY streamlit-app.py .
COPY src ./src
COPY data ./data
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile

# Expose the port that Streamlit runs on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit-app.py", "--server.port=8501", "--server.address=0.0.0.0"]