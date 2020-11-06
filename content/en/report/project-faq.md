# Project FAQ

{{% pageinfo %}}

{{< table_of_contents >}}

{{% /pageinfo %}}

## Do I have to read every Piazza post?

Yes.

There are very view posts in Piazza, typically much less than 10 per
week. If you were taking a live class I am sure you get also 10+ tips
and comments form the instructors. Piazza is a mechanism fo use to
communicate to the entire class as this class is an online class.

Use piazza to discuss things. You can also use it to discuss issues in
your projects with other class mates openly.

## I see something mssing or wrong in this FAQ. How can I correct or add it?

If you see something missing that we shoudl add, please edit this web
page and create a pull request with your changes:

[Edit here](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/edit/master/content/en/report/checklist.md)

## Where to get help?

We often use the term TA instead of AI as AI in this class has a
specific meaning related to class content. 

TA hours are posted at

* <https://piazza.com/class/kedccsbsthm5sc?cid=179>

If a TA is not available during that time, you have the right to ask
for an alternative time.

## Do I have to work weekly on the project?

Yes.

Please plan to set aside a **significant** time every week for your
project. We include your weekly progress in the grade. This is because
you will fail if you do not set sufficient time aside and start your
project in the week before the deadline.


## When are updates due?

Updates are due every week from the time that the project has been
announced. The updates will be committed by you to github.com. TAs
will be reviewing your updates The weekly progress will be check by
the TA's while looking at the GitHub insights page.

TAs or instructors may make comments to your repository. It is your
responsibility to make sure to stay in sync with the content in the
repo. Best is to use a tool such as a command line tool or a GUI tool
to stay in sync with the repo.

## How do I define a project?

Please take a look at the class content and select a topic that
interests you. Your project needs to be related to *big data* and
provide an analysis of the data. You may choose a topic that is only
explained later on in class. In this case, you can explore the topic
ahead of time before it is explained in class. Previous class material
is posted for all topics. If you have a question, work with the TA's
and nstructors.

Please remember this is not just an AI class to demonstrate a specific
AI method. Your project must have a section or an explanation of how your
project relates or could relate to big data.

However, it is **not** required to use a huge dataset for this class. 

The class has also the ability to do projects related to cloud
infrastructure. In that case, please contact Gregor directly to assess
if you have enough qualifications and can succeed in the project. 

## Project Directory

The following is the best structure for your project

* `project/project.md` # your project report
* `project/project.bib` # your project bib file if you use jabref
* `project/plan.md` # for final submission move your Plan section here
* `project/images` # place all images in this directory
* `project/code/`

   Move your python code or notebooks here.

* `project/data`

  Your project must not have (large) data in GitHub, instead you must
  have a program that downloads the data.  best is to add project/data
  to your .gitignore file See more information on the data section.

Make sure you create in your paper citations and references to your own
code and GitHub directory.

## Filenames

Filenames must be precise, and we recommend using lower case file names
in most cases (some Python class files may also contain capital
letters). Filenames must not have spaces included in them. We will not
review any information included in a file that contains spaces or
characters that are not in [a-Z0-9] and the _ and - characters. We will
return your project without review and assign an "F" as those files
cause issues.

All image file names must be lower case.

Her an example of an image file name that is wrong in many ways:
 project/images/THIS IS Gregor's Image.PNG contains spaces contains
 capital letres contains ' which is not allowed ever has an ending
 with capital letters see also:
 <https://piazza.com/class/kedccsbsthm5sc?cid=240>

## Project Proposal

This is a snapshot of your final project. You do not have to use the
words *I* or *plan* simply write it as if you already decided to do
the project and make it look like a final paper's snapshot. Your
paper must follow a typical research paper outline. The project
ideally provides a novel feature that has not been presented by
others. Just replication what others in the community did may not be
lead to the best result. If you have not researched if others have
done your project, It also will not lead to your best result.

A sample of a report is provided at

* Raw:
<https://raw.githubusercontent.com/cybertraining-dsc/fa20-523-312/master/project/project.md>
* <https://cybertraining-dsc.github.io/report/fa20-523-312/project/project/>

Sections that must be included

* Abstract
* Introduction
* Related Research
  Identify similar projects and describe what you do differently
* Data
  Write about which data you choose
* Analysis
  Write about your intended analysis 
* Plan 
  Provide a plan that lists what you do every week.(This plan is to be removed before the final submission at the end of the semester. You can move it into a file called project/plan.md
  in case you like to preserve it

## Reports without programming

It is possible for undergraduates, but not for graduate students to do
a report that does not include programming. You will automatically get
a half grade point deduction, and the best grade achievable will be an
A-. The report will typically be 25% to 50% longer than a project
with programming. It must be comprehensive and have a more in-depth background
section. Proper citations are a must. Citations are
typically much more in reports due to the nature of it.

In case you chose a report, your directory structure will look like this

* report/report.md # your project report
* report/report.bib # your project bib file
* report/plan.md # for final submission move your Plan section here
* report/images # place all images in thsi directory

It is our **strong** recommendation that you use jabref for assisting you
with the management of your references! You will save a lot of time
while using it and assure that the format will be correct, which is
important for reports!

## Formal writing

They shall not use the word "I" in the report.

see also: <https://piazza.com/class/kedccsbsthm5sc?cid=181>

We do allow, however, the words *we*, *you*

In general:

* Do not use first-person pronouns ("I", "me", "my", "us", etc.). ...
* You must not use contractions such as don't or 've ...
* Avoid colloquialism and slang expressions. ...
* Avoid nonstandard diction. ...
* When using an abbreviation, it must be defined before its first use
  in brackets): Artificial Intelligence (AI) ... Avoid the creation of unnecessary abbreviations. It is better to say big data instead of BD
