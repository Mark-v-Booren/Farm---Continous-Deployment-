# Continous Deployment Pipeline

Back-End assignment:  

Creating and provisioning a server at Digital Ocean;
Connecting to a Linux server over SSH;
Running basic terminal commands on a Linux server;
Deploying a Flask application on a Linux server.
Use of Flask.
Use of Pytest.
Use of SSH key and Github secrets

The continous deployment pipeline looks on the web like:

http://161.35.19.72

http://161.35.19.72/cow

http://161.35.19.72/mice


GitHub Actions runs tests on the code with Pytest.
If and only if the tests pass, GitHub Actions logs into the VPS running with Digital Ocean and runs commands such that the code is updated to the latest version.

You can think of an SSH key as a username and password in one. You can use it to make reading and writing to repositories under your account on GitHub easier. A deploy key is an SSH key that grants access to just one repository. You can even set the key to only allow read-only access for extra security.

In order to execute commands on the VPS that your application is running on you need to have access to it within a workflow on GitHub Actions. On the other hand we don't never want to put log-in credentials in the repository itself. The way to do this is by using encrypted secrets.

Hereby I created the continuous deployment pipeline as described above. The complexity of this  Flask application is not important here, only that you use a GitHub Actions workflow to test and -- if it passed -- update the code running on your server after a push.

Thanks for reading! Stay safe & funny








 
 


