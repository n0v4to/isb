from NIST_tests import *


if __name__ == "__main__":
    config = read_json("settings_file.json")
    sequences = read_json(config["From"])
    sequences_cpp = sequences["C++"]
    sequences_java = sequences["Java"]
    frequency_test_nist(sequences_cpp, config["To"], "C++")
    frequency_test_nist(sequences_java, config["To"], "Java")
    same_bits_test_nist(sequences_cpp, config["To"], "C++")
    same_bits_test_nist(sequences_java, config["To"], "Java")
    longest_run_ones_test_nist(sequences_cpp, config["To"], "C++")
    longest_run_ones_test_nist(sequences_java, config["To"], "Java")
