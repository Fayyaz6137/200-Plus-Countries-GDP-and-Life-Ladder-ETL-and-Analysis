# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Create directory for SQLite DB (if not exists)
RUN mkdir -p /app/database

# Run ETL
CMD ["python", "main.py"]
