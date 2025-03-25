FROM quay.io/astronomer/astro-runtime:12.7.1

USER root

RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-arm64/
RUN export JAVA_HOME

USER astro
