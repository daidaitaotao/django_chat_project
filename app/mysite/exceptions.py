from rest_framework.exceptions import APIException

class RequestError(APIException):
    status_code = 400
    default_detail = "Bad Request."


class PermissionError(APIException):
    status_code = 403
    default_detail = "You do not have permission to perform this action."