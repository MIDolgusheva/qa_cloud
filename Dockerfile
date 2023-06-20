FROM python
WORKDIR /qa/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python -m pytest -s --alluredir=test_results/ /qa/