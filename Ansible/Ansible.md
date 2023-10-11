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

# Structure 

Best pratice is in [Master_repo](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)

[Tutaj wpisz notatki lub opis dotyczący tematu 1]

my-app/  
├─ playbook.yml  
├─ site.yml  
├─ requirements.txt  
├─ inventories/  
├─ roles/  
   ├─ name_role/
   ├─ name_role/  
   ├─ example_role/  
│  ├─ install_nginx/  
│  ├─ favicon.ico  
│  ├─ remove  
│  ├─ index.html  
├─ src/  
│  ├─ index.css  
│  ├─ index.js  
├─ .gitignore  
├─ ansible.cfg  
├─ README.md  
defaults/  
meta/  
tasks/  
handlers/  


## Temat 2

[Tutaj wpisz notatki lub opis dotyczący tematu 2]

### Podtemat 2.1

[Tutaj wpisz notatki lub opis dotyczący podtematu 2.1]

### Podtemat 2.2

[Tutaj wpisz notatki lub opis dotyczący podtematu 2.2]

## Temat 3

[Tutaj wpisz notatki lub opis dotyczący tematu 3]oo