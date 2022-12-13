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
