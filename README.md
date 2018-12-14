# ae_test_task-fb_posts
#### COMMON DEPENDENCIES:
* python 3.6.5

#### FOR SETUP PYTHON DEPENDENCIES:
For unix OS:
* Create and activate virtualenv
> pip3 install virtualenv
* Verify installation is successful
> virtualenv --version
* Create a virtual environment for a project (execute command from the project directory)
* Go to the project directory
> virtualenv venv
* For activation virtualenv (execute command from the project directory)
> source venv/bin/activate
* Setup python dependencies (execute command from the project directory)
> pip3 install -r requirements.txt

### PAY ATTENTION!!!
* You should update all requirement variables (see "{project_path}/config.py")


##### FAQ (How to run the tests)
* For run all tests
> pytest