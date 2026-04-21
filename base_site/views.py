import logging

from django.db import connection
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def wake_up(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT fn_prevent_pausing()")
        result = cursor.fetchone()
    logger.info("Returned rows: %s", result[0])
    return HttpResponse("OK")
