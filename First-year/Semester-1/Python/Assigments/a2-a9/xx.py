#
# Functions section
#
def create_candidate(candidate_id, candidate_name):
    return [candidate_id, candidate_name, 0]

def get_id(candidate):
    return candidate[0]

def get_name(candidate):
    return candidate[1]

def uni_id(candidates_list, id):
    for candidate in candidates_list:
        if candidate[0] == id:
            return False
    return True

def validate_candidate(candidate, candidates_list):
    if candidate[0] < 0:  # Correctly validating candidate ID
        raise ValueError("Candidate ID must be greater than or equal to 0")
    if not uni_id(candidates_list, candidate[0]):
        return False
    return True

def to_str(candidate):
    return ("candidate number " + str(candidate[0]) + ", " + str(candidate[1]) + " with " + str(candidate[2]) + " votes")

#
# User interface section
#
def add_candidate(candidates_list, inputs):
    word = inputs.split()
    candidate_id = int(word[1])  # Ensuring candidate_id is an integer
    if candidate_id < 0:
        raise ValueError("Candidate ID must be greater than or equal to 0")
    candidate_name = word[2]
    candidate = create_candidate(candidate_id, candidate_name)
    if validate_candidate(candidate, candidates_list):
        candidates_list.append(candidate)
    else:
        print("Candidate cannot be added")

def show_candidates(candidates_list, inputs):
    for candidate in candidates_list:
        print(to_str(candidate))

def commands():
    return {
        "add_candidate": add_candidate,
        "show_candidates": show_candidates,
    }

def menu():
    commands_list = commands()
    candidates = []
    while True:
        command_input = input(" >>> ")
        command = command_input.split()
        if command[0] in commands_list:
            commands_list[command[0]](candidates, command_input)
        elif command[0] == "exit":
            break
        else:
            print("Invalid command")

menu()

#
# Tests section
#
def test_create_candidate():
    candidate = create_candidate(1, "Alice")
    assert candidate == [1, "Alice", 0], "Test failed: create_candidate"

def test_get_id():
    candidate = create_candidate(1, "Alice")
    assert get_id(candidate) == 1, "Test failed: get_id"

def test_get_name():
    candidate = create_candidate(1, "Alice")
    assert get_name(candidate) == "Alice", "Test failed: get_name"

def test_uni_id():
    candidates_list = [
        create_candidate(1, "Alice"),
        create_candidate(2, "Bob")
    ]
    assert uni_id(candidates_list, 3) == True, "Test failed: uni_id (unique ID)"
    assert uni_id(candidates_list, 1) == False, "Test failed: uni_id (duplicate ID)"

def test_validate_candidate():
    candidates_list = [create_candidate(1, "Alice")]
    candidate = create_candidate(2, "Bob")
    assert validate_candidate(candidate, candidates_list) == True, "Test failed: validate_candidate (valid case)"
    candidate = create_candidate(1, "Charlie")
    assert validate_candidate(candidate, candidates_list) == False, "Test failed: validate_candidate (duplicate ID)"
    try:
        validate_candidate(create_candidate(-1, "Invalid"), candidates_list)
    except ValueError as e:
        assert str(e) == "Candidate ID must be greater than or equal to 0", "Test failed: validate_candidate (negative ID)"

def test_to_str():
    candidate = create_candidate(1, "Alice")
    assert to_str(candidate) == "candidate number 1, Alice with 0 votes", "Test failed: to_str"

def test_add_candidate():
    candidates_list = []
    add_candidate(candidates_list, "add_candidate 1 Alice")
    assert len(candidates_list) == 1, "Test failed: add_candidate (add valid)"
    assert candidates_list[0] == [1, "Alice", 0], "Test failed: add_candidate (correct data)"
    add_candidate(candidates_list, "add_candidate 1 Bob")
    assert len(candidates_list) == 1, "Test failed: add_candidate (prevent duplicate ID)"
    try:
        add_candidate(candidates_list, "add_candidate -1 Invalid")
    except ValueError as e:
        assert str(e) == "Candidate ID must be greater than or equal to 0", "Test failed: add_candidate (negative ID)"

# Run all tests
def run_tests():
    test_create_candidate()
    test_get_id()
    test_get_name()
    test_uni_id()
    test_validate_candidate()
    test_to_str()
    test_add_candidate()
    print("All tests passed!")

run_tests()
