# Setup Ansible ansible env

## VENV
Isolate your Python development projects from your system installed 
Setup virtual environmen:  

```python3 -m venv path-to-catalog```  
```python3 -m venv C:\Kodilla\course_python\env```

Activate enviroment  
``` $ source ./env/bin/activate ```  
Also use  
```pip freeze```
```pip freeze > requirements.txt```

## Ad-hoc
```ansible all -i inventory.txt -m command -a "df -h"```

## Ansible logs
By default, the option is disabled. Can be enabled in the file  ```/etc/ansible/ansible.cfg``` uncommenting ```log_path = /var/log/ansible```

# Structure 

# Best pratice

Best pratice is in [Official Doc](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)
- Different inventory files for different people.
- On  ```No Log``` not to keep secrets in the log
- Group hosts based on location, server type, hardware etc etc
- Encryption of inventory or passwords themselves.
  

# Structure 

```
production                # inventory file for production servers
staging                   # inventory file for staging environment

group_vars/
   group1.yml             # here we assign variables to particular groups
   group2.yml
host_vars/
   hostname1.yml          # here we assign variables to particular systems
   hostname2.yml

library/                  # if any custom modules, put them here (optional)
module_utils/             # if any custom module_utils to support modules, put them here (optional)
filter_plugins/           # if any custom filter plugins, put them here (optional)

site.yml                  # master playbook
webservers.yml            # playbook for webserver tier
dbservers.yml             # playbook for dbserver tier

roles/
    common/               # this hierarchy represents a "role"
        tasks/            #
            main.yml      #  <-- tasks file can include smaller files if warranted
        handlers/         #
            main.yml      #  <-- handlers file
        templates/        #  <-- files for use with the template resource
            ntp.conf.j2   #  <------- templates end in .j2
        files/            #
            bar.txt       #  <-- files for use with the copy resource
            foo.sh        #  <-- script files for use with the script resource
        vars/             #
            main.yml      #  <-- variables associated with this role
        defaults/         #
            main.yml      #  <-- default lower priority variables for this role
        meta/             #
            main.yml      #  <-- role dependencies
        library/          # roles can also include custom modules
        module_utils/     # roles can also include custom module_utils
        lookup_plugins/   # or other types of plugins, like lookup in this case

    webtier/              # same kind of structure as "common" was above, done for the webtier role
    monitoring/           # ""
    fooapp/               # ""
```

## Inventory file

```ansible_host=192.0.2.50``` - this is host where we   
```ansible_connection=ssh``` or ```ansible_connection=winrm``` - this is type conncetion, for linux and windows       
```ansible_port=80```  
```ansible_user=user```   
```ansible_password=PASWORD``` or ```ansible_ssh_private_key_file=./key/file```   

## Inventory groups

```
Pattern	Result Target
all	All Hosts from your inventory file
host1	A single host (host1)
host1:host2	Both host1 and host2
group1	A single group (group1)
group1:group2	All servers in group1 and group2
group1:\&group2	Only servers that are both in group1 and group2
group1:\!group2	Servers in group1 except those also in group2
```
# Ansible logic

<<<<<<< HEAD
## Dictionary

## 

# Ansible acceleration
=======
### Jinja Template

We use like: 
```
vars:
    zmienna: zmiennawpliku
tasks:
    - name: Jinja Template
      template:
        src: plik.txt.j2
        dest: /usr/plik.txt
```

in j2 file we shoud have
```
This is random file with {{ zmiennawpliku }} for this instance
```


### Handlers
>>>>>>> 0c67835 (Update)

## TAGS
    

## Pipelining

Improves performance. Depends on server power. Increases Does not work with all distributions.

Remove # from ```/etc/ansible/ansible.cfg```  in the ```ANSIBLE_PIPELINING = FALSE ``` varialbe.

### Strategy
It allows you to perform tasks without waiting for responses from all machines.

Adding to the role ``strategy: free``

### Catching facts

Adding to the role ```gether_fact: no```

Before running the playbook, the machine does not collect facts. Saving time.

### ASYNC

Ansible działa w sposób synchroniczny domyślnie. W praktyce kazde zadanie blokuje poprzednie, doputy nie zostanie wykonane. 

Worning: Np wygaśnięcie sesii ssh. 

Musimy zdefiniowac dwie wartosci
async -  mówi ile ansible ma czekac na zadanie. Wyrazane jest w sekundach
pool - jak często ansible ma sprawdzic czy zadanie zostalo wykonane. Jesli damy ``0``  ansible uruchomi zadania i przejdzie dalej. 

### Mitogen 

This is a plugin that improves the performance of Ansible. This is not an official Ansible solution.