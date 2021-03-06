import glob
import subprocess
import re

files = glob.glob("task*py")
score = -1
for f in files:
    o = ""
    try:
        o = subprocess.check_output(("python -m doctest -v %s" % f).split(" "))
    except subprocess.CalledProcessError as e:
        o = e.output
    # print(str(o))  # debug info

    match = re.search("(\d) passed and (\d) failed", str(o))
    passed = int(match.group(1))
    failed = int(match.group(2))
    print("%s: %.1lf/1.0" % (f, passed / (passed + failed)))
    score += passed / (passed + failed)

print("Your score is: %.1lf/%d" % (score // 1, len(files) - 1))
