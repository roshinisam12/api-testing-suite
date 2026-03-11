import requests


class APIClient:
    """Reusable HTTP client with base URL, headers, and response helpers."""

    def __init__(self, base_url: str, headers: dict = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(headers or {"Content-Type": "application/json"})

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        return self.session.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint: str, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def put(self, endpoint: str, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}{endpoint}")

    @staticmethod
    def assert_status(response: requests.Response, expected: int):
        assert response.status_code == expected, (
            f"Expected status {expected}, got {response.status_code}. "
            f"Response: {response.text[:300]}"
        )

    @staticmethod
    def assert_response_time(response: requests.Response, max_ms: int = 2000):
        elapsed = response.elapsed.total_seconds() * 1000
        assert elapsed < max_ms, f"Response too slow: {elapsed:.0f}ms (max: {max_ms}ms)"
