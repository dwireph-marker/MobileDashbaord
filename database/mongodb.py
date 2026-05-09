# =====================================================
# FILE: database/mongodb.py
# =====================================================

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

DATABASE_NAME = os.getenv("DATABASE_NAME")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# =====================================================
# CHECK ENV VARIABLES
# =====================================================

if not MONGO_URI:

    raise Exception(
        "MONGO_URI not found in .env file"
    )

# =====================================================
# CONNECT TO MONGODB
# =====================================================

try:

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    # =============================================
    # UNIQUE MODEL INDEX
    # =============================================

    collection.create_index(
        [("model", 1)],
        unique=True
    )

    print(
        "MongoDB Connected Successfully"
    )

except Exception as e:

    print(
        "MongoDB Connection Error:",
        e
    )

# =====================================================
# GET ALL DEVICES
# =====================================================

def get_all_devices():

    try:

        data = list(
            collection.find()
        )

        return data

    except Exception as e:

        print(
            "Fetch Error:",
            e
        )

        return []

# =====================================================
# ADD DEVICE
# =====================================================

def add_device(device_data):

    try:

        result = collection.insert_one(
            device_data
        )

        return result.inserted_id

    except Exception as e:

        print(
            "Insert Error:",
            e
        )

        return None

# =====================================================
# DELETE DEVICE
# =====================================================

def delete_device(model_name):

    try:

        result = collection.delete_one({

            "model": model_name
        })

        return result.deleted_count > 0

    except Exception as e:

        print(
            "Delete Error:",
            e
        )

        return False

# =====================================================
# UPDATE DEVICE
# =====================================================

def update_device(
    old_model,
    updated_data
):

    try:

        result = collection.update_one(

            {
                "model": old_model
            },

            {
                "$set": updated_data
            }
        )

        return result.modified_count > 0

    except Exception as e:

        print(
            "Update Error:",
            e
        )

        return False