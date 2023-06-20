pip install -r requirements.txt
pytest -s -v --alluredir=test_results/ tests
allure serve test_results/