FROM python:3.10.11


# Make work directory
RUN mkdir /app
WORKDIR /app

# Install required packaged for Django projects
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Clone source code
COPY . .

# Expose Django Server Port
EXPOSE 8000

# Start webserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]