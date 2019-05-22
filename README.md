# metrics-collection-script

How to use this script (for example in CentOS 7)

You must install the following applications:

	$yum install git
	$yum install docker

1 The next step is to download this repository to your Linux server:
	$git clone https://github.com/xzgooglik/metrics-collection-script.git

2 Go to current directory "metrics-collection-script":
	$cd metrics-collection-script/

3 Use "docker build" for create new image: 
	$docker build -t metrics-script . 
 "metrics-script" is name of your new image.

4 Run your container with next parameters: 
	$docker run -it metrics-script bash
  
  Write in console next command for prints basic information about your OS
	$./metrics.py cpu 
	or 
	$./metrics.py mem

5 Or run your container with next command:
	$docker run -it metrics-script ./metrics.py cpu
  or
	$docker run -it metrics-script ./metrics.py mem
