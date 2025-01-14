# global variables init
import dotenv, os

dotenv.load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
TEST_GUILD_ID = os.getenv('DISCORD_TEST_GUILD_ID')
PROFESSOR_ROLE_NAME = os.getenv('PROFESSOR_ROLE_NAME')
HEAD_TA_ROLE_NAME = os.getenv('AUXILIAR_ROLE_NAME')
TA_ROLE_NAME = os.getenv('ASSISTANT_ROLE_NAME')
STUDENT_ROLE_NAME = os.getenv('STUDENT_ROLE_NAME')

DEFAULT_ENV_VALUES = {
    "GENERAL_TEXT_CHANNEL_NAME" : os.getenv('GENERAL_TEXT_CHANNEL_NAME'),
    "GENERAL_VOICE_CHANNEL_NAME" : os.getenv('GENERAL_VOICE_CHANNEL_NAME'),
    "PRIVATE_TEXT_CHANNEL_NAME" : os.getenv('PRIVATE_TEXT_CHANNEL_NAME'),
    "PRIVATE_VOICE_CHANNEL_NAME" : os.getenv('PRIVATE_VOICE_CHANNEL_NAME'),
    "MAX_STUDENTS_PER_GROUP" : 3,
    "REQUIRE_NICKNAME": True,
    "BROADCAST_TO_EMPTY_GROUPS": True,
    "TT_ROLES" : [PROFESSOR_ROLE_NAME, HEAD_TA_ROLE_NAME, TA_ROLE_NAME]
}