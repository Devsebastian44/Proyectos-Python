import ftplib  # nosec B402
import os
from pathlib import Path
from typing import List


class FTPClient:
    """
    A simple FTP client for uploading and downloading files.
    """

    def __init__(self, host: str, user: str, password: str):
        self.host = host
        self.user = user
        self.password = password
        self.ftp = None

    def connect(self):
        """Establishes connection to the FTP server."""
        try:
            # ftplib is used for legacy FTP support as required by the tool's purpose.
            # For secure transfers, SFTP or FTPS should be used.
            self.ftp = ftplib.FTP(  # nosec B310, B321 # noqa: S310, S321
                self.host, self.user, self.password, timeout=30
            )
            self.ftp.encoding = "utf-8"
            print(f"Connected to {self.host}")
        except Exception as e:
            print(f"Error connecting to FTP: {e}")
            raise

    def list_files(self) -> List[str]:
        """Lists files in the current directory."""
        if not self.ftp:
            self.connect()
        try:
            return self.ftp.nlst()
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def upload_file(self, local_path: str, remote_filename: str = None):
        """Uploads a local file to the FTP server."""
        if not self.ftp:
            self.connect()

        local_path_obj = Path(local_path)
        if not local_path_obj.exists():
            print(f"File not found: {local_path_obj}")
            return

        remote_filename = remote_filename or local_path_obj.name

        try:
            with open(local_path_obj, "rb") as file:
                self.ftp.storbinary(f"STOR {remote_filename}", file)
            print(f"Uploaded {local_path_obj} to {remote_filename}")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_filename: str, local_path: str = None):
        """Downloads a file from the FTP server."""
        if not self.ftp:
            self.connect()

        local_path = local_path or remote_filename

        try:
            with open(local_path, "wb") as file:
                self.ftp.retrbinary(f"RETR {remote_filename}", file.write)
            print(f"Downloaded {remote_filename} to {local_path}")
        except Exception as e:
            print(f"Error downloading file: {e}")

    def close(self):
        """Closes the FTP connection."""
        if self.ftp:
            try:
                self.ftp.quit()
            except Exception:
                self.ftp.close()
            print("FTP connection closed.")


if __name__ == "__main__":
    # Example usage (Use environment variables for actual credentials)
    HOST = os.getenv("FTP_HOST", "ftp.example.com")
    USER = os.getenv("FTP_USER", "user")
    PASS = os.getenv("FTP_PASS", "")

    if not PASS:
        print("Skipping FTP test (no password provided).")
        exit(0)

    client = FTPClient(HOST, USER, PASS)
    try:
        client.connect()
        print(client.list_files())
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client.close()
