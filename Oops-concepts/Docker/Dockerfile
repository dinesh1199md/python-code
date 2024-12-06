
#base image 
FROM python:3.9-slim as build
WORKDIR /app
COPY requirements.tx .
Copy . .
RUN  pip  install --upgrade pip &pip install -r requirements.tx
#final stage
FROM python-slim:3.9 
WORKDIR /app
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /app /app
EXPOSE 800
CMD ["python3","/app/main.py"]


---
# Stage 1: Build stage
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Final stage
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the installed dependencies from the build stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the application code from the build stage
COPY --from=builder /app /app

# Command to run the application
CMD ["python", "app.py"]



'''Why Multi-Stage Builds?
Efficiency: Multi-stage builds allow you to separate the build environment from the runtime environment. This results in a smaller, 
more secure final image because it only contains the necessary files to run the application, not the build tools or temporary files.
Reduced Image Size: By copying only the necessary artifacts (e.g., Python packages and application code) from the build stage, 
you avoid including unnecessary files that would bloat the final image.
This approach ensures that your Docker image is both lightweight and secure, which is especially important for deploying applications in production environments.'''
  

FROM python:3.9-slim as builder
WORKDIR /app
COPY  requirements.tx  .
run pip i upgrade pip &  pipe3 i -r requirements.txt
FROM python:3.9-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app
EXPOSE 3000
CMD ["python3", '/app/app.py']




