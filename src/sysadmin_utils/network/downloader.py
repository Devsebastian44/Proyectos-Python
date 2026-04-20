import urllib.error
import urllib.parse
import urllib.request


def download_file(url: str, filename: str):
    """
    Downloads a file from a URL.
    """
    # Security: Validate URL scheme before downloading (S310)
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme not in ("http", "https"):
        raise ValueError(f"Unsupported URL scheme: {parsed_url.scheme}")

    try:
        urllib.request.urlretrieve(url, filename)  # noqa: S310
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error downloading file: {e}")


if __name__ == "__main__":
    # Example usage
    test_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    download_file(test_url, "google_logo.png")
