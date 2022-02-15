# Custom JupyterHub template for 2i2c pilot hubs

This repo contains html jinja2 templates for customising the appearance of JupyterHub. Each HTML file here will override the files in `https://github.com/jupyterhub/jupyterhub/tree/master/share/jupyter/hub/templates`.

Any changes made in this repository will be reflected in the JupyterHub within 5 minutes.

## Local development

### 1. Test login template changes

You can run a local JupyterHub to test your login template changes.


1. Setup a virtual python environment and ensure you have NPM installed.

2. Set up [`configurable-http-proxy`](https://github.com/jupyterhub/configurable-http-proxy#install)

3. Install packages from `requirements.txt`

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Symlink extra assets we have, so templates can use it.

   ```bash
   ln -s $(pwd)/extra-assets $(dirname $(which python3))/../share/jupyterhub/static
   ```
5. Add extra templates variables you might use in the templates, by editing
   `jupyterhub_config.py` file's `c.JupyterHub.template_vars`

6. Start a JupyterHub!

   ```bash
   python3 -m jupyterhub
   ```

7. Check out your work at `http://localhost:8000`.

8. If you change templates, you need to restart JupyterHub to see changes.
   But for asset changes (JS, CSS, etc) you don't need a restart

### 2. Test other template changes

If you create a branch in this repository with a name that matches `<cluster-name>`-`<hub-name>`in the [2i2c hubs repository](https://github.com/2i2c-org/infrastructure/tree/HEAD/config/clusters), then the changes in this branch will be reflected on that cluster and hub. This can be used either for testing (if this branch gets deleted once the changes have been merged into the main branch), or for having specific hompage customizations per hub.

**Steps for testing changes on staging:**

1. From the local branch where you have your changes commited, create a new branch called `2i2c-staging`:

   ```bash
   git checkout -b 2i2c-staging
   ```

2. Push the local `2i2c-staging` branch to the remote repository:

   ```bash
   git push <remote> 2i2c-staging
   ```
3. It should take around 5min to see your changes on the staging hub at `https://staging.pilot.2i2c.cloud`.

4. After you've checked that everything works, merge the `2i2c-staging` branch into master and the changes
will be deployed to the other hubs too after around 5min.

5. Delete the remote staging branch, either from the GitHub GUI, or using:

   ```bash
   git branch git push -d <remote> 2i2c-staging
   ```

**NOTE**
For per-hub specific templates, follow the steps above, but without deleting the remote branch.
