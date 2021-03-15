from mesh_client import MeshClient, LOCAL_MOCK_ENDPOINT
from mesh_client.mock_server import MOCK_SHARED_KEY
import os
from pprint import pprint

client1 = MeshClient(
    LOCAL_MOCK_ENDPOINT,
    "TESTSEND",
    "password",
    MOCK_SHARED_KEY,
    transparent_compress=True,
)
client1.handshake()


data = {
    "Body": open("test.txt", "rb"),
    "ContentLength": os.path.getsize("test.txt"),
}


client1.send_message(
    "TEST",
    subject="GP List Reconciliation: LNA 2021-03-07",
    filename="GPR4LNA.zip",
    data=data,
    workflow_id="GPExtract",
)


client2 = MeshClient(
    LOCAL_MOCK_ENDPOINT,
    "TEST",
    "password",
    MOCK_SHARED_KEY,
)
client2.handshake()

message_ids = client2.list_messages()
with client2.retrieve_message(message_ids[0]) as first_message:
    print("Subject:", first_message.subject)
    print("Message:", first_message.read())
    print("Filename:", first_message.filename)
    pprint(first_message.__dict__)


"""
Need:
    - Service account from which to send messages
        - Flag as unmonitored/send unmonitored autoreplies
        - Refuse mail or prune messages on schedule
    - Recipient name/MESH mailbox lookups
    - Go through Onboarding from https://digital.nhs.uk/developer/api-catalogue/message-exchange-for-social-care-and-health-api

    - Decide what kind of management tools we want for client side
    - workflowID for GP extract data?


"""
