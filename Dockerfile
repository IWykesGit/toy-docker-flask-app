
# Start from slim Python base (fast, secure)
FROM python:3.11-slim 

# Set working directory in container
WORKDIR /app

#Copy everything over
COPY . .

# Install dependencies (no caching to keep image small)
RUN pip install --no-cache-dir -r requirements.txt

#Tell Docker about the port
EXPOSE 5000

# Command to run the app when container starts
CMD ["python", "app.py"]