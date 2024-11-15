def test_create_user(client):
    data = {"email":"jsmithtest@users.com", "password":"supersecretpsw"}
    response = client.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == data["email"]
