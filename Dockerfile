FROM ubuntu
LABEL Bekzat Maxut
RUN apt-get update -y

#Installs python3 and numpy 
RUN apt-get install python3 python3-numpy -y

# Copies data.log sample log file and log_analyzer.py script
COPY  data.log  log_analyzer.py ./

# Using CMD and ENTRYPOINT instructions, we have instructed the 
# Container to run the log_analyzer.py Python script when the container is started.
CMD ["log_analyzer.py"]
ENTRYPOINT ["python3"]
