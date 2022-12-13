# jenkinsmulti
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


