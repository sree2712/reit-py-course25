def calculate_bmi(weight_kg, height_m):
    """
    Compute Body Mass Index (BMI) from weight and height.

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI value.

    Raises:
        ValueError: If height is zero or negative.
    """
    if height_m <= 0:
        error_msg = f"Height must be greater than zero, got {height_m}"
        raise ValueError(error_msg)
    return weight_kg / height_m**2
