# Grab the base image from Docker Hub
FROM node:latest

# Set up development environment...
WORKDIR /app/public

# Update package database
RUN apt-get update -y

# Install some useful tools
RUN apt install htop -y

# Install Flask on Python...
RUN apt install python3-pip -y
RUN pip install Flask


# Install Node Package Manager (NPM)...
RUN curl -qL https://www.npmjs.com/install.sh | sh

# Install react-bootstrap module...
RUN npm install --save react-bootstrap bootstrap@3

# Install your personal copy of docker
#   Start with basic dependencies for Docker.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables
    
#   Next we will install Docker from toe official Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

#   Install the docker wrapper.
#   Do a hand stand
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
#   Mount storage for the container
VOLUME /var/lib/docker

# Install Code server
RUN echo "**** install runtime dependencies ****" && \
  apt-get install -y \
    git \
    jq \
    libatomic1 \
    nano \
    s6 \
    net-tools \
    sudo && \
  echo "**** install code-server ****" && \
  if [ -z ${CODE_RELEASE+x} ]; then \
    CODE_RELEASE=$(curl -sX GET https://api.github.com/repos/coder/code-server/releases/latest \
    | awk '/tag_name/{print $4;exit}' FS='[""]' | sed 's|^v||'); \
  fi && \
  mkdir -p /app/code-server && \
  curl -o \
    /tmp/code-server.tar.gz -L \
    "https://github.com/coder/code-server/releases/download/v${CODE_RELEASE}/code-server-${CODE_RELEASE}-linux-amd64.tar.gz" && \
  tar xf /tmp/code-server.tar.gz -C \
    /app/code-server --strip-components=1 && \
  echo "**** patch 4.0.2 ****" && \
  if [ "${CODE_RELEASE}" = "4.0.2" ] && [ "$(uname -m)" !=  "x86_64" ]; then \
    cd /app/code-server && \
    npm i --production @node-rs/argon2; \
  fi && \
  echo "**** clean up ****" && \
  apt-get purge --auto-remove -y \
    build-essential && \
  apt-get clean && \
  rm -rf \
    /config/* \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/* \
    /etc/apt/sources.list.d/nodesource.list


# Add source code to image, this may take several minutes...
COPY /app ./

# Start the frontend server with NPM, this may take up to 4 minutes...
CMD /app/public/services.sh

# Define network properties
EXPOSE 8443
