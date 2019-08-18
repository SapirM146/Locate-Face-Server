
# General
UNKNOWN = -1
REGISTER = "register"
RECOGNIZE_IN = "in"
RECOGNIZE_OUT = "out"
HOURS_REPORT = "hours_report"
HOURS_UPDATE = "hours_update"
ERROR_MESSAGE = "Error:"

# Sever
SERVER_HOST = 'localhost'
SERVER_PORT = 12470
SERVER_LOG = "server.log"
DEBUG_MODE = "debug"
ERROR_MODE = "error"


# Recognizer
THREAD_TRAIN_TIMER = 28800 # 8 hours in seconds
WIDTH = 80
HEIGHT = 80
DATASET_PATH = "dataset"
FISHERFACE_CONFIDENCE = 600
PATH_TO_TRAINER = 'trainer/trainer.yml'
TRAIN_FAILED = "Need at least 2 different faces to train the recognizer"
RECOGNIZE_FAILED = "Need to have at least 2 workers in order to use recognition function"


# Database
DATABASE_NAME = "faceLogin"
DATABASE_HOST = 'localhost' # enter yours
DATABASE_PORT = 3306


# Email
EMAIL_USER = 'facereco100@gmail.com'


# HOURS REPORT
HOURS_REPORT_FILE_NAME = "Hours_Report.xls"


# HOURS UPDATE
HOURS_UPDATE_IN = 1
HOURS_UPDATE_OUT = 2
HOURS_UPDATE_BOTH = 3


# AWS
AWS_SERVER_PUBLIC_KEY = "" # enter yours
AWS_SERVER_SECRET_KEY = "" # enter yours
REGION_NAME = "us-east-1" # enter yours
BUCKET_NAME = 'my-bucket' # enter yours