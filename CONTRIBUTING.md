# How to Contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution;
this simply gives us permission to use and redistribute your contributions as
part of the project. All contributions are assumed to be under APache 2.0 License.

## Clone the Repository

You must have go, hugo and docsy installed. This is described on the appropriate web sites

To clone the repo use:

```bash
git clone --recursive git@github.com:cybertraining-dsc/cybertraining-dsc.github.io.git
cd cybertraining-dsc.github.io
```

## Modification of the Content

The content is organized in directories such as. We can add new directories.
The index will be automatically updated from it.

```
content/
├── about
│   └── _index.html
├── blog
│   ├── _index.md
│   ├── news
│   │   ├── news-1,md
│   │   └── news-2.md
│   └── releases
│       ├── release-1.md
│       └── _index.md
├── community
│   └── _index.md
├── docs
│   ├── topic-1
│   │   └── _index.md
│   ├── topic-2
│   │   └── _index.md
├── _index.html
└── search.md
```

We can add and 


## Create The Web Site Locally


To view the site locally say

```bash
hugo server
```

To create the pages that need to be submitted to git use

```bash
hugo
```

THen you need to commit them.

However we are in the process to automate this with Netifly so a commit into the content dir is all you need

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## Community Guidelines

This project follows
[Google's Open Source Community Guidelines](https://opensource.google.com/conduct/).
