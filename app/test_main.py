from app.main import get_human_age


def test_should_return_list_with_two_elements() -> None:
    assert len(get_human_age(1, 1)) == 2, (
        "resulted list must consist of 2 items"
    )


def test_should_return_0_if_pets_age_under_15() -> None:
    assert get_human_age(12, 14) == [0, 0], (
        "Pet's age under 15 should equal 0"
    )


def test_should_return_1_if_pets_age_under_24() -> None:
    assert get_human_age(23, 15) == [1, 1], (
        "Pet's age from 15 to 24 should equal 1"
    )


def test_add_1_every_4_years_after_24_for_cats() -> None:
    assert get_human_age(28, 0) == [3, 0], (
        "Cat's human age should increase by 1 every 4 years after 24"
    )


def test_add_1_every_5_years_after_24_for_dogs() -> None:
    assert get_human_age(0, 29) == [0, 3], (
        "Dog's human age should increase by 1 every 5 years after 24"
    )


def test_should_correctly_calculate_large_pet_ages() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "Human age should be correctly calculated for large pet ages"
    )
