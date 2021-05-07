# Cybertraining Web Page

The cybertraining web page can be created locally and one can review
changes prior to a commit.

First you will have to iinstall `go` and `hugo`

## Windows

See golang

* <https://golang.org/doc/install>

Install Cocolatey via powershell

* <https://chocolatey.org/install>

See hugo

* <https://gohugo.io/getting-started/installing/#chocolatey-windows>

Please also install gitbash and use gitbash instead of powershell

## OSX

See golang

See hugo


## Linux

See golang

See hugo


## Clone

If you have not yet cloned the repo you can do this with

```bash
git clone --recurse-submodules -j8 git@github.com:cybertraining-dsc/cybertraining-dsc.github.io.git
cd cybertraining-dsc.github.io
make setup
```

## Compile

The web page can be compiled and run with

```bash
make pull # pulls new info from the submodules
hugo serve
```

This allows you to modify the source with your favourite editor and
the changes will be automatically viewed.

The web page can be viewed with your browser at

* <http://localhost:1313/>

## Pull request

To change things, simply do a pull request. 

## Commit

Direct commits can be made by those who have write access others need to do a pull request.

Content is loacted in "./content./en"

Let us assume you like to change the content of the file
`content/en/courses/bigdata2020/_index.md`. Please use your favourite
editor, mine is emacs:

```
emacs content/en/courses/bigdata2020/_index.md 
```

Make your change and save is. Browse to the page that you changed and
observer the changes. To generate the changes for the web page we also
need to say

```
hugo
```


If you are satisfied, you can commit it with a
reasonable commit message. 

```
git commit -m "my super improvement" content/en/courses/bigdata2020/_index.md
```

However as hugo will create other changes, you can do 

```
git commit -a
```

which presents you in your editor that you use for git the ability to commit multiple 
files with the same comment that you fill out in the editor.

After the commit you want to push it with

```
git push
```

To keep up to date with other peoples changes you **MUST** often do a
git pull and if you see a conflict you need to resolve this. Thus it
is pest to communicate with the development team in aces you need to
do larger cahnges or have the risk that others work in pararlel.

## Add a submodule

Submodules for participants are located in the organizational repository. They shoudl be added to the reports directory to include the report for a participant.

```
cd content/en/report
git submodule add git@github.com:cybertraining-dsc/fa20-523-301.git 
```

replace the directoryname with the new module you like to add. After that, plase modify the Makefile to add it to the target `pull`.

..


