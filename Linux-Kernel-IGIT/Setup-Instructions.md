####Note : These instructions assume you are running a variant of Ubuntu (like 12.04 LTS).


This will cover what all you need to get your first patch submitted. 
You have three choices for how to complete this:

1. Run Linux in VMPlayer from Windows.
2. Run Linux natively on your own machine.
3. Run Linux within VMPlayer on Linux.



##Setup your tools

####Install vim

```
sudo apt-get install vim
```


####Install git

```
sudo apt-get install git

sudo apt-get -y install git-core
```

OR

```
sudo add-apt-repository ppa:git-core/ppa

sudo apt-get update

sudo apt-get install git
```

Check git version using

```
git --version
```


####Gmail set up

In gmail, go click the gear icon, go to "Settings", go to the tab "Forwarding POP/IMAP",

and click the "Configuration instructions" link at the very bottom of the page.


Then click "I want to set up IMAP". At the bottom of the page, under the paragraph about

configuring your mail client, select "Other". Note the outgoing mail server information, and copy it

somewhere.



####SSL Tools

```
sudo apt-get install openssl ca-certificates
```


####msmtp

```
sudo apt-get install msmtp
```


####Fetchmail

```
sudo apt-get install fetchmail
```


####Procmail

```
sudo apt-get install procmail
```


####Install Mutt

```
sudo apt-get install mutt
```


####Install some packages

```
sudo apt-get install vim libncurses5-dev gcc make git exuberant-ctags
```


####Setup your Linux kernel code repository

```
mkdir -p git/kernels; cd git/kernels

git clone -b staging-next git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git

cd staging
```


####Install some more tools

Install all tools given [here](https://tapaswenipathak.wordpress.com/2014/10/11/tools-to-cleanup-linux-kernel/).

The instructions to install are also present in the blog post.



##Update your kernel

```
git fetch origin
```


Find more information [here](http://kernelnewbies.org/OutreachyfirstpatchSetup?action=show&redirect=OPWfirstpatchSetup) and [here](http://kernelnewbies.org/Outreachyfirstpatch?action=show&redirect=OPWfirstpatch).

More on git setup is [here](https://tapaswenipathak.wordpress.com/2014/08/26/git-setup/).


Some more useful links are [here](https://tapaswenipathak.wordpress.com/2014/10/03/submit-your-first-linux-kernel-patch/).
