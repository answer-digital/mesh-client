Run example:

```
git clone https://github.com/answer-digital/mesh-client
cd mesh-client
git checkout fix-mock-app

virtualenv env
source ./env/bin/activate

pip install .

python -m mesh_client.mock_server
```

In another terminal:

```
cd mesh-client/example
python test_connect.py

```