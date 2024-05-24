import requests
import json
import string
import random
import pytest

# base url:
base_url = "https://gorest.co.in"

# Auth token:
auth_token = "Bearer 44d49cbdbc0b9d66fd403226121e74c2c664578ad10b2fcce18ec1926d29d46a"

# get random email id:
def generate_random_email():
    domain = "acharya.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#POST Request to create an user with new user ID.
@pytest.fixture(scope="module")
def create_user():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Samarpan Acharya",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body: ", json_str)
        user_id = json_data["id"]
        print("user id ===>", user_id)
        assert response.status_code == 201
        print("==========POST/User is created========")
        yield user_id
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])

    # GET Request to retrieve user info and validate the same
def test_retrieve_and_validate_usersInfo(create_user,get_EnvName):
    if get_EnvName == "Staging" or get_EnvName == "Production":
        url = base_url + f"/public/v2/users/{create_user}"
        print("get url: " + url)
        headers = {"Authorization": auth_token}
        try:
            response = requests.get(url, headers=headers)
            assert response.status_code == 200
            json_data = response.json()
            assert json_data["id"] == create_user
            print("user id ===>", create_user)
            assert json_data["name"] == "Samarpan Acharya"
            json_str = json.dumps(json_data, indent=4)
            print("json GET response body: ", json_str)
            print("=========VALIDATING USER PROFILE INFO IS DONE============")
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
    else:
        assert False, "Sorry, Can't run these TCs on other than Staging/Production"

# # PATCH Request to update the user's profile name and verify the update
def test_update_user_profileInfo_and_verify(create_user,get_EnvName):
    if get_EnvName == "Staging" or get_EnvName == "Production":
        url = base_url + f"/public/v2/users/{create_user}"
        print("PATCH url: " + url)
        headers = {"Authorization": auth_token}
        data = {
             "name": "Shiva Raj Acharya"
           }
        try:
            response=requests.patch(url, json=data, headers=headers)
            assert response.status_code == 200
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("json PUT response body: ", json_str)
            assert json_data["id"] == create_user
            assert json_data["name"] == "Shiva Raj Acharya"
            print(".......UPDATING USER PROFILE DONE.......")
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
    else:
        assert False, "Sorry, Can't run these TCs on other than Staging/Production"




