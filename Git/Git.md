# Setup

## Local and global user config 

Set your username: ```git config --global user.name "FIRST_NAME LAST_NAME"```  
Set your email address: ```git config --global user.email "MY_NAME@example.com"```

## Branch manipulate

Add branch: ``` git checkout -b ＜new-branch＞```  
Delete branch: ``` git checkout -d ＜new-branch＞ ```

## Remote branch manipulate

Show remote branch: ``` git branch -r ```   
Download branches: ``` git fetch ```  
Remote repository name, which by default is origin: ``` git fetch origin ```  
Download pull all: ``` git pull --all ```

## Git tag

Show tags: ``` git tag  ```  
List tags: ``` git tag -l ```  
Show details: ``` git show v1.4 ```  
Add new tags: ``` git tag -a v1.4 -m "my version 1.4" ```  
Push specyfic tag: ``` git push origin v1.5 ```  
Push all tags: ``` git push origin --tags ```  


# More git 
[.git more](https://blog.meain.io/2023/what-is-in-dot-git/?utm_source=unknownews)
[git rebase](https://www.freecodecamp.org/news/git-rebase-handbook/?utm_source=unknownews)