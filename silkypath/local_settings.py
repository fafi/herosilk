
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "0dc1142d-a8f8-45ee-9cb7-520aff55f80366975dc7-e545-425d-843d-a78d55d7e5298a6523ba-0db9-46bc-bd37-642c9de60e2a"
NEVERCACHE_KEY = "937887e5-c204-4285-8cf7-f097b160b9178f30e107-79d4-42af-9e49-da82f30fbfb4df70dc31-6d94-48ff-ad44-e089cc472d63"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
		#"ENGINE": "mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "silkypath.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


# Copy this settings to your local_settings.py.
# Comment out the settings where you want to use defaults.

FABRIC = {
    # Webfaction SSH username
    "SSH_USER": "fafi",
    # Webfaction SSH password (You'll need this even if you use
    # key-based auth because of Webafaction's API)
    "SSH_PASS":  "factionfa1",
    # Local path to SSH key file, for key-based auth
    "SSH_KEY_PATH":  "",
    # The IP address of your Webfaction server
    "HOSTS": ["108.168.213.82", "2607:f0d0:1103:106:11::57"],
    # Unique identifier for project.
    # Default: container folder name.
    "PROJECT_NAME": "silkypath",
    # Absolute remote path for virtualenvs.
    # Default: $HOME/.virtualenvs
    "VIRTUALENV_HOME":  "",
    # Name of the remote virtualenv to use.
    # Default: PROJECT_NAME
    "VIRTUALENV_NAME":  "",
    # Path to pip requirements, relative to project.
    # Default: requirements/project.txt
    "REQUIREMENTS_PATH": "",
    # Locale for your live project. Should end with ".UTF-8"
    # Default: en_US.UTF-8
    "LOCALE": "",
    # Domain where the site will be deployed
    "LIVE_DOMAIN": "www.silkypath.com",
    # Subdomian where the site will be deployed
    "LIVE_SUBDOMAIN": "www.silkypath.com",
    # Git remote repo path for the project
    # Comment this out if you used prepare_webfaction
    # Default: $HOME/webapps/git/repos/PROJECT_NAME
    "REPO_PATH": "",
    # Live database user
    "DB_USER": "",
    # Live database password
    "DB_PASS": "",
    # Live admin user password
    "ADMIN_PASS": "",
    # Minutes between every time Twitter is polled
    # Optional, but requires mezzanine.twitter
    "TWITTER_PERIOD": "",
    # Make sure these keys are available here
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}


# Domains for public site
#ALLOWED_HOSTS = ["silkypath.com"]
#
#FABRIC = {
#    "DEPLOY_TOOL": "",  # Deploy with "git", "hg", or "rsync"
#    "SSH_USER": "",  # VPS SSH username
#    "HOSTS": ["72.9.151.72"],  # The IP address of your VPS
#    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#    "DB_PASS": "",  # Live database password
#    "ADMIN_PASS": "",  # Live admin user password
#    "SECRET_KEY": SECRET_KEY,
#    "NEVERCACHE_KEY": NEVERCACHE_KEY,
#	}
#	
#FABRIC = {
# "SSH_USER": "", # SSH username
# "SSH_PASS": "", # SSH password (consider key-based authentication)
# "HOSTS": ['72.9.151.72', ], # List of host names or IPs.
# #"VIRTUALENV_HOME": "/home/vagrant", # Absolute remote path for virtualenvs
# "PROJECT_NAME": "silkypath", # Unique identifier for project
# "REQUIREMENTS_PATH": "requirements/project.txt", # Path to pip requirements, relative to project
# "GUNICORN_PORT": 8000, # Port gunicorn will listen on
# "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
# "LIVE_HOSTNAME": "silkypath.com", # Host for public site.
# #"REPO_URL": "<repository_url>",
# "DB_PASS": "", # Live database password
# "ADMIN_PASS": "", # Live admin user password
# "SECRET_KEY": SECRET_KEY
#}