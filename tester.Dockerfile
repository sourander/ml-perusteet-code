FROM ghcr.io/astral-sh/uv:python3.13-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy test dependencies
COPY pyproject.toml pytest.ini README.md ./
