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

# Structure 

Best pratice is in [Master_repo](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)

[Tutaj wpisz notatki lub opis dotyczący tematu 1]

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

### Podtemat 2.1

[Tutaj wpisz notatki lub opis dotyczący podtematu 2.1]

### Podtemat 2.2

[Tutaj wpisz notatki lub opis dotyczący podtematu 2.2]

## Temat 3

[Tutaj wpisz notatki lub opis dotyczący tematu 3]oo