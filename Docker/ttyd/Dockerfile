FROM debian:bullseye

# Install basic tools
RUN apt-get update && \
    apt-get install -y curl git build-essential cmake libjson-c-dev libwebsockets-dev zlib1g-dev pkg-config bash sudo iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Build ttyd
RUN git clone https://github.com/tsl0922/ttyd.git /opt/ttyd && \
    cd /opt/ttyd && \
    mkdir build && cd build && \
    cmake .. && make && make install

# Create non-root user
ARG USERNAME=ctfuser
RUN useradd -m ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Copy start script
COPY start.sh /home/${USERNAME}/start.sh
RUN chmod +x /home/${USERNAME}/start.sh

# Set working directory
USER ${USERNAME}
WORKDIR /home/${USERNAME}

# Expose port
EXPOSE 7681

# Start ttyd (listen on port 7681)
CMD ["ttyd", "--writable", "-p", "7681", "./start.sh"]
