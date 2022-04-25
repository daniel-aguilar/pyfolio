from datetime import datetime

from . import __version__


def version(request):
    return {'project_version': __version__}


def current_year(request):
    return {'current_year': datetime.today().strftime('%Y')}
