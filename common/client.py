from io import BytesIO

import pandas as pd
import requests


class DataGovUAClient:
    """
    A client for fetching and handling datasets from data.gov.ua API.

    This class allows you to:
    - retrieve dataset metadata using the dataset ID,
    - extract resource URLs from metadata,
    - download and load Excel files into pandas DataFrames.

    Attributes:
        dataset_id (str): The unique identifier of the dataset.
        metadata (Optional[Dict]): The full metadata of the dataset, once fetched.
        resources (Optional[list]): A list of resources extracted from the metadata.
    """

    BASE_URL = "https://data.gov.ua/api/3/action/package_show?id="

    def __init__(self, dataset_id: str):
        self.dataset_id = dataset_id
        self.metadata: dict | None = None
        self.resources: list | None = None

    def fetch_metadata(self):
        """
        Fetch metadata for the dataset from the API.

        Raises:
            requests.HTTPError: If the request fails.
            ValueError: If required fields are missing in the response.
        """
        url = self.BASE_URL + self.dataset_id
        response = requests.get(url)
        response.raise_for_status()
        data: dict = response.json()

        if "result" in data:
            KeyError("Invalid metadata format: 'result' not found.")

        if "resources" in data["result"]:
            KeyError("Invalid metadata format: 'resources' not found.")

        self.metadata = data
        self.resources = data["result"]["resources"]
        print("Metadata and resources is fetched.")

    def get_resource_url(self, resource_id: str) -> str:
        """
        Get the download URL for a specific resource in the dataset.

        Args:
            resource_id (str): The identifier of the resource.

        Returns:
            str: The direct URL to download the resource.

        Raises:
            RuntimeError: If resources have not been fetched yet.
            ValueError: If the resource ID is not found.
        """
        if not self.resources:
            raise RuntimeError("Resources not loaded. Call fetch_metadata() first.")

        for res in self.resources:
            if res["id"] == resource_id:
                return res["url"]

        print("Resources urls received.")
        raise KeyError(f"Resource ID {resource_id} not found in dataset.")

    def load_dataframe(self, resource_url: str) -> pd.DataFrame:
        """
        Download an Excel file from the given resource URL and return it as a DataFrame.

        Args:
            resource_url (str): Direct URL to the Excel file.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.

        Raises:
            RuntimeError: If the file cannot be fetched.
        """
        try:
            response = requests.get(resource_url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch file: {e}") from e

        return pd.read_excel(BytesIO(response.content))
