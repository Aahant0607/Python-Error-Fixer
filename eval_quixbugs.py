import os
from app import load_code, fix_code_with_model, run_tests_on_fixed_code

BUGGY_DIR = "Code-Refactoring-QuixBugs/python_programs"
RESULT_FILE = "results.txt"

def evaluate_all_programs():
    total = 0
    passed = 0
    failed_files = []

    with open(RESULT_FILE, "w") as result_log:
        result_log.write("📊 Evaluation Results\n\n")

        for filename in os.listdir(BUGGY_DIR):
            if filename.endswith(".py"):
                total += 1
                path = os.path.join(BUGGY_DIR, filename)
                code = load_code(path)
                fixed_code = fix_code_with_model(code)
                test_result = run_tests_on_fixed_code(fixed_code)

                result_log.write(f"{filename} — {test_result}\n")

                if "All tests passed" in test_result:
                    passed += 1
                else:
                    failed_files.append(filename)

        summary = f"\n✅ Passed: {passed}/{total}\n❌ Failed: {len(failed_files)}\n"
        result_log.write(summary)
        result_log.write("\nFailed Files:\n" + "\n".join(failed_files))

    print("📁 Results saved to results.txt")
