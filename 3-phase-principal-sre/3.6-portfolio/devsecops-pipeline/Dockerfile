# Use a specific digest-pinned base image for reproducibility
# In production, pin to digest: FROM python:3.12-slim@sha256:<digest>
FROM python:3.12-slim

# Run as non-root — OPA policy will enforce this requirement
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy requirements first for layer caching efficiency
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Switch to non-root user before CMD
USER appuser

EXPOSE 8080

# Use exec form to avoid shell wrapper (PID 1 goes to app, not /bin/sh)
CMD ["python", "app.py"]
