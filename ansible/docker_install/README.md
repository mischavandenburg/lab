# README 

Run with using the following command:
ansible-playbook -i inventory main.yml

The repo is divided by roles, using the structure acquired by the "ansible-galaxy init" command. 

Description of roles:

docker_installer:
Installs Docker on the Docker server and makes sure the service is enabled and started on boot.

make_partition:
Creates two partitions on a separately loaded EBS volume (set in AWS), and mounts these partitions to the /appl and /data directories on the root filesystem. 
Also ensures these partitions are added to fstab and are mounted on boot. 

Currently, this role is dependent on hardcoded device names. 
This needs to be adjusted with automatic device detection and partition name detection to make it more modular and usable in the future. 

www.mischavandenburg.com
