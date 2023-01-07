# Deploying a simple Linux VM to Azure with Terraform

For a project I'm setting up my environment with Terraform. 

I used [this tutorial](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-terraform), but modified the code to make it simpler and easier to understand for beginners. The original uses a random module to generate random names, and generates a new SSH key. Also, this tutorial uses expensive VM tiers and Premium storage, which is not necessary if you are learning.

I also thought the SSH configuration was overcomplicated. My version just takes an SSH keypair stored at `~/.ssh/id_rsa.pub`

To run:

```hcl
terraform init
terraform plan
terraform apply
```

The scripts prints the public IP of the newly created VM. You should be able to SSH to it:

`ssh azureuser@the_printed_ip_address`

You can find the code in [my "lab" repo on GitHub.](https://github.com/mischavandenburg/lab/tree/main/terraform/azure-simple-linux-vm)

https://mischavandenburg.com/zet/terraform-linux-vm/

https://github.com/mischavandenburg/lab/tree/main/terraform/azure-simple-linux-vm

https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-terraform

https://learn.microsoft.com/en-us/azure/developer/terraform/authenticate-to-azure?source=recommendations&tabs=bash#authenticate-to-azure-via-a-microsoft-account
