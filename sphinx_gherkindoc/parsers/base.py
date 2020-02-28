"""Base classes for parsing."""


class BaseModel:
    """Base model for parsers."""

    def __init__(self, data):
        self._data = data

    def __getattr__(self, key):
        """Grab attribute from wrapped class, if present."""
        # Temporary work-around until Ryan's pytest-bdd PR lands:
        # Scenarios in pre-Ryan pytest-bdd do not have or permit descriptions.
        # To allow for either version of pytest-bdd, stub out description.
        # Once Ryan's pytest-bdd PR is in the published pytest-bdd,
        # this workaround can be removed.
        if key == "description":
            return getattr(self._data, key, None)
        return getattr(self._data, key)


class BaseFeature(BaseModel):
    """Feature base for parsers."""

    def __init__(self, root_path, source_path):
        self._data = None

    @property
    def examples(self):
        """Supports feature-level examples in some parsers."""
        return []
