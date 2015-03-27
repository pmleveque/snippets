# Shell snipets

## files

Create new file with some contents
`echo "# Shell snipets" > shell.md`

Open current folder with SublimeText
`subl .`

Create a file named introduction.js:
`touch introduction.js`

Display file
`cat readme.txt`

Link
`ln -s source destination`


## web

Display response in terminal (including errors)
`curl -vs google.com 2>&1 | less`

`echo hack the planet | curl -d@- http://localhost:8000`


## git

Add remote connections
`git remote add <REMOTENAME> <URL>`

Set a URL to a remote
`git remote set-url <REMOTENAME> <URL>`

Pull in changes
`git pull <REMOTENAME> <BRANCHNAME>`

View remote connections
`git remote -v`

Push changes
`git push <REMOTENAME> <BRANCH>`


## mac os x

Command line start MySQL.
`sudo /usr/local/mysql/support-files/mysql.server start`

Show All Files in Finder
`defaults write com.apple.finder AppleShowAllFiles TRUE`
`killall Finder`

Hide a file
`chflags hidden /path/to/file-or-folder`
`chflags nohidden /path/to/file-or-folder`

executable python script
`chmod +x /chemin/vers/ton/script`

## installation scripts

`launchctl list |grep xxxNAMExxx`
`open ~/.bash_profile`

This will reload your .bash_profile with the newly added directory.
`source ~/.bash_profile`

`sudo sublime /etc/apache2/httpd.conf`

Reload apache to kick in
`sudo apachectl restart`

