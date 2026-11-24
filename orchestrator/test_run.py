import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
RUN = pathlib.Path(__file__).with_name("run.py")
class DispatcherTests(unittest.TestCase):
    def invoke(self, tasks, execute=False):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "config.json"
            p.write_text(json.dumps({"tasks": tasks}))
            return subprocess.run([sys.executable, str(RUN), str(p)] + (["--execute"] if execute else []), capture_output=True, text=True)
    def task(self, ident="demo", code="print('ok')"):
        return {"id":ident,"role":"REVIEWER","prompt":"demo","command":[sys.executable,"-c",code]}
    def test_dry(self):
        r=self.invoke([self.task(code="raise Exception()")])
        self.assertEqual(r.returncode,0)
        self.assertIn("Dry run",r.stdout)
    def test_execute(self):
        self.assertEqual(self.invoke([self.task()],True).returncode,0)
    def test_failure(self):
        r=self.invoke([self.task(code="raise SystemExit(2)"),self.task("next")],True)
        self.assertNotEqual(r.returncode,0)
        self.assertNotIn("Process exited successfully: next",r.stdout)
    def test_duplicate(self):
        self.assertNotEqual(self.invoke([self.task(),self.task()]).returncode,0)
    def test_invalid_id(self):
        self.assertNotEqual(self.invoke([self.task("../bad")]).returncode,0)
if __name__=="__main__":
    unittest.main()
