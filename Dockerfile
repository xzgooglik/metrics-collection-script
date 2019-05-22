FROM python:2
RUN pip install psutil
ADD metrics.py .
RUN chmod 755 metrics.py
RUN chmod +x metrics.py


