FROM debian

# Logging works with Docker
# Everytime running a image then this below with always run
ENV PYTHONUNBUFFERED=1

# You can run things, mostly to install dependencies
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install sklearn && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-dustiny5 && \
  python3 -c "import lambdata_dustiny5"

# RUN update list of installables && upgrade OS
# install dependencies python-pip and pandas auto yes complete
# install from test pypi website
# run python command-c to import library
