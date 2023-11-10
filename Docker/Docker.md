# Commands 

```docker ps```

Instalacja 

# Checking Dockerfiles
hadolint - tool to flag errors, bugs, stylistic errors, best practice   
    ```hadolint Dockerfile```  
    ```hadolint ignore=DL3018```  
# Testing Images
Container Structure Tests 
    1. CECKING FILES IN/EXISTANCE/PERMISIONS etc.
    2. Check files content presence or absence
    3. check metadata (env vars, user, entrypoint)
    4. run commands inside the container 
Unit tests 
    1. Integration test posible
   Output formats: Json, text or junit 


#Analyzing images
dive - tool to analize docker leyers container
#Building images

# Data folder data volume

# Clear space

```du -sh /var/lib/docker```   
```docker system prune --all --force --volumes ```