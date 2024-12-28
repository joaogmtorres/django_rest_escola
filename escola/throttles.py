from rest_framework.throttling import AnonRateThrottle

class MatriculaAnonRate (AnonRateThrottle):
    rate = '5/day'