from flask import Blueprint, render_template, session
from CTFd.plugins import register_plugin_assets_directory
from CTFd.utils.decorators import authed_only

shell_plugin = Blueprint('ttyd_shell', __name__, template_folder='templates', static_folder='assets')

@shell_plugin.route('/shell')
@authed_only
def shell():
    return render_template('shell.html', username=session.get('name'))
