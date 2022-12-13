# jenkinsmulti

jenkinsmulti
├── LICENSE # license file
├── master # master data folder
├── multi.yml # the main docker compose yml file (custom name)
├── remote
│   └── init.sh # initialisation script for the remote machine. consists ssh server configuration and ssh users configuration
└── slave
    ├── init.sh # initialisation script for the slave jenkins. includes the files needed for the program for running commands remotely
    └── ssh.py # python program that takes two inputs to run the bash commands remotely. This will be called by the jenkins job

3 directories, 5 files

Steps:

- Create 2 directories in home: `~/jenkins/` & `~/jnlp_slave`
```
mkdir  ~/jenkins/  ~/jnlp_slave
```

- Navigate to the `jenkinsmulti` repository folder

```
cd ~/testscripts/jenkinsmulti
```

- Make sure the Docker desktop is installed and running (https://www.docker.com/products/docker-desktop/)

- Once inside the `jenkinsmulti` folder, run the following command

```
docker-compose -f multi.yml up -d
```
This above will be a success once you see this output

```
(base) ➜  jenkinsmulti git:(main) docker-compose -f multi.yml up -d
Creating network "jenkinsmulti_vpcbr" with driver "bridge"
Creating remote_computer ... done
Creating jnlp_slave      ... done
Creating jenkins         ... done
```
This is how the docker desktop should look like
<img width="899" alt="Screenshot 2022-12-13 at 10 18 11 PM" src="https://user-images.githubusercontent.com/7270563/207393983-6654e90c-d769-44a8-a263-80ee874f1910.png">

- Go to the container named "jenkins" and copy the master password to log into jenkins server
for ex: `c51c81860b424059badf009a1d06ec33`
<img width="896" alt="Screenshot 2022-12-13 at 10 19 32 PM" src="https://user-images.githubusercontent.com/7270563/207394297-deb18829-5bc4-449f-8144-af1f9277d2e5.png">


- After copying the master password go to the url http://localhost:8080/ in your browser
Enter the password on the input `Administrator password` and click `Continue`

- You'll be shown the setup wizard, and press "Install suggested plugins" and let the installation continue
<img width="991" alt="Screenshot 2022-12-13 at 10 22 33 PM" src="https://user-images.githubusercontent.com/7270563/207394935-bc6b814d-36c7-4af1-896a-5d6b73b1ed1a.png">

- Once the above process completes, you'll be asked to add new admin users, use 'jenkins' as username and 'jenkins' as password and all the fields as shown in the screenshot. After that press "Save and Continue"

<img width="993" alt="Screenshot 2022-12-13 at 10 33 27 PM" src="https://user-images.githubusercontent.com/7270563/207397397-13e57f44-b948-4dee-a677-4542176f3651.png">

- Next is the jenkins url,
set it to `http://10.5.0.5:8080/` and "Save and Finish"
<img width="984" alt="Screenshot 2022-12-13 at 10 35 27 PM" src="https://user-images.githubusercontent.com/7270563/207397781-fca5a93a-0ea9-4284-89e2-527317adfeeb.png">

- Jenkins is ready, click on next

- Create a new jenkins slave node. Click on Manage Jenkins -> Setup Agent
Set node name as `slave_1` and enable "Permanent Agent" press "Create"
<img width="1328" alt="Screenshot 2022-12-13 at 10 37 22 PM" src="https://user-images.githubusercontent.com/7270563/207398154-2241e694-586f-4d70-ba9d-233d1f2a8df3.png">

- In the next step, its gonna ask more details for the node, set them as follows and hit "Save"
<img width="1785" alt="Screenshot 2022-12-13 at 10 39 25 PM" src="https://user-images.githubusercontent.com/7270563/207398522-f23b8e0f-ece4-4694-9ba1-bf8d72d2c2df.png">
<img width="1764" alt="Screenshot 2022-12-13 at 10 39 47 PM" src="https://user-images.githubusercontent.com/7270563/207398602-7164079d-e154-4a69-bad5-29de317e6c3e.png">


- Slave Node is now created, go to http://localhost:8080/manage/computer/slave_1/ and copy the secret for ex `460330d08e62e6f45849670dca55b31bf2485b30b1601671bfca107bf63f22b7`
<img width="1731" alt="Screenshot 2022-12-13 at 10 41 44 PM" src="https://user-images.githubusercontent.com/7270563/207398998-f123ff11-b9e4-4b69-ac60-9ba29420a395.png">


- Replace the secret in line no. 29 for example `dad74fba44f1e53823a9dcf52ba920f9cfcdcc7ff6a9e174d60e47996bb14a6c` with `460330d08e62e6f45849670dca55b31bf2485b30b1601671bfca107bf63f22b7`

- After this go to terminal and the `jenkinsmulti` folder. Execute the following command
```
docker-compose -f multi.yml down
```
This will show this output 
```
(base) ➜  jenkinsmulti git:(main) docker-compose -f multi.yml down
Stopping jenkins         ... done
Stopping remote_computer ... done
Stopping jnlp_slave      ... done
Removing jenkins         ... done
Removing remote_computer ... done
Removing jnlp_slave      ... done
Removing network jenkinsmulti_vpcbr
```

- Again start the docker compose with
```
docker-compose -f multi.yml up -d
```
Go to http://localhost:8080/manage/computer/ and check if the slave_1 is online 
<img width="1430" alt="Screenshot 2022-12-13 at 10 46 43 PM" src="https://user-images.githubusercontent.com/7270563/207400076-d490530c-c0d7-4262-b06a-06f50ad378a0.png">

- Now this completes the jenkins master and slave configuration in the same docker as two separate containers

- Now we will create a new job that will execute a python script which lists files in remote server
Create a new job and name it as test
Jenkins Dashboard -> New Item -> Set name as "test" -> Select "Freestyle Project" -> Click ok
Now configure this new job "test"
This job has to run on a specific agent "slave_1". This job is parametrized and will have two string parameters 'ip_addr' and 'root_dir'. It should have a build steps as execute a shell command. The contents of this should be 
```
apt update
apt install pip -y
pip install paramiko
python3 /tmp/slave/ssh.py --ip_addr=${ip_addr} --root_dir=${root_dir}
```
Follow the screenshots and the job config should look like this, leave rest as is
<img width="1774" alt="Screenshot 2022-12-13 at 10 52 35 PM" src="https://user-images.githubusercontent.com/7270563/207402307-1ba7ba72-a14b-4aed-be0f-be28c99fb2db.png">

<img width="1780" alt="Screenshot 2022-12-13 at 10 52 48 PM" src="https://user-images.githubusercontent.com/7270563/207402335-79fdbd6a-1bff-4f12-a64b-2e2f382355c3.png">

<img width="1785" alt="Screenshot 2022-12-13 at 10 53 07 PM" src="https://user-images.githubusercontent.com/7270563/207402356-234288ac-fc87-45a1-a5f8-0f8448abeea1.png">

Hit save

- Now build the jenkins job with the following default parameters
<img width="1791" alt="Screenshot 2022-12-13 at 10 53 18 PM" src="https://user-images.githubusercontent.com/7270563/207402484-7455acca-3da2-426e-ac71-10b400d56df4.png">


- The output should look like this and the job should succeed

<img width="1778" alt="Screenshot 2022-12-13 at 10 55 00 PM" src="https://user-images.githubusercontent.com/7270563/207402522-de25dcaf-3bb4-4756-b534-2f88de283431.png">

