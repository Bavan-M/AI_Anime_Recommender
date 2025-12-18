# Base Image - Our prepared construction land
FROM python:3.10-slim

# House Rules - How Python should behave
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Designate the workshop room
WORKDIR /app

# Get basic construction tools from hardware store
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Bring in all building materials
COPY . .

# Install custom furniture (Python packages)
RUN pip install --no-cache-dir -e .

# Install a door at port 8501
EXPOSE 8501

# What happens when someone visits
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]