* Avoid the overuse of short and simple sentences.
* Avoid the overuse of very long and complex sentences.

### colons 

A colon is :

* They shall not use a space before a colon ever.
* They shall not use colons in section headers.

### Quotes

* They shall not use "quoted quotes" to highlight.
* They shall use *italic* to highlight

Quotes are reserved for citations and must be followed by a citation
that is included in your reference section.

## Update and check the submission

Once you submit your paper, you need to dow the following.

1. modify the README.yaml file and update the information of your project in it. Keep it up to date in case authors or title changes. We use this information to mine all Gitrepos, and thus it must be up to date all the time.
   In case you are in a group, make sure you preserve the authors' order in the list among all group members. The person that has the repo for the project must be the first author.

	Example for single author: <https://github.com/cybertraining-dsc/fa20-523-312/README.yaml>

2. Check every week if your report renders correctly and if your
   report is listed at <https://cybertraining-dsc.github.io/report/>
   Click on your paper link, your student link, and your edit link to ensure they all work correctly. If not, please correct them via a
   pull request (you can edit that page and see how we do it for other students).

## Using Markdown

We no longer accept any document format that is not markdown. We use
proper markdown that must not include any HTML tags. submissions with
HTML tags will be rejected without reviews. You must look at our
template in raw format to see what features of markdown we use. Your
file may not be properly rendered in GitHub (e.g., abstract and table
of content, as well as references look differently), but it will be on our Web
site. 

## References and citations

You must have a reference section from the get-go. We use 
footnotes to showcase the references as GitHub does not support proper
references in markdown. However, we use footnotes in a straightforward and
specific way that requires you to be careful with the dot at the end of
the sentence. The footnotes must not be after the dot, but they must
be within the dot. The reason is that at one point, we will
automatically replace your footnotes with a [number] theme. You do not
have to do this; we will do this. This is simpler than it sounds for
you, so we give an example:

When you use the citations, you MUST for us do them before the dot that
closes the sentence that you cite in or refers to. They do require you
do the `[^1]` before the dot

wrong: `This is a sentence with reference.[^1]`

correct: `This is a sentence with reference [^1]`.

wrong: `Simon says "Hallo".[^1]`

The reference section must be the last section in your report

```
## 8. Refernces

[^1]:  This is where you put the citation information. 
```

See, there is no space before the :

see also https://piazza.com/class/kedccsbsthm5sc?cid=45

### Format of References

Although we use footnotes in markdown, we will use the propper IEEE
format style for citations. Please google it. The easiest way for you
to get IEEE references is to use jabref and manage your references there
and just copy the rendered content from jabrefs display window into
your markdown reference section. Make sure to remove all HTML tags.
If you use jabref, please submit your references as project.bib file 

### URLs in the text

In case you use URLs in the text, they must be followed by a citation
with it being referenced in the reference section by a label.

### References that are not cited in the text

You must not have any references that you have not cited in the text

### Images that you copied

In case you copied an image from the internet, it must have a citation
in the caption and be referenced in the reference section.

If you use figures, check carefully with our template, do not invent
your own method. We will reject your paper without review if you do it
wrong.

### How to include images

We have provided a clear example. Do not invent your own method or use
relative links. Images must be cited with a link to the raw image in
GitHub. See our example!

## Programs

### Python 

You are allowed to use python notebooks or python programs. All of
which must be checked into GitHub in your assigned repo. Sometimes notebooks have a cache
that is too big for GitHub, this you need to make sure to always clear
the cache before you check it into GitHub.

### Otherprogramming langauges

Use python.

### Data

Please add a "download" data function that downloads the data from the
source. Do not store the actual data in Github.
The download function must have a logic that does not download the
data when it is already downloaded. Python makes this easy with
`os.path` and `python requests`. We recommend you use python requests
and not `urllib`. You can share the download function openly with each
other. 

In case of questions discuss on piazza.

See also:

* <https://piazza.com/class/kedccsbsthm5sc?cid=227>
* <https://piazza.com/class/kedccsbsthm5sc?cid=142>


### Images from Programs

You can create png files of graphics so you can include them in your
project.md. Make sure you add a save image function and do not just
create screenshots. Matplotlib and other graphics frameworks have an
API call for this.

There are many good and even specialized graphics libraries that you
can use, examples are

* matplotlib
* bokeh
* seaborn
* ...

See also: <https://piazza.com/class/kedccsbsthm5sc?cid=226>


### Bechmark

Your program must use cloudmesh benchmark. It includes a convenient
StopWatch and benchmark print function. 

see: <https://piazza.com/class/kedccsbsthm5sc?cid=103>


## Template Links

Here are the relevant URLs to them, which you naturally can find from
our report web page. But as some of you have not visited the web page
at

* <https://cybertraining-dsc.github.io/report/>

* <https://cybertraining-dsc.github.io/report/fa20-523-312/project/project/>
* <https://raw.githubusercontent.com/cybertraining-dsc/fa20-523-312/master/project/project.md>

See that githib does not quite render it properly, but it will by ok
for a superficial view and editing.

* <https://github.com/cybertraining-dsc/fa20-523-312/blob/master/project/project.md>

Make sure to check your report at

* <https://cybertraining-dsc.github.io/report/>

which will be updated weekly




