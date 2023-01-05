# Dockerized LEMP stack deployed with Ansible

The role docker__installer installs Docker and enables it on startup.

The script then continues to build 4 containers:

- MySQL
- PHP
- PHPMyAdmin
- NGINX

The containers are added to the same network and are configured to be able to communicate with eachother. The application should be available at the IP addres of the VM or localhost.
It is mainly designed to use on a VM / EC2 instance.

The repo is using the "ansible-galaxy init" role structure. You will find the playbooks as follows: roles/your_choice/tasks/main.ymlo

Configuration:
- The script needs a SSH key to be set up beforehand which is set in the inventory file.
- The script needs a user on the dockerserver with the username "ds" with sudo rights and sudo password turned off.
- Add the ip address to your hosts file with the alias "ds"

Like so:
```bash
sudo vim /etc/hosts
123.13.13 ds
```

## LEMP stack?

You might think I mean a LAMP stack, which is deployed with Apache. Hence the A in LAMP. In a LEMP stack, we use NGINX as a webserver, which is pronounced “Engine X”, hence the E in LEMP stack. Therefore, LEMP is the correct way to spell it, and it is used in all the tutorials that I have been using.

## Blog post:

Here's the blog post written for this lab:

https://mischavandenburg.com/docker-lemp-stack-deployed-with-ansible/
