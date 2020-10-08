import pathlib
from oauthenticator.generic import GenericOAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner


c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

HERE = pathlib.Path(__file__).parent

c.JupyterHub.template_paths = [str(HERE / 'templates')]

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.Authenticator.admin_users = [
    'yuvipanda'
]

c.JupyterHub.template_vars = {
    'hub': {
        'org_name': 'Hello world',
        'org_image': 'wat'
    }
}
