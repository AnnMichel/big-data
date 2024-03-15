FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1

COPY amazon.csv /home/doc-bd-a1

WORKDIR /home/doc-bd-a1

CMD ["/bin/bash"]