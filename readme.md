||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Haruka_YANG (Practice Version)
Now: Only ChatGPT
More Translation Tool API - Update as soon
Date: January 19, 2024
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Steps:

1. Rebuild using Dockerfile: 
sudo docker build -t my-flask-app .

2. Run the program and send POST requests using Postman.

3. Use the POST method to:
Local: http://localhost:5000/translate
Example IP: http://192.168.10.117:5000/translate

4. For the request body (raw JSON), 
use an example like text_files/example_input.json.

5. Automatic backups, 
e.g., translated_files/2024-01-19 18:31:19.json.


Notes:

1. Check API limits in case of errors.
2. Processing long texts (~4000 characters) may be slow (response time: 2-3 minutes). Please be patient.
This translation provides an overview of the usage instructions for a translation tool API.