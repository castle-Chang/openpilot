from tools.lib.logreader import LogReader, MultiLogIterator
from tools.lib.robust_logreader import RobustLogReader
import subprocess
import sys

def test_multilogiterator():
    log_paths = [
        "test/fake_events1.json",
        "test/fake_events2.json"
    ]
    multi_log_iterator = MultiLogIterator(log_paths)

    reader1 = multi_log_iterator._log_reader(0)
    reader2 = multi_log_iterator._log_reader(1)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(reader1, ground_truth_ids):
        assert log.id == id, "Test 1 failed: MultiLogIterator returned incorrect order when sort_by_time is using default value"
    ground_truth_ids = [7,10,6,9,8]
    for log, id in zip(reader2, ground_truth_ids):
        assert log.id == id, "Test 2 failed: MultiLogIterator returned incorrect order when sort_by_time is using default value"

    multi_log_iterator = MultiLogIterator(log_paths, sort_by_time=False)
    reader1 = multi_log_iterator._log_reader(0)
    reader2 = multi_log_iterator._log_reader(1)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(reader1, ground_truth_ids):
        assert log.id == id, "Test 1 failed: MultiLogIterator returned incorrect order when sort_by_time is set to False"
    ground_truth_ids = [7,10,6,9,8]
    for log, id in zip(reader2, ground_truth_ids):
        assert log.id == id, "Test 2 failed: MultiLogIterator returned incorrect order when sort_by_time is set to False"

    multi_log_iterator = MultiLogIterator(log_paths, sort_by_time=True)
    reader1 = multi_log_iterator._log_reader(0)
    reader2 = multi_log_iterator._log_reader(1)
    ground_truth_ids = [3,1,0,4,2]
    for log, id in zip(reader1, ground_truth_ids):
        assert log.id == id, "Test 1 failed: MultiLogIterator returned incorrect order when sort_by_time is set to True"
    ground_truth_ids = [9,10,7,8,6]
    for log, id in zip(reader2, ground_truth_ids):
        assert log.id == id, "Test 2 failed: MultiLogIterator returned incorrect order when sort_by_time is set to True"
    
    print("Test 2 passed.")
    
def test_logreader():
    log_path = "test/fake_events1.json"
    log_reader = LogReader(log_path)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is using default value"

    log_reader = LogReader(log_path, sort_by_time=False)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is set to False"

    log_reader = LogReader(log_path, sort_by_time=True)
    ground_truth_ids = [3,1,0,4,2]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is set to True"

    print("Test 1 passed.")

def test_logreader_main():
    result = subprocess.run(
        ["python", "-m", "tools.lib.logreader", "test/fake_events1.json"],
        capture_output=True,
        text=True,
        check=True
    )
    ground_truth_ids = [3,1,0,4,2]
    for id, line in zip(ground_truth_ids, result.stdout.splitlines()):
        assert line == str(id), f"Test 3 failed: logreader.py:__main__ returned incorrect order."

    print("Test 3 passed.")

def test_robust_logreader():
    log_path = "test/fake_events1.json"
    log_reader = RobustLogReader(log_path)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is using default value"

    log_reader = RobustLogReader(log_path, sort_by_time=False)
    ground_truth_ids = [0,1,2,3,4]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is set to False"

    log_reader = RobustLogReader(log_path, sort_by_time=True)
    ground_truth_ids = [3,1,0,4,2]
    for log, id in zip(log_reader, ground_truth_ids):
        assert log.id == id, "Test 1 failed: LogReader returned incorrect order when sort_by_time is set to True"

    print("Test 4 passed.")
if __name__ == '__main__':
    # Test 1:
    test_logreader()

    # Test 2:
    test_multilogiterator()
    
    # Test 3:
    test_logreader_main()

    # Test 4:
    test_robust_logreader()
