FROM amazonlinux:2023

RUN dnf install -y https://repo.mysql.com//mysql80-community-release-el9-1.noarch.rpm
RUN rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023
RUN dnf install -y mysql-community-devel
RUN dnf -y install python3-devel python-virtualenv gcc gcc-c++ make
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip3 install --upgrade pip
RUN dnf install -y npm

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

ADD . /code/
