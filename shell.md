# Shell snipets

## bash

show previous commands

    history | grep <CMD>

alias

    alias cbp="pbpaste|less"

quickly create file from clipboard

    pbpaste > /tmp/f

## files

Create new file with some contents

    echo "# Shell snipets" > shell.md

Open current folder with SublimeText / in Finder

    subl .
    open .

Create a file named introduction.js:

    touch introduction.js

Display file

    cat readme.txt

Link

    ln -s source destination

## web

GET with JSON:

    curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://hostname/
cf. http://stackoverflow.com/questions/14978411/http-post-and-get-using-curl-in-linux

Display response in terminal (including errors)

    curl -vs google.com 2>&1 | less
    echo hack the planet | curl -d@- http://localhost:8000
    curl -X PUT <URL>
    curl -H 'Content-Type: application/json' <url>

Pretty print html / json

    echo "<test><deep>value</deep></test>" | tidy -xml -q -i
    echo '{"json":"obj"}' | python -mjson.tool
    cat /tmp/f | pypp
    curl http://127.0.0.1:5984 | js-beautify -

*Resty*
https://github.com/pmleveque/resty
    
    resty http://127.0.0.1:5984
    GET / | js-beautify - | subl
    

*Jsawk*

    resty http://example.com:8080/data*.json
    GET /people/47 | jsawk 'this.favoriteColor = "blue"' | PUT /people/47

NB: two patterns:
1. Modify the this object in place (no return statement necessary).
2. Create a replacement object for each record, and *return* it at the end of each iteration.

    cat /tmp/t | jsawk 'return this.age'

with HTTPie: 

    http --verbose http://http-fun.hackership.org/ User-Agent:Terminal

## git

Add remote connections

    git remote add <REMOTENAME> <URL>

Set a URL to a remote

    git remote set-url <REMOTENAME> <URL>

Pull in changes

    git pull <REMOTENAME> <BRANCHNAME>

View remote connections

    git remote -v

Push changes

    git push <REMOTENAME> <BRANCH>

Remove a file from history

    git filter-branch --tree-filter 'rm -f settings.py' HEAD
    git push origin --force --all
cf. https://help.github.com/articles/remove-sensitive-data/

Create new branch

    git checkout -b <NAME>

## mac os x

cf. http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/

    open http://google.com
    open dash://man
    pbppaste                  # clipboard
    pbpaste | open -f -a Safari
    pbpaste | subl
    man -t [command] | open -f -a Preview

Command line start MySQL.

    sudo /usr/local/mysql/support-files/mysql.server start

Show All Files in Finder

    defaults write com.apple.finder AppleShowAllFiles TRUE

    killall Finder

Hide a file

    chflags hidden /path/to/file-or-folder

    chflags nohidden /path/to/file-or-folder

executable python script

    chmod +x /chemin/vers/ton/script

## installation scripts


    launchctl list |grep xxxNAMExxx

    open ~/.bash_profile

This will reload your .bash_profile with the newly added directory.

    source ~/.bash_profile


    sudo sublime /etc/apache2/httpd.conf

Reload apache to kick in

    sudo apachectl restart

