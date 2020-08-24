"""Validation functions for userService endpoints."""


def check_required_fields(request_data, target_model):
    """Dynamically check if the basic needed fields are present."""
    # TODO this should be moved to the FE
    return True if target_model.REQUIRED_FIELDS <= request_data else False
