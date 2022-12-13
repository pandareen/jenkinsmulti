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

- 
