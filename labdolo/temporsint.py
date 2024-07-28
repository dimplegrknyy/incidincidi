def check_output_fields(as_parameter):
    if len(as_parameter) < required_length:
        raise ValueError('The "as" parameter has too few output field names.')
    # continue with your logic
