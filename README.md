# AWS Portal

It is a script through which a user will be able to login into its various aws instances. He would be able to see a list of instances in various regions and select where he wants to login by defining the private key path
Following is the process :

  - The initial thing the file does is to create a config file named aws_login at the user's home folder.
    - It asks for your aws access_key, secret_key, .pem file path and the regions of the instances you want to list.
    - It then calls for the list of instances (instance-tag-name, instance-id and ip_address) and inserts in the config file.
  - There are two flags that can be entered when calling the script.
    -  -c [CACHE], --cache [CACHE]   Pass "no" for calling new instances data. By default, it is yes.
    -  -k [KEY], --key [KEY]         Provide the ssh-key-path.
    -  -s [SEARCH], --search [SEARCH] Searches for the word in the name tag of the instances.
  - After the list of instances is shown on the terminal, you can just enter the corresponding index of the instance to login or press 0 to exit.

## How to install :
    -   curl "https://raw.githubusercontent.com/aasaanjobs/aws-portal/master/aws-portal" > aws-portal  (Getting data from github and making a file out of it)
    -   mkdir ~/bin (Create bin folder in user's home directory0
    -   mv aws-portal ~/bin (Copy the file in the bin directory of your home folder.)
    -   chmod +x ~/bin/aws-portal (Make it executable)
    -   export PATH=$PATH:~/bin (To make the custom terminal command)
    -   aws-portal (To run the file)

### Script Made by :
* [Gaurav Verma]
* [Shubham Bhartiya]

[Gaurav Verma]:https://www.linkedin.com/profile/view?id=20880813
[Shubham Bhartiya]:https://www.linkedin.com/profile/view?id=254924970
