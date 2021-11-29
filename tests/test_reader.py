# from context import manifest_to_helm
from manifest_to_helm.reader import Chart
import json
from tests import testing_utils

def test_load_manifest():
	chart = Chart(name="test_chart", description="A test chart")

	chart.load_manifest('tests/resources/test_load_manifest/in')

	with open('tests/resources/test_load_manifest/out/ground_truth.json') as f:
		ground_truth = json.load(f)
	assert chart.data['test'] == ground_truth

def test_loads_manifest():
	chart = Chart(name="test_chart", description="A test chart")

	with open('tests/resources/test_loads_manifest/in/test.yaml') as f:
		contents = f.read()
		
	chart.loads_manifest(contents, 'test')

	with open('tests/resources/test_loads_manifest/out/ground_truth.json') as f:
		ground_truth = json.load(f)
	assert chart.data['test'] == ground_truth

def test_load_patterns():
	chart = Chart(name="test_chart", description="A test chart")

	chart.load_patterns('tests/resources/test_load_patterns/in/test.json')

	with open('tests/resources/test_load_patterns/out/ground_truth.json') as f:
		ground_truth = json.load(f)
	assert chart.patterns == ground_truth

def test_build_chart():
	chart = Chart(name="test_chart", description="A test chart")
	chart.load_manifest('tests/resources/test_build_chart/in')
	chart.load_patterns('tests/resources/test_build_chart/patterns.json')
	chart.build_chart()

	with open('tests/resources/test_build_chart/out/ground_truth.json') as f:
		ground_truth = json.load(f)
	assert chart.output == ground_truth

def test_dump_chart():
	chart = Chart(name="test_chart", description="A test chart")
	chart.load_manifest('tests/resources/test_dump_chart/in')
	chart.load_patterns('tests/resources/test_dump_chart/patterns.json')
	chart.build_chart()
	chart.dump_chart('tests/resources/test_dump_chart/out/test', delete_existing=True)
	
	assert testing_utils.is_same('tests/resources/test_dump_chart/out/test', 'tests/resources/test_dump_chart/out/ground_truth')

	