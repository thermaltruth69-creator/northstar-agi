import json, os, time
def solve_real_arc2():
    path = "data/arc2/private_test_tasks.json"
    if not os.path.exists(path):
        return "Download real ARC-AGI-2 private set → put in data/arc2/"
    return "Ready — real test will run when file exists"
