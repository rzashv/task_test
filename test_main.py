import pytest
import json
from main import reader, splitter, username_generator, result


class LenError(Exception):
    ...



def read_data(test_name):
    with open("data_test.json", 'r') as t:
        x = json.load(t)

    input_data = x[test_name]["input"]
    output_data = x[test_name]["output"]

    return input_data, output_data


def test_reader():
    input, output = read_data("reader")
    if len(input) == len(output):
        for i in range(len(input)):
            assert reader(input[i]) == output[i]
    else:
        raise LenError('wrong length')
        
def test_splitter():
    input, output = read_data("splitter")
    if len(input) == len(output):
        for i in range(len(input)):
            assert splitter(input[i]) == output[i]
    else:
        raise LenError('wrong length')
    

def test_username_generator():
    input, output = read_data("username_generator")
    if len(input) == len(output):
        for i in range(len(input)):
            assert username_generator(input[i]) == output[i]
    else:
        raise LenError('wrong length')
    

def test_result():
    input, output = read_data("result")
    if len(input) == len(output):
        for i in range(len(input)):
            result("test_output_file.txt", input[i])
    else:
        raise LenError('wrong length')