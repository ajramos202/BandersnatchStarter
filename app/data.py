from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

load_dotenv()


class Database:
    def __init__(self):
        '''Initializing and connecting to MongoDB'''
        self.db_url = getenv("DB_URL")

        # Connect to MongoDB
        self.client = MongoClient("mongodb+srv://ajramos202:gocRRJEmKUOKBvNH@cluster1.qnioq.mongodb.net/",
                                  tlsCAFile=where())
        self.db = self.client["LabsDB"]
        self.collection = self.db["Monsters"]
        print("Databases:", self.client.list_database_names())

    def seed(self, amount):
        '''Function that inserts the specified number of documents
        into the collection'''
        monsters = [Monster() for _ in range(amount)]
        monsters_dict = [monster.to_dict() for monster in monsters]

        # Insert the generated monsters into the MongoDB collection
        self.collection.insert_many(monsters_dict).acknowledged
        print("Seeding comlplete.")

    def reset(self):
        '''Function to delete all documents from collection'''
        self.collection.delete_many({}).acknowledged

    def count(self) -> int:
        '''Function to return the number of documents in the collection'''
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        '''Function that returns the entire collection as a dataframe'''
        documents = list(self.collection.find({}))
        df = DataFrame(documents)
        return df

    def html_table(self) -> str:
        '''Function that returns an HTML table representation
        of the dataframe'''
        df = self.dataframe()
        return df.to_html() if not df.empty else None


if __name__ == "__main__":

    db = Database()

    print("Seeding the collection with 1,000 documents...")
    db.seed(1000)

    print("Counting the documents in the collection...")
    print(f"Total documents: {db.count()}")

    print("Creating a DataFrame from the collection...")
    print(db.dataframe())

    print("Generating an HTML table from the DataFrame...")
    print(db.html_table())

    # print("Resetting the collection...")
    # db.reset()
