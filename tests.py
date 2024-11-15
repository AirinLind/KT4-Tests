import pytest
import requests

BASE_URL = "https://dog.ceo/api"


@pytest.fixture
def get_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    return response.json()


def test_get_all_breeds(get_breeds):
    """Проверка получения списка всех пород собак."""
    assert "breeds" in get_breeds
    assert isinstance(get_breeds["breeds"], dict)
    assert len(get_breeds["breeds"]) > 0


def test_get_images_of_breed():
    """Проверка получения изображений для породы."""
    breed = "bulldog"
    response = requests.get(f"{BASE_URL}/breeds/{breed}/images")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert isinstance(data["message"], list)
    assert len(data["message"]) > 0


def test_get_random_image_of_breed():
    """Проверка получения случайного изображения для породы."""
    breed = "bulldog"
    response = requests.get(f"{BASE_URL}/breeds/{breed}/images/random")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert isinstance(data["message"], str)


def test_get_random_image():
    """Проверка получения случайного изображения собаки."""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert isinstance(data["message"], str)


def test_get_random_fact():
    """Проверка получения случайного факта о собаках."""
    response = requests.get(f"{BASE_URL}/facts/random")
    data = response.json()
    assert response.status_code == 200
    assert "fact" in data
    assert isinstance(data["fact"], str)


def test_get_random_image_all_breeds():
    """Проверка получения случайного изображения для любой породы."""
    response = requests.get(f"{BASE_URL}/image/random")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert isinstance(data["message"], str)


def test_get_random_image_specific_breed():
    """Проверка получения случайного изображения для определенной породы."""
    breed = "labrador"
    response = requests.get(f"{BASE_URL}/image/{breed}/random")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert isinstance(data["message"], str)


def test_get_all_facts():
    """Проверка получения всех фактов о собаках."""
    response = requests.get(f"{BASE_URL}/facts")
    data = response.json()
    assert response.status_code == 200
    assert "facts" in data
    assert isinstance(data["facts"], list)


def test_get_random_fact():
    """Проверка получения случайного факта о собаках."""
    response = requests.get(f"{BASE_URL}/facts/random")
    data = response.json()
    assert response.status_code == 200
    assert "fact" in data
    assert isinstance(data["fact"], str)
