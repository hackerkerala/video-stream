import config
from config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    LOG_GROUP_ID,
    MONGO_DB_URI,
    OWNER_ID,
    SUDO_USERS,
)


def initialize():
    global dbb
    dbb = {}

### Mongo DB
MONGODB_CLI = Bot(mango)
db = MONGODB_CLI
pymongodb = ""

### Boot Time
boottime = time.time()

### Clients
app = app
userbot = userbot
aiohttpsession = ClientSession()


initialize()

print("[INFO]: INITIALIZING DATABASE")
MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
SUDOERS = SUDO_USERS
OWNER = OWNER_ID


async def load_sudoers():
    global SUDOERS
    print("[INFO]: LOADING SUDO USERS")
    sudoersdb = db.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDOERS:
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
            )
    SUDOERS = (SUDOERS + sudoers) if sudoers else SUDOERS
    print("[INFO]: LOADED SUDO USERS")


    
def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    getme = app.get_me()
    getme1 = client.get_me()
    BOT_ID = getme.id
    ASSID = getme1.id
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username

    
