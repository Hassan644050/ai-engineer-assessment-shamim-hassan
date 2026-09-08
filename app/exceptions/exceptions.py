class AppException(Exception):
    """Base exception for application-specific errors."""


class SuperheroAPIException(AppException):
    """Raised when the Superhero API cannot be used."""


class LLMException(AppException):
    """Raised when the LLM service cannot be used."""

class LLMRateLimitException(LLMException):
    """Raised when the LLM rate limit is exceeded."""


class LLMProviderException(LLMException):
    """Raised when the LLM provider returns an error."""