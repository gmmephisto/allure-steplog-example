FROM centos:7

ARG ALLURE_VERSION=2.14.0

RUN yum install -y epel-release \
    && yum clean all \
    && rm -rf /var/cache/yum

RUN yum install -y \
        java-1.8.0-openjdk \
        which \
    && yum clean all \
    && rm -rf /var/cache/yum

ENV PATH=/opt/allure-$ALLURE_VERSION/bin:$PATH

RUN curl -sSL https://github.com/allure-framework/allure2/\
releases/download/$ALLURE_VERSION/allure-$ALLURE_VERSION.tgz | \
    tar -zxf - -C /opt

WORKDIR /app

ENTRYPOINT ["allure"]